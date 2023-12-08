# STA308_Final - Grace Runge 

## Purpose 

The two scripts in this project (.r and .py) are both to fulfill the requirements 
of the STA 308 Fall 2023 take home final exam. The remainder of this readme
file serves to answer the provided questions in the assignment description.

The goal of both scripts: 
  Given 4 different data sets, for four census regions, compute the mean  
  state percentage difference in the flu-pneumonia mortality 
  rates from 2018 to 2021 as well as the corresponding standard deviation 
  and coefficient of variation. 
    

## Calculated Values 
Show a table of the calculated values from your R and python programs.

I included 3 significant figures because that is what R provides, and though 
python outputs more significant figures, when you round you end up with the same 
values. I did not include 2 columns for R vs python since the values are the same.


| Region     | Mean Percent Difference | Standard Deviation  | Coefficient of Variation |
|------------|-------------------------|---------------------|--------------------------| 
| Midwest    | 35.7                    | 8.92                | 0.250                    |
| Northeast  | 38.5                    | 12.4                | 0.323                    | 
| South      | 24.9                    | 7.14                | 0.287                    |
| West       | 34.9                    | 12.9                | 0.371                    | 


## Explaination of CV 
Write a short paragraph that explains the coefficient of variation

insert here 

## Compare/Contrast average and variation in percent differences 
Compare and contrast the average and variation of the percent differences 
in the mortality rates from 2018 to 2021 in the four census regions.



## Mapping Table 
Construct a table that provides a mapping of the R functionality 
you used with the Python functionality you used for this assignment.

Note: df abbreviation used meaning either DataFrame in python or 
data.frame in R.


| Functionality      | in python                       | in R                        |
|--------------------|---------------------------------|-----------------------------|
| load in data       | pd.read_csv()                   | read_csv()                  | 
| rename column      | df.rename(column=dict{old:new}) | rename(new, old)            |
| merge data         | df1.merge(df2, on=column name)  | merge(df1, df2, by.x, by.y) |
| select df columns  | df[[list of column names]]      | select()                    |
| add a variable     | df.assign()                     | mutate()                    |
| summary stats      | df.mean(), df.std()             | summarise(mean(), sd())     |
| group data         | .groupby()                      | group_by()                  |
| remove data        | df.column !=                    | filter(data != )            | 


## Short Review of favorite topic from class 
Write a short review of your favorite topic and/or material 
from the course (what was it and why?). 












