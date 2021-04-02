library(tidyverse)
library(magrittr)
library(data.table)
library(naniar)
library(caret)

################################################################################

full_dat <- fread('../data/fdata_preproc_hot.csv')

# Make specific dataset for stillbirth, dropping NAs
stillbirth_Classify <- full_dat %>%
  select(-Gonorrhea, -Syphilis, -Chlamydia, -HepatitisB, -HepatitisC, -MaritalStatus, -PrevPretermBirths, -ART, -InfertilityDrugs) %>%
  na.omit()

rm(full_dat)
fwrite(stillbirth_Classify, "../data/final/stillbirth_classify.csv")
message('wrote full stillbirth file:')

# Split stillbirth into train, feature selection, validation, and test sets
idx_train <- stillbirth_Classify$outcome %>% createDataPartition(p = 0.7, list = FALSE)
stillbirth_train <- stillbirth_Classify[idx_train, ]
fwrite(stillbirth_train, "../data/final/stillbirth_train.csv")
rm(stillbirth_train)
message('wrote stillbirth train')

holdout <- stillbirth_Classify[-idx_train, ]
idx_feature <- holdout$outcome %>% createDataPartition(p = 1/3, list = FALSE)
stillbirth_feature <- holdout[idx_feature, ]
fwrite(stillbirth_feature, "../data/final/stillbirth_feature.csv")
rm(stillbirth_feature)
message('wrote stillbirth feature')

holdout <- holdout[-idx_feature, ]
idx_val <- holdout$outcome %>% createDataPartition(p = 1/2, list = FALSE)
stillbirth_val <- holdout[idx_val, ]
fwrite(stillbirth_val, "../data/final/stillbirth_val.csv")
rm(stillbirth_val)
message('wrote stillbirth val')

stillbirth_test <- holdout[-idx_val, ]
fwrite(stillbirth_test, "../data/final/stillbirth_test.csv")
message('wrote stillbirth test')