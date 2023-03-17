# Econometrics
Folder Containing all projects related to empirical economics, done for coursework or personal interest. Descriptions of each mini project can be found below!


# Current Projects (Last Updated: 3/17/23)

Currently I'm building off the logit model I developed for college partcipation project and instead taking a traditional mathematical modeling approach. This project is relatively new however, I will update this repo as needed. 

With this project We hope to develop a model that will allow us to analyze the effect of government subsidies on college enrollment, labor supply and wages.

## Summary Report for Labor Demand Estimation and College Participation Model (Pdf Version):

[ECN_421_HW_1-2.pdf](https://github.com/noahruiz416/Econometrics/files/10928629/ECN_421_HW_1-2.pdf)

## OEWS Labor Demand Estimation

In this repo I try to estimate labor demand curves based on Bureau of Labor Statistics Occupational Employment and Wage Statistics survey data from a May 2021 industry census report. The data set itself had a wide variety of potential variables, but for simplicity we chose to only focus on Hourly Median Wages and Total Employment Numbers. In addition we conditioned on both "Broad" and "Detailed" occupation levels, where a "Broad" occupation is a basket of similar jobs, and "Detailed" is a granular occupation level.

### Variable Descriptions

Hourly Median wages, is an estimate of the hourly median wage for a given worker in an occupation class. In addition the BLS defines wages as a wide range of potential payment types, including but not limited too: base rates, commissions, tips and production bonuses. More can be found here: https : //www.bls.gov/oes/oesques.htm. Total Employment, is an estimate of the total number of people employed in a given occupation. Besides that a large number of other variables exist within this survey, but besides the variables mentioned above and the conditioning levels, no other data was analyzed. A large amount of data cleaning was conducted, which can all be found in the python scripts.

### Findings

After cleaning each respective data set, we created two separate python data frames which we chose too work with. One of the data frames was conditioned on the "Detailed" occupation level and the other on the "Broad" occupation level. When we check the shape of each data set we find that the broad data set has a total of 433 observations and the detailed data set has a total of 753 observations. From here we plotted each variable of interest with a histogram too get an idea of the distribution of total employment and hourly median wages when we condition on the granularity of an an occupation class. We find that both have a non-normal right skewed distribution, regardless of the conditional. After plotting histograms we create multiple scatter plots to see if a negative linear relationship exists between total employment and median wages. We find that when plotting total employment and median hourly wages, a very slight negative relationship does exist between the two variables. Further when we control for outliers and take any variable 3 standard deviations above the mean out of each respective data set, the negative linear relationship between total employment and median hourly wages strengthens. Overall this exercise, showed that even under very loose assumptions and subpar aggregate survey data, the labor demand curve is downward sloping.

Repo Link: https://github.com/noahruiz416/Econometrics/tree/main/Labor%20Economics/Labor%20Demand%20OEWS


## Estimating effect of socioeconomic background on post secondary education choice

How does family background, educational achievement, and academic environment affect the chance of completing higher education? Utilizing cross section data from the NLSY97 Cohort, we estimate a college choice model that takes a set of important socioeconomic factors and tries to estimate their impact on post secondary education choice. We believe that individuals who come from higher income households, safer neighborhoods, strong academic backgrounds and who had positive parental influences, will have a stronger inclination towards post secondary education. In an ideal experiment, we would clone individuals to account for unobserved personality traits (e.g. grit, drive, IQ, social skills) and experimentally assign them to different families.

### Data Descriptions

Our data set was from the National Longitudinal Survey of Youth in 1997. The independent variables that we are using are listed below in the methodology section. In terms of pros, the data has a large number of observations and a lot of variables to utilize as controls. Sample selection was random. With cons, the data set purposefully over samples from Black and Hispanic youth. Due to cultural differences, our sample may not be completely representative of the entire United States. Another weakness of this data set is measurement error. This questionnaire was originally taken with paper and pencil and each interviewer had to go through hundreds of interview questions. Therefore there might be some issues with survey reporting error and data input error. Finally, there were a lot of missing values in the data set. Originally, we had a data set of 8,000 observations. After taking out the missing values, we only had around 1,500 observations.

### Methodology

Listed below is the regression equation that we wish to estimate with our data. With this model we hope to capture the impact of an individuals socioeconomic background to see if we can estimate how factors such as Family Household Net Worth, High School GPA’s and more effect a persons secondary college decision. For purpose of brevity we write out each parameter in shorthand form. The first parameter is HHNW or Household Net Worth, it simply measures the total household Net Worth (Assets, Liabilities, Etc) for a given persons household in 1997. In addition we standardized the variable for purposes of computation and to make comparisons between different levels of net worth easier. RFC and RMC are a binary variables that respectively measure whether or not the residential father or mother completed a university level education. FR is a family risk index score. The risk score was created by the NLS, with higher scores indicating a "high risk" family environment for a child. The index score considers factors such as neighborhood safety, child welfare and parental stability. Enriching Environment or EE captures how educationally enriching an individuals environment is, with factors such as technology, access to books and additional tutoring/teaching, considered. A higher EE score corresponds to a more enriching environment. Finally we measure GPA, which is simply the grade point average of an individual during high school years.

### Regression Results

Fitting the model to the data yielded interesting results. Since we are utilizing a logistic model the coefficient values are challenging to interpret and will depend on the levels of other values of the independent variables. Because of this we can instead estimate the average marginal effect, of each independent variable, which will give us an idea about how changing the value of a given independent variable effects the probability of an individual completing post secondary education. Detailed results of the regression equation coefficient estimates and average marginal effects can be found in the tables and screenshots below. After estimating the coefficient values for our theorized logistic regression model, we find that HHNW, RFC, RMC and GPA all have positive coefficient values. This indicates increasing levels of GPA and Household Net-Worth lead to a higher probability of completing post secondary education. In addition this shows that parental completion of higher education for both the residential father and mother leads to an increased probability of completing post secondary education. Interestingly we found that the risk index scores, had slightly negative coefficient values. This was contrary to our initial idea and could indicate potential issues with our model. Additionally the other values we controlled for in our model may have caused the slight negative coefficient value for both risk scores. Omitted variable bias is likely still present within this data set, as certain factors that can effect higher education choice, such as ability level, intelligence, drive and grit only have proxies such as GPA. Further selection bias is likely present as well due in large part to the dropping of null values, which narrowed our sample from 8984 observations to 1445.


Repo Link: https://github.com/noahruiz416/Econometrics/tree/main/College%20Participation%20NLS
