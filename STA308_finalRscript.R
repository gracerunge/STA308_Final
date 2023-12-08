##################################
#* Author: Grace Runge 
#* 
#* Date: 12/8/2023
#* 
#* Purpose: To fulfill the requirements of the STA 308 final exam.
#*   Given 4 different data sets, for four census regions, compute the mean 
#*   state percentage difference in the flu-pneumonia mortality 
#*   rates from 2018 to 2021 as well as the corresponding standard deviation 
#*   and coefficient of variation. 
#* 
#* ###############################

## Load tidyverse
library(tidyverse) 

## Load in the required data
mortality2018 <- read_csv("https://tjfisher19.github.io/data/fluPneumonia_2018.csv")
mortality2021 <- read_csv("https://tjfisher19.github.io/data/fluPneumonia_2021.csv")
state_codes <- read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
census_regions <- read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

## Change rate variable names for easier handling
mortality2018 <- mortality2018 %>%
  rename("Rate2018" = "Rate")

mortality2021 <- mortality2021 %>%
  rename("Rate2021" = "Rate")

## Remove Alaska and Hawaii 
mortality2018 <- mortality2018 %>%
  filter(State != "AK") %>%
  filter(State != "HI")

mortality2021 <- mortality2021 %>%
  filter(State != "Alaska") %>%
  filter(State != "Hawaii")

#* Merge the 4 data frames together so left with only desired information:
#*    state code, region, and rates from both 2018 and 2021 

# Use the additional data set given to change state names to codes 
add_abbreviations <- merge(mortality2021, state_codes)

new_2021 <- add_abbreviations %>% 
  select("Rate2021", "Code")

# combine both years by code
both_mortality <- merge(new_2021, mortality2018, by.x = "Code", by.y = "State")

# combine with census region data 
both_mortality <- merge(both_mortality, census_regions, by.x = "Code", by.y = "State")


# For each of the four census regions: 
#   compute the mean state percentage difference in rates 
#   from 2018 to 2021 (Rate2018 - Rate2021)/Rate2018*100)
#   and the standard deviation and coefficient of variation (mean/std)

## Add variable for percent difference to data frame 
both_mortality <- both_mortality %>%
  mutate(mean_diff = (Rate2018-Rate2021)/Rate2018*100)

## Compute the mean, std, and CV and show summary info 
both_mortality %>%
  group_by(Region) %>%
  summarise(mean(mean_diff), sd(mean_diff), sd(mean_diff)/mean(mean_diff))



