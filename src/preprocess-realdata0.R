library(tidyverse)
library(magrittr)
library(data.table)
library(naniar)
library(caret)

normalize <- function(x)  {
  return ((x - mean(x, na.rm = TRUE)) / sd(x, na.rm = TRUE))
}

# Rename, reformat vars; create outcome var
full_dat1 <- fread("../data/fdata.csv")

full_dat <- full_dat1 %>%
  mutate(MaritalStatus=recode(MaritalStatus, `1` = 1, `2`= 0)) %>%
  mutate(Race=recode(Race, `1` = "White", 
                     `2` = "Black", 
                     `3` = "AmeriIndian", 
                     `4` = "AsianPI")) %>%
  mutate(Education=recode(Education, `1` = "lteq8",
                          `2` = "HSIncomplete",
                          `3` = "HSGraduate",
                          `4` = "CollIncomplete",
                          `5` = "Associate",
                          `6` = "Bachelor",
                          `7` = "Master",
                          `8` = "Doctorate"
  )) %>%
  replace_with_na(replace = list(PrevTerminations = 99, BMI = 99.9, Height = 99, Weight = 999, PrevPretermBirths = "", PrevCesareans = "", PrepregnancySmoking = 99, Parity = 9, Preterm = 99)) %>%
  mutate(WIC=recode(WIC, "N" = 0, "Y" = 1)) %>%
  mutate(PrevPretermBirths=recode(PrevPretermBirths, "N" = 0, "Y" = 1)) %>%
  mutate(PrevCesareans=recode(PrevCesareans, "N" = 0, "Y" = 1)) %>%
  mutate(PrepregnancyDiabetes=recode(PrepregnancyDiabetes, "N" = 0, "Y" = 1)) %>%
  mutate(GestationalDiabetes=recode(GestationalDiabetes, "N" = 0, "Y" = 1)) %>%
  mutate(PrepregnancyHypertension=recode(PrepregnancyHypertension, "N" = 0, "Y" = 1)) %>%
  mutate(GestationalHypertension=recode(GestationalHypertension, "N" = 0, "Y" = 1)) %>%
  mutate(HypertensionEclampsia=recode(HypertensionEclampsia, "N" = 0, "Y" = 1)) %>%
  mutate(InfertilityTreatment=recode(InfertilityTreatment, "N" = 0, "Y" = 1)) %>%
  mutate(InfertilityDrugs=recode(InfertilityDrugs, "N" = 0, "Y" = 1)) %>%
  mutate(ART=recode(ART, "N" = 0, "Y" = 1)) %>%
  mutate(Gonorrhea=recode(Gonorrhea, "N" = 0, "Y" = 1)) %>%
  mutate(Syphilis=recode(Syphilis, "N" = 0, "Y" = 1)) %>%
  mutate(Chlamydia=recode(Chlamydia, "N" = 0, "Y" = 1)) %>%
  mutate(HepatitisB=recode(HepatitisB, "N" = 0, "Y" = 1)) %>%
  mutate(HepatitisC=recode(HepatitisC, "N" = 0, "Y" = 1)) %>%
  mutate(outcome = case_when(
    Stillborn == 0 & Preterm < 37  ~ "preterm",
    Stillborn == 0 & Preterm >= 37 ~ "normal",
    Stillborn == 1 & Preterm < 28  ~ "early stillbirth",
    Stillborn == 1 & Preterm >= 28 ~ "late stillbirth"
  ))
message('reformat complete')

# Drop based on exclusion criteria; normalize continuous variables; create one-hots
rm(full_dat1)  # cove needs this aha
gc()
full_dat <- full_dat %>%
  filter(!(Preterm < 21 & Stillborn == 0)) %>%
  filter(Age >= 18) %>%
  dplyr::mutate(id = dplyr::row_number()) %>%
  mutate(BMI = normalize(BMI)) %>%
  mutate(Height = normalize(Height)) %>%
  # Excluded weight
  # mutate(Weight = normalize(Weight)) %>%
  # The authors called these "discrete" variables so it was unclear whether or not they normalized them
  mutate(PrepregnancySmoking = normalize(PrepregnancySmoking)) %>%
  mutate(PrevTerminations = normalize(PrevTerminations)) %>%
  mutate(Parity = normalize(Parity))
message('normalize complete')
fwrite(full_dat, '../data/fdata_preproc_not_hot.csv')
