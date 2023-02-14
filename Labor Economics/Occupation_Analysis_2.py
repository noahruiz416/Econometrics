#in this python script we will do the following
    # 1. Clean two different datasets one on detailed occupation stats the other on broad occupation stats
    # 2. Calculate basic statistics and create simple histogram plots to understand distributions of variables
    # 3. Load each dataset into a csv for tableu analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#setting some optional conditions
np.seterr(divide = 'ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sns.set_theme()


#loading in two seperate data sets one we will use to analyze detailed occupations the other we will only analyze
 #df0 = broad data
 #df = detailed data
df0 = pd.read_csv("/Users/n/Desktop/ECN 421/Occupation_Data.csv")
df = pd.read_csv("/Users/n/Desktop/ECN 421/Occupation_Data.csv")

#cleaning detailed data (getting rid of commas, replacing stars and hashes)
df.replace(',','', regex=True, inplace=True)
df.replace('\*','0', regex=True, inplace=True)
df.replace('#','0', regex=True, inplace=True)

#changing from string to float
df['H_MEDIAN'] = df['H_MEDIAN'].astype('float')
df['TOT_EMP'] = df['TOT_EMP'].astype('float')

#getting rid of everything but detailed occupation types and getting rid of rows with median hourly wages that == 0
df = df.drop(df[df.O_GROUP == 'broad'].index)
df = df.drop(df[df.O_GROUP == 'minor'].index)
df = df.drop(df[df.O_GROUP == 'major'].index)
df = df.drop(df[df.O_GROUP == 'total'].index)
df = df.drop(df[df.H_MEDIAN == 0].index)


#cleaning broad data (getting rid of commas, replacing stars and hashes)
df0.replace(',','', regex=True, inplace=True)
df0.replace('\*','0', regex=True, inplace=True)
df0.replace('#','0', regex=True, inplace=True)

#changing from string to float
df0['H_MEDIAN'] = df0['H_MEDIAN'].astype('float')
df0['TOT_EMP'] = df0['TOT_EMP'].astype('float')

#getting rid of everything but broad occupation types and getting rid of rows with median hourly wages that == 0
df0 = df0.drop(df0[df0.O_GROUP == 'detailed'].index)
df0 = df0.drop(df0[df0.O_GROUP == 'minor'].index)
df0 = df0.drop(df0[df0.O_GROUP == 'major'].index)
df0 = df0.drop(df0[df0.O_GROUP == 'total'].index)
df0 = df0.drop(df0[df0.H_MEDIAN == 0].index)


#checking that the data cleaning worked
df0.shape
df.shape

#normalizing the tot emp and median variables
df['H_MEDIAN_NORM'] = (df['H_MEDIAN'] - df['H_MEDIAN'].mean()) / (df['H_MEDIAN'].std())
df0['H_MEDIAN_NORM'] = (df0['H_MEDIAN'] - df0['H_MEDIAN'].mean()) / (df0['H_MEDIAN'].std())

df['TOT_EMP_NORM'] = (df['TOT_EMP'] - df['TOT_EMP'].mean()) / (df['TOT_EMP'].std())
df0['TOT_EMP_NORM'] = (df0['TOT_EMP'] - df0['TOT_EMP'].mean()) / (df0['TOT_EMP'].std())

df.shape
df0.shape

#histograms, normalized distributions are obviously non_normal
fig1 = df['H_MEDIAN'].hist().set_title('Detailed Median Hourly Wage Distribution').get_figure()
fig2 = df0['H_MEDIAN'].hist().set_title('Broad Median Hourly Wage Distribution').get_figure()

fig3 = df['TOT_EMP'].hist().set_title('Detailed Total Employment Distribution').get_figure()
fig4 = df0['TOT_EMP'].hist().set_title('Broad Total Employment Distribution').get_figure()

#descriptive stats
df['H_MEDIAN'].describe()

df['TOT_EMP'].describe()

#scatterplots, slight downward sloping relationship between employment and Hourly median wages
fig5 = sns.regplot(x = 'TOT_EMP', y = 'H_MEDIAN', data = df).set_title('Detailed Median Hourly Wages vs Total Employment (Millions)').get_figure()

#scatterplots, slight downward sloping relationship between employment and Hourly median wages
fig6 = sns.regplot(x = 'TOT_EMP', y = 'H_MEDIAN', data = df0).set_title('Broad Median Hourly Wages vs Total Employment (Millions)').get_figure()

#what if we create an interval of the wages that are most commonly occuring (ie: not outliers), we will assume that outliers are 3 std devs from the mean median wage
df['H_MEDIAN'].describe()
std = df['H_MEDIAN'].std()
upper_limit = df['H_MEDIAN'].mean() + std * 3



#lower limit does not make sense when dealing with wage data
new_df_detailed = (df[df['H_MEDIAN'] < upper_limit])
new_df_detailed.shape
df.shape

new_df_detailed['H_MEDIAN'].describe()
new_df_detailed['H_MEDIAN'].hist()
fig7 = sns.regplot(x = 'TOT_EMP', y = 'H_MEDIAN', data = new_df_detailed).set_title('Detailed Median Hourly Wages vs Total Employment (Millions)').get_figure()

#applying the same procedure on broad occupation class
df0['H_MEDIAN'].describe()
std = df0['H_MEDIAN'].std()
upper_limit = df0['H_MEDIAN'].mean() + std * 3



#lower limit does not make sense when dealing with wage data
new_df_broad = (df0[df0['H_MEDIAN'] < upper_limit])
new_df_broad.shape
df0.shape

new_df_broad['H_MEDIAN'].describe()
new_df_broad['H_MEDIAN'].hist()
fig8 = sns.regplot(x = 'TOT_EMP', y = 'H_MEDIAN', data = new_df_broad).set_title('Broad Median Hourly Wages vs Total Employment (Millions)').get_figure()

#finally we will load our 4 datasets to a csv file for future analysis (do not rerun unless you want the dataset, also switch file path)

df.to_csv('/Users/n/Desktop/ECN 421/Cleaned_Detailed_Occupation_Data.csv')
df0.to_csv('/Users/n/Desktop/ECN 421/Cleaned_Broad_Occupation_Data.csv')

new_df_detailed.to_csv('/Users/n/Desktop/ECN 421/Cleaned_Detailed_Occupation_Data_Clipped.csv')
new_df_broad.to_csv('/Users/n/Desktop/ECN 421/Cleaned_Broad_Occupation_Data_Clipped.csv')
