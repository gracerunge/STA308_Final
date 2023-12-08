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
The values are the same, rounding is different based on the IDE you are 
choosing to use this is Rstudio and Spyder.


| Region     | Mean (R)   | Mean (py) | SD (R)    | SD (py)    | CV (R)   | CV (py)     |
|------------|------------|-----------|-----------|------------|----------|-------------| 
| Midwest    | 35.7       | 35.722550 | 8.92      | 8.918304   | 0.250    | 0.249655    |
| Northeast  | 38.5       | 38.527446 | 12.4      | 12.432945  | 0.323    | 0.322704    | 
| South      | 24.9       | 24.863418 | 7.14      | 7.140688   | 0.287    | 0.287197    |
| West       | 34.9       | 34.877063 | 12.9      | 12.928896  | 0.371    | 0.370699    | 


## Explaination of CV 
Write a short paragraph that explains the coefficient of variation

Coefficient of variation is calculated as the standard deviation divided 
by the mean. This value is a measure of how dispersed data points are 
surrounding the mean (the ratio of SD to mean). The higher a CV value, the 
more dispersion there is around the mean and the data is more scattered, lower 
CV values are "better" as they mean that the data is a good fit around the mean.

## Compare/Contrast average and variation in percent differences 
Compare and contrast the average and variation of the percent differences 
in the mortality rates from 2018 to 2021 in the four census regions.

The south had the lowest percentage decrease in mortality rate with 24.9%, 
and the northeast had the largest percentage decrease of 38.5% from 2018 to 
2021. Generalizing quite a bit, I would assume that people in the northeast 
took wearing masks and social distancing when feeling ill more seriously than 
people in the south did post COVID. All 4 regions have a mean percent decrease 
of over 20% which is quite significant and shows that we all did learn from the 
experience of COVID to try and stop the spread of other diseases like the flu 
when one begins to feel sick regardless of region. The Midwest and the west had 
very similar mean differences of about 35%, however the West has the largest CV 
value meaning its data is not all close to the mean but there is more variation
occurring. The Midwest in contrast has the lowest CV value and thus the least 
amount of dispersion in data points around the mean. It is important to not only 
consider the mean percent differences when making comparisons between regions 
but also to consider the variation through the SD and the CV.


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

My favorite thing I learned in this course would have to be how to use 
github and version control when working on projects. I think it is a very important 
and powerful tool to be able to showcase my work and to ensure that important 
projects that I have done are in a safe location that cannot be lost if I (knock 
on wood) were to have any more troubles with my computer or my local server. I 
plan to utilize my github page to display bioinformatics systems and projects that 
I have worked hard on and it can help me professionally in the same manner that 
my linked in site or similar has. I also enjoyed learning about the topic of merging
data sets to make answering complex questions more manageable. If you do not have 
all the data you need in one place it is much harder to work with or answer specific 
questions you may have, so merging data sets in both R and python will be tools 
that I am sure I will use in the future. 










