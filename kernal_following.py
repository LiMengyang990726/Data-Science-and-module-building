import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
%matplotlib inline
import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns
# seaborn is built on top of matplotlib
color = sns.color_palette()
sns.set_style('darkgrid')
import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn #ignore annoying warning (from sklearn and seaborn)
pd.set_option("display.max_columns",100)

from scipy import stats
from scipy.stats import norm, skew #for some statistics


pd.set_option('display.float_format', lambda x: '{:.3f}'.format(x)) #Limiting floats output to 3 decimal points


from subprocess import check_output

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

print("The train data size before dropping Id feature is : {} ".format(train.shape))
print("The test data size before dropping Id feature is : {} ".format(test.shape))

#Save the 'Id' column
train_ID = train['Id']
test_ID = test['Id']

#Now drop the  'Id' colum since it's unnecessary for  the prediction process.
train.drop("Id", axis = 1, inplace = True)
test.drop("Id", axis = 1, inplace = True)

#check again the data size after dropping the 'Id' variable
print("\nThe train data size after dropping Id feature is : {} ".format(train.shape))
print("The test data size after dropping Id feature is : {} ".format(test.shape))

fig,ax = plt.subplots() # is useful if you want to change figure-level attributes
# or save the figure as an image file later
# e.g.fig.savefig('yourfilename.png'
ax.scatter(x = train['GrLivArea'], y = train['SalePrice'])
plt.ylabel('SalePrice', fontsize=13)
plt.xlabel('GrLivArea', fontsize=13)
plt.show()
#Deleting outliers, as they are huge area with low price, not possible
train = train.drop(train[(train['GrLivArea']>4000) & (train['SalePrice']<300000)].index)
fig,ax = plt.subplots()
ax.scatter(x = train['GrLivArea'],y = train['SalePrice'])
plt.ylabel('SalePrice',fontsize=13)
plt.xlabel('GrLivArea',fontsize=13)
plt.show()

sns.distplot(train['SalePrice'] , fit=norm);
# Get the fitted parameters used by the function
(mu, sigma) = norm.fit(train['SalePrice'])

print( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))
plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
            loc='best')
plt.ylabel('Frequency')
plt.title('SalePrice distribution')
# stats.probplot is a scipy plot
fig = plt.figure()

# Generates a probability plot of sample data against the quantiles of a specified theoretical distribution (the normal distribution by default)
# optionally calculates a best-fit line for the data and plots the results using Matplotlib or a given plot function
res = stats.probplot(train['SalePrice'], plot=plt)
plt.show()

# already done this: train["SalePrice"] = np.log1p(train["SalePrice"])
sns.distplot(train["SalePrice"],fit = norm)
(mu, sigma) = norm.fit(train['SalePrice'])
print( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))
#Now plot the distribution
plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
            loc='best')
plt.ylabel('Frequency')
plt.title('SalePrice distribution')

#Get also the QQ-plot
fig = plt.figure()
res = stats.probplot(train['SalePrice'], plot=plt)
plt.show()

# =====================================================================================
# Part of feature engineering
# =====================================================================================
train.shape[0]
test.shape[0]
ntrain = train.shape[0]
ntest = test.shape[0]
y_train = train.SalePrice.values
all_data = pd.concat((train, test)).reset_index(drop=True)
# what does this (drop=True) for???
# join the test and train together (rows double), the "SalePrice" from test are all nan
all_data.drop(['SalePrice'], axis=1, inplace=True)
# thus we drop all the SalePrice, as train has this column while test doesn't have this column
print("all_data size is : {}".format(all_data.shape))

# see the missing data ratio for each column
all_data_na = (all_data.isnull().sum() / len(all_data)) * 100
# all_data_na[all_data_na == 0].index means to drop all those columns that don't have missing values
all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)[:80]
missing_data = pd.DataFrame({'Missing Ratio' :all_data_na})
# why missing ratio will be automatically set to the column with all the floating value???
missing_data.head(20)


f, ax = plt.subplots(figsize=(15, 12))
plt.xticks(rotation='90') # to make the x labels vertical
sns.barplot(x=all_data_na.index, y=all_data_na)
plt.xlabel('Features', fontsize=15)
plt.ylabel('Percent of missing values', fontsize=15)
plt.title('Percent missing data by feature', fontsize=15)

corrmat = train.corr()
plt.subplots(figsize=(12,9))
sns.heatmap(corrmat, vmax=0.9, square=True)

#
# =====================================================================================
# Fill in the missing values according to ituition
# =====================================================================================
all_data["PoolQC"] = all_data["PoolQC"].fillna("None")
all_data["MiscFeature"] = all_data["MiscFeature"].fillna("None")
all_data["Alley"] = all_data["Alley"].fillna("None")
all_data["Fence"] = all_data["Fence"].fillna("None")
all_data["FireplaceQu"] = all_data["FireplaceQu"].fillna("None")
 # LotFrontage: Linear feet of street connected to property
 # intuitively, we can fill in the value from the median of it's neighbourhood's LotFrontage
all_data["LotFrontage"] = all_data.groupby("Neighborhood")["LotFrontage"].transform(
    lambda x: x.fillna(x.median()))
    # confused by .transform and .apply, refer here:
    # https://stackoverflow.com/questions/27517425/apply-vs-transform-on-a-group-object
Garage_ralated = ["GarageQual","GarageCond","GarageFinish","GarageYrBlt","GarageType"]
for col in Garage_ralated:
    all_data[col] = all_data[col].fillna("None")
all_data['GarageYrBlt'].replace('None', np.nan, inplace=True)

# as GarageArea and GarageCars all doesn't have nan values at the beginning,
# however, they are relevant features with GarageYrBlt/GarageType (whatever)
# no matter what they have in the beginning, we should change them back to 0

# use those relavant columns that have "NaN" to carry the columns that doesn't have "NaN"
# carry them to change to 0 for correponding columns
for col in ('GarageYrBlt', 'GarageArea', 'GarageCars'):
    all_data[col] = all_data[col].fillna(0)
for col in ('BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF','TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath'):
    all_data[col] = all_data[col].fillna(0)

all_data["MasVnrType"] = all_data["MasVnrType"].fillna("None")
all_data["MasVnrArea"] = all_data["MasVnrArea"].fillna(0)

for col in ("BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinType2"):
    all_data[col] = all_data[col].fillna("None")
for col in ("BsmtFinSF1","BsmtFinSF2","BsmtUnfSF","TotalBsmtSF",'BsmtFullBath', 'BsmtHalfBath'):
    all_data[col] = all_data[col].fillna(0)
for col in ('BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2'):
    all_data[col] = all_data[col].fillna('None')
all_data_na = (all_data.isnull().sum()/len(all_data))*100
all_data_na = all_data_na.drop(all_data_na[all_data_na==0].index).sort_values(ascending=False)
all_data_na
