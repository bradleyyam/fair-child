library(tidyverse)
library(magrittr)
library(data.table)
library(naniar)
library(caret)

################################################################################

full_dat <- fread('../data/fdata_preproc_hot.csv')

preterm_Classify <- full_dat %>%
    select(-ART, -InfertilityDrugs) %>%
    na.omit()

rm(full_dat)
fwrite(preterm_Classify, "../data/final/preterm_classify.csv")
message("wrote full preterm file:")

# Split preterm into train, feature selection, validation, and test sets
idx_train <- preterm_Classify$outcome %>% createDataPartition(p = 0.7, list = FALSE)
preterm_train <- preterm_Classify[idx_train, ]
fwrite(preterm_train, "../data/final/preterm_train.csv")
rm(preterm_train)
message("wrote preterm train")

holdout <- preterm_Classify[-idx_train, ]
idx_feature <- holdout$outcome %>% createDataPartition(p = 1/3, list = FALSE)
preterm_feature <- holdout[idx_feature, ]
fwrite(preterm_feature, "../data/final/preterm_feature.csv")
rm(preterm_feature)
message("wrote preterm feature")

holdout <- holdout[-idx_feature, ]
idx_val <- holdout$outcome %>% createDataPartition(p = 1/2, list = FALSE)
preterm_val <- holdout[idx_val, ]
fwrite(preterm_val, "../data/final/preterm_val.csv")
rm(preterm_val)
message("wrote preterm val")

preterm_test <- holdout[-idx_val, ]
fwrite(preterm_test, "../data/final/preterm_test.csv")
message("wrote preterm test")