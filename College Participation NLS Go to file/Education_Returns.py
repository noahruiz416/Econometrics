#loading in libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Desktop/ECN 421/college_participation/college_participation_categorical.csv")
additional_controls = pd.read_csv("Desktop/ECN 421/labor_hwa1/additional_controls/additional_controls_clean.csv")

frames = [df, additional_controls]
df = pd.concat(frames, axis=1)


df.drop('Unnamed: 0', axis=1, inplace = True)
additional_controls.drop('Unnamed: 0', axis = 1, inplace = True)


df['CVC_HIGHEST_DEGREE_EVER_XRND'].value_counts(ascending=True).plot.barh().set_title('Levels of Education')

mappings = {
    "High school diploma (Regular 12 year program)": 0,
    "Bachelor's degree (BA, BS)": 1,
    "GED": 0,
    "None": 0,
    "Associate/Junior college (AA)": 0,
    "Master's degree (MA, MS)": 1,
    "Professional degree (DDS, JD, MD)": 1,
    "PhD": 1
}

df['POST_SECONDARY_EDU'] = df['CVC_HIGHEST_DEGREE_EVER_XRND'].replace(mappings)

#prepping data for logistic model
#POST_SECONDARY_EDU = Biological_Secondary_Edu + HS_GPA + Supportive_Parents + Child_Care + Hard_Times + HH_NetWorth + Citizenship + Ethnicity
#variables to prep, Biological_Secondary_Edu, Arrest_History, ACT Scores, MAT Scores, ENG Scores, Citizenship

df.info()

trimmed_data = df[['ARREST_TOTNUM_XRND', 'INCARC_TOTMONTHS_XRND', 'KEY_SEX_1997', 'CV_CITIZENSHIP_1997', 'CV_HH_NET_WORTH_P_1997',
                    'CV_HGC_RES_DAD_1997','CV_HGC_RES_MOM_1997', 'KEY_RACE_ETHNICITY_1997',
                    'POST_SECONDARY_EDU',
                    'TRANS_CRD_GPA_OVERALL_HSTR', 'FP_ADHRISKI_1997', 'FP_ADPENVRI_1997', 'FP_ADENRCHI_1997', 'CV_INCOME_GROSS_YR_1997']]


trimmed_data.shape

trimmed_data.isna().sum()

trimmed_data_dropped = trimmed_data.dropna()

trimmed_data_dropped.info()

sns.distplot(trimmed_data['CV_HH_NET_WORTH_P_1997']).set_title('Family Net Worth')

trimmed_data['CV_HH_NET_WORTH_P_1997'].describe()

trimmed_data['GPA_NORM'] = trimmed_data['TRANS_CRD_GPA_OVERALL_HSTR'] * (1/100)

trimmed_data['GPA_NORM'].describe()

def filter(ar):
  return ar[np.isfinite(ar)]

filted_log_nw =  filter(np.log(trimmed_data['CV_HH_NET_WORTH_P_1997']))
standardize_nw = (trimmed_data['CV_HH_NET_WORTH_P_1997'] - trimmed_data['CV_HH_NET_WORTH_P_1997'].mean()) /(trimmed_data['CV_HH_NET_WORTH_P_1997'].std())

standardize_nw.hist()

#creating a variable for resiential parents college choice

sex_mappings = {
    "Male": 1,
    "Female": 0
}

citizen_mappings = {
    "Citizen, born in the U.S.": 1,
    "Unknown, not born in U.S.": 0,
    "Unknown, can't determine birthplace": 0,
}

