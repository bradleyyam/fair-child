library(tidyverse)
library(magrittr)
library(data.table)
library(naniar)
library(caret)

full_dat <- fread('../data/fdata_preproc_not_hot.csv')

full_dat <- full_dat %>%
  mutate(Race = paste("race", Race, sep = "_"),
         race_hot = 1,
         Education = paste("education", Education, sep = "_"),
         education_hot = 1) %>%
  tidyr::spread(key = Race, value = race_hot, fill = 0) %>%
  tidyr::spread(key = Education, value = education_hot, fill = 0) %>%
  select(-id, -Version, -DeliveryYear, -Weight, -Stillborn, -Preterm)
message('one-hot creation complete!')

fwrite(full_dat, '../data/fdata_preproc_hot.csv')
message('wrote full preprocessed file')