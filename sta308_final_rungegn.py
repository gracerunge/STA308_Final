# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:51:32 2023

@author: Grace Runge 

Purpose of this script: 
    This script is to fulfill the requirements of the 
    STA 308 Fall 2023 take home final examination.
    
    For four census regions, compute the mean state 
    percentage difference in the flu-pneumonia mortality 
    rates from 2018 to 2021 as well as the standard deviation 
    and coefficient of variation.
    
    Note: Alaska and Hawaii are to be removed since they 
    are not in the contiguous United States 

"""

## load the pandas package to help with data wrangling and munging
import pandas as pd 

# load the required data sets 
mortality_2018 = pd.read_csv("https://tjfisher19.github.io/data/fluPneumonia_2018.csv")
mortality_2021 = pd.read_csv("https://tjfisher19.github.io/data/fluPneumonia_2021.csv")
state_codes = pd.read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
census_regions = pd.read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

# Change rate variable names for easier handling 
mortality_2018 = mortality_2018.rename(columns={"Rate":"Rate2018", "State":"Code"})
mortality_2021 = mortality_2021.rename(columns={"Rate":"Rate2021"})

# Remove Alaska and Hawaii 
mortality_2018 = mortality_2018[mortality_2018.Code != "AK"]
mortality_2021 = mortality_2021[mortality_2021.State != "Alaska"]
mortality_2018 = mortality_2018[mortality_2018.Code != "HI"]
mortality_2021 = mortality_2021[mortality_2021.State != "Hawaii"]

# Merge the 4 data frames together so left with only desired information:
#  state code, region, and rates from both 2018 and 2021 
mortality_2021 = mortality_2021.merge(state_codes, on="State")
both_mortality = mortality_2021.merge(mortality_2018, on="Code")
both_mortality = both_mortality[["Code", "Rate2018", "Rate2021"]]
both_mortality = both_mortality.rename(columns={"Code":"State"})
both_mortality = both_mortality.merge(census_regions, on="State")
 

# For each of the four census regions, 
#   compute the mean state percentage difference in rates 
#   from 2018 to 2021 (Rate2018 - Rate2021)/Rate2018*100)
#   and the standard deviation and coefficient of variation (mean/std)

# add the difference variable 
both_mortality = both_mortality.assign(
    mean_diff = ((both_mortality.Rate2018 - both_mortality.Rate2021)/
                 (both_mortality.Rate2018)*100))

# group by regions to find mean, std, and CV for each region 
mean_series = both_mortality.groupby("Region")["mean_diff"].mean()
std_series = both_mortality.groupby("Region")["mean_diff"].std()
# CV is mean/STD so can use existing series to create a third 
cv_series = std_series/mean_series

# combine the 3 series into a summary df 
final_table = pd.DataFrame({"Mean Difference": mean_series,
                            "Standard Deviation": std_series,
                            "Coefficient of Variation":cv_series})

# show the final table 
print(final_table)












