import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
%matplotlib inline
# get data
data = pd.read_csv('data/train.csv')

# ================================================================================
# Get familiar with data
# ================================================================================

data.shape
pd.set_option("display.max_columns",100)
data_my = data[data.columns[54:81]]

data_my.head()

# check what kind of values that some columns have

data_my.TotRmsAbvGrd.unique()
data_my.Functional.unique()
data_my.Fireplaces.unique()
data_my.FireplaceQu.unique()
data_my.GarageFinish.unique()
data_my.GarageType.unique()
data_my.GarageQual.unique()
data_my.PavedDrive.unique()
# Check whether the value for Fireplaces and FireplaceQu is consistent


# ================================================================================
# Fireplaces analysis
# ================================================================================

zero_fireplaces = (data_my['Fireplaces'] == 0).sum()
zero_fireplaces
data_my['FireplaceQu'].isnull().sum()
# They are consistent

portion_fireplaces = data_my['Fireplaces'].value_counts()
portion_fireplaces.plot.pie(autopct='%.1f%%').set_aspect('equal')
# the percentage of having 0,1,2,3 Fireplaces

data_fireplaces_saleprice = data_my.groupby('Fireplaces')['SalePrice'].mean()
data_fireplaces_saleprice.plot.bar(x = 'saleprice',y = 'number of fireplaces')
# More Fireplaces, higher the price

data_fireplaces_qu = data_my[['FireplaceQu','SalePrice']].dropna()
data_fireplaces_qu_salesprice = data_fireplaces_qu.groupby('FireplaceQu')['SalePrice'].mean()
data_fireplaces_qu_salesprice.plot.box()
# consistent with ituition, how can I get the value for ech point?


# ================================================================================
# Garage analysis
# ================================================================================

data_my[['GarageType','GarageYrBlt','GarageFinish','GarageCars','GarageArea','GarageQual']].isnull().sum()
(data_my[['GarageCars','GarageArea']]==0).sum()
# the number for all the give garage parameters is consistent

have_garage = data_my[['GarageType','SalePrice']].dropna()
have_garage['SalePrice'].mean()
no_garage = data_my[data_my['GarageType'].isnull()]
no_garage['SalePrice'].mean()
# the avarage saleprice for with garage or without garage

data_my = data_my.assign(GarageYr = [2018] - data_my['GarageYrBlt'])
(data_my['GarageYr']>100).sum()
data_my['GarageYr'].max()
data_my = data_my.assign(Garage_year_cut = pd.cut(data_my['GarageYr'], [0, 20, 40,60,80,120]))
df1 = data_my[data_my.columns[4:10]]
df2 = data_my[data_my.columns[26:29]]
data_my_garage = df1.join(df2)
data_my_garage = data_my_garage.dropna()
# columns regarding Garage

data_garage_yr_price = data_my_garage.groupby('Garage_year_cut')['SalePrice'].mean()
ax = data_garage_yr_price.plot.bar()
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.1, i.get_height()-3,  \
            str(round((i.get_height()), 2)), fontsize=12, color='black')

# relationship between the year of the garage and the salesprice


# ================================================================================
# Porch analysis
# ================================================================================

data_my.rename(columns={'3SsnPorch':'SsnPorch'},inplace = True)
data_my[data_my['OpenPorchSF']!=0].shape
data_my[data_my['EnclosedPorch']!=0].shape
data_my[data_my['3SsnPorch']!=0].shape
data_my[data_my['ScreenPorch']!=0].shape
# how to check whether someone has both a 3SsnPorch and a ScreenPorch etc.

def porch_to_symbol(OpenPorchSF,EnclosedPorch,SsnPorch,ScreenPorch):
    if (OpenPorchSF != 0):
        return 'OpenPorch'
    if (EnclosedPorch != 0):
        return 'EnclosedPorch'
    if (SsnPorch != 0):
        return 'SsnPorch'
    if (ScreenPorch != 0):
        return 'ScreenPorch'
    return 'NoPorch'
# question
# data_my['PorchType'] = data_my['OpenPorchSF','EnclosedPorch','SsnPorch','ScreenPorch'].apply(lambda OpenPorchSF, EnclosedPorch, SsnPorch, ScreenPorch: porch_to_symbol(OpenPorchSF,EnclosedPorch,SsnPorch,ScreenPorch))
# I thus use an alternative way
OpenPorch_price = data_my.loc[(data_my[['OpenPorchSF']]!=0).any(1)]
OpenPorch_price = OpenPorch_price['SalePrice'].mean()
ClosePorch_price = data_my.loc[(data_my[['EnclosedPorch']]!=0).any(1)]
ClosePorch_price = ClosePorch_price['SalePrice'].mean()
SsnPorch_price = data_my.loc[(data_my[['SsnPorch']]!=0).any(1)]
SsnPorch_price = SsnPorch_price['SalePrice'].mean()
ScreenPorch_price = data_my.loc[(data_my[['ScreenPorch']]!=0).any(1)]
ScreenPorch_price = ScreenPorch_price['SalePrice'].mean()
PorchType_price = pd.DataFrame({'Type':['Open','Close','ThreeSeason','Screen'],'Avg_price':[OpenPorch_price,ClosePorch_price,SsnPorch_price,ScreenPorch_price]})
ax = PorchType_price.plot.bar(color = 'purple',legend = False)
ax.set_xlabel('Porch types')
ax.set_ylabel('Average saleprice')
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.1, i.get_height()-3,  \
            str(round((i.get_height()), 2)), fontsize=12, color='black')


# ================================================================================
# Pool analysis
# ================================================================================

def pool_quality(PoolQC):
    if (PoolQC == 'Ex'):
        return 3
    if (PoolQC == 'Gd'):
        return 2
    if (PoolQC == 'Fa'):
        return 1
    return 0

data_my = data_my.assign(PoolScore = data_my['PoolQC'].apply(lambda PoolQC: pool_quality(PoolQC)))
ax = (data_my.groupby('PoolScore')['SalePrice'].mean()).plot.bar(color = 'pink')
ax.set_xlabel('Pool score')
ax.set_ylabel('Average saleprice')
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.1, i.get_height()-3,  \
            str(round((i.get_height()), 2)), fontsize=12, color='black')
# Amazing, the pool with score 2's average saleprice is lower than the pool with score 1

with_pool = data_my.loc[(data_my[['PoolArea']]!=0).any(1)]
with_pool['SalePrice'].mean()
data_my[data_my['PoolArea']==0]['SalePrice'].mean()
# the average price difference with pool and without pool
data_my.head()

# ================================================================================
# Pool analysis
# ================================================================================