university_mappings = {
    "12TH GRADE": 0,
    "4TH YEAR COLLEGE":1,
    "2ND YEAR COLLEGE":0,
    "1ST YEAR COLLEGE":0,
    "6TH YEAR COLLEGE":1,
    "11TH GRADE":0,
    "8TH YEAR COLLEGE OR MORE": 1,
    "10TH GRADE":0,
    "3RD YEAR COLLEGE":0,
    "9TH GRADE": 0,
    "5TH GRADE": 0,
    "4TH GRADE": 0,
    "7TH GRADE": 0,
    "3RD GRADE": 0,
    "2ND GRADE": 0,
    "1ST GRADE": 0,
    "6TH GRADE": 0,
    "5TH YEAR COLLEGE": 1,
    "7TH YEAR COLLEGE": 1,
    "8TH GRADE":0,
    "UNGRADED": 0
}


#cleaned variables, transformed
trimmed_data_dropped['KEY_SEX_1997'] = trimmed_data_dropped['KEY_SEX_1997'].replace(sex_mappings)
trimmed_data_dropped['CITZENSHIP'] = trimmed_data_dropped['CV_CITIZENSHIP_1997'].replace(citizen_mappings)
trimmed_data_dropped['RES_DAD_COLLEGE'] = trimmed_data_dropped['CV_HGC_RES_DAD_1997'].replace(university_mappings)
trimmed_data_dropped['RES_MOM_COLLEGE'] = trimmed_data_dropped['CV_HGC_RES_MOM_1997'].replace(university_mappings)

trimmed_data_dropped

#transforming more data now focused on education data

GPA_SCORES = []
for row in trimmed_data_dropped['TRANS_CRD_GPA_OVERALL_HSTR']:
    if row == -9 or row == -8 or row == -7 or row == -6:
        GPA_SCORES.append(-1)
    else:
        GPA_SCORES.append(row)



#trimmed_data_dropped['TRANSFORMED_GPA'] = GPA_SCORES
trimmed_data_dropped['TRANSFORMED_GPA'] = GPA_SCORES

trimmed_data_dropped['TRANSFORMED_GPA'] = trimmed_data_dropped['TRANSFORMED_GPA'] * (1/100)


#variables to be transformed into dummies
trimmed_data_dropped['CITIZENSHIP'] = trimmed_data_dropped['CITZENSHIP']
trimmed_data_dropped['NORM_NET_WORTH'] = (trimmed_data_dropped['CV_HH_NET_WORTH_P_1997'] - trimmed_data_dropped['CV_HH_NET_WORTH_P_1997'].mean()) / (trimmed_data_dropped['CV_HH_NET_WORTH_P_1997'].std())

X = trimmed_data_dropped[['NORM_NET_WORTH','RES_DAD_COLLEGE', 'RES_MOM_COLLEGE', 'TRANSFORMED_GPA','FP_ADHRISKI_1997', 'FP_ADENRCHI_1997']]

X_dummies = pd.get_dummies(X, drop_first = True)

y = trimmed_data_dropped['POST_SECONDARY_EDU']

X_dummies


import statsmodels.api as sm

#logistc model
log_reg = sm.Logit(y, X_dummies).fit(maxiter = 1000)
print(log_reg.summary())

print(log_reg.get_margeff(at ='overall').summary())

#saving regression ouputs to photos
plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(log_reg.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.tight_layout()
plt.savefig('Logistc_Regression_Results.png')

plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(log_reg.get_margeff(at ='overall').summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.tight_layout()
plt.savefig('Logistc_Regression_Results.png')

#logist_preds
ypred = log_reg.predict(X_dummies)
X_dummies_log = X_dummies
X_dummies_log['Preds'] = ypred
frames = [X_dummies_log, y]
X_dummies_log = pd.concat(frames, axis=1)
X_dummies_log

#linear probability model
X_int = sm.add_constant(X_dummies)
lin_reg = sm.OLS(y, X_int).fit()

print(lin_reg.summary())

#lin reg preds
ypred_lin = lin_reg.predict(X_int)
X_dummies_lin = X_int
X_dummies_lin['Preds'] = ypred_lin
frames = [X_dummies_lin, y]
X_dummies_lin = pd.concat(frames, axis=1)
X_dummies_lin

#probit model
#linear probability model
probit = sm.Probit(y, X_dummies).fit()

print(probit.summary())
