---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.7
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Retail Sales Analysis Jupyter Notebook

```{code-cell} ipython3
#All Models in this program test the validity of the model at predicting actiual values.  
# I have not yet added prediction/forecasting functionality.  I will do one week's work of prediction at a time.  


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import operator
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
```

```{code-cell} ipython3
def mape_vectorized_v2(a, b): 
    mask = a != 0
    return (np.fabs(a - b)/a)[mask].mean() 
```

```{code-cell} ipython3
#Creating the initial Data Frame from the potLog6 csv.  Data from 1/1/2020 to 3/31/2020

df = pd.read_csv('csv/PotLog.csv')


#creating the dictionary to hold the Errors of each method.  Will find minimum(best) value at the end
rmseDictionary = {}

mapeDictionary = {}
```

```{code-cell} ipython3
#Rearanging data into two new data frames aggregated by the sums of days
#historic data contains the months of jan and february
#test data is the month of march

allData = df.copy()
allData['Timestamp'] = pd.to_datetime(allData.date,format='%Y-%m-%d')
allData.index = allData.Timestamp
allData = allData.resample('D').sum()
allData = allData.drop(columns=['hour', 'week'])

historic = df[:720].copy()

historic['Timestamp'] = pd.to_datetime(historic.date,format='%Y-%m-%d')
historic.index = historic.Timestamp
historic = historic.resample('D').sum()
historic = historic.drop(columns=['hour', 'week'])

test = df[720:].copy()

test['Timestamp'] = pd.to_datetime(test.date,format='%Y-%m-%d')
test.index = test.Timestamp
test = test.resample('D').sum()
test = test.drop(columns=['hour', 'week'])



```

```{code-cell} ipython3
#Plotting the Historic and Test data on the same plane

historic.sales.plot(figsize=(15,8), title= 'Sales', fontsize=14)
test.sales.plot(figsize=(15,8), title= 'Sales', fontsize=14)

plt.show()
```

```{code-cell} ipython3
dd= np.asarray(allData.sales)
y_hat_avg = allData.copy()
y_hat_avg['naive'] = 0 
#print (y_hat_avg['sales'][3])
#print (len(y_hat_avg))

y_hat_avg['naive'][0] = allData.sales[0]
i = 1
for index, row in y_hat_avg.iterrows():
    if i < len(y_hat_avg):
        y_hat_avg['naive'][i] = allData.sales[i-1]
        #print(index)
        #sale = row.sales
        #print(sale)
        i +=1
    else:
        break


y_hat_avg.head(10)
```

```{code-cell} ipython3
# The easy or naive forcasting method.  It predicts values according to the value of the previous day 
#This needs to be redone.  It shuold not be a straight line but rather a scatter plot

#dd= np.asarray(allData.sales)
#y_hat_avg = test.copy()
#y_hat_avg['naive'] = dd[len(dd)-1]
plt.figure(figsize=(12,8))
#plt.plot(historic.index, historic['sales'], label='Historic Sales')
plt.plot(allData.index,allData['sales'], label='Actual')
plt.plot(y_hat_avg.index,y_hat_avg['naive'], label='Predicted')
plt.legend(loc='best')
plt.title("Naive Forecast")
plt.show()
    
rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg.naive))
rmseDictionary["Naive"] = rmse
print("The RMS for the Naive Method is equal to {}".format(rmse))

mape = mape_vectorized_v2(allData.sales, y_hat_avg.naive)
mapeDictionary['Naive'] = mape 

y_hat_avg.head(10)
```

```{code-cell} ipython3
#The Simple Average forcasting method forcasts according the overall average of sales

#y_hat_avg = test.copy()
y_hat_avg['avg_forecast'] = allData['sales'].mean()


plt.figure(figsize=(12,8))
plt.plot(historic['sales'], label='Historic')
plt.plot(test['sales'], label='Test')
plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')
plt.legend(loc='best')
plt.show()

rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg.avg_forecast))
rmseDictionary["Simple Average"] = rmse

print("The RMS for the Simple Average Method is equal to {}\n".format(rmse))

mape = mape_vectorized_v2(allData.sales, y_hat_avg.avg_forecast)
mapeDictionary['Simple_Average'] = mape 

y_hat_avg.tail()
```

```{code-cell} ipython3
#The moving average forcasting method forcasts according the average of a number of units.  In this case we use 7 days 
#or one week.  More testing should be done to discover the best number of days to use for average
#This should also shift by values.  Will revisit this 

#y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = allData['sales'].rolling(3).mean()
y_hat_avg['moving_avg_forecast'][0] = allData['sales'][0].copy()
y_hat_avg['moving_avg_forecast'][1] = allData['sales'][1].copy()
y_hat_avg['moving_avg_forecast'][2] = allData['sales'][2].copy()

plt.figure(figsize=(16,8))
#plt.plot(historic['sales'], label='Historic')
#plt.plot(test['sales'], label='Test')
plt.plot(allData['sales'], label='Actual Sales')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.show()
    
rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg.moving_avg_forecast))
rmseDictionary["Moving Average"] = rmse
print("The RMSE for the Moving Average Method is equal to {}\n".format(rmse))

mape = mape_vectorized_v2(allData.sales, y_hat_avg.moving_avg_forecast)
mapeDictionary['Moving Average'] = mape 

y_hat_avg.head()
```

```{code-cell} ipython3
model = SimpleExpSmoothing(np.asarray(allData['sales']))
fit1 = model.fit()
fit2 = model.fit(smoothing_level=0.2)
fit3 = model.fit(smoothing_level=0.5)
fit4 = model.fit(optimized=True)


y_hat_avg['Simple_Exponential_Smoothing_alpha=.3'] = fit1.fittedvalues
y_hat_avg['Simple_Exponential_Smoothing_alpha=.2'] = fit2.fittedvalues
y_hat_avg['Simple_Exponential_Smoothing_alpha=.5'] = fit3.fittedvalues
y_hat_avg['Simple_Exponential_Smoothing_alpha_Optimum'] = fit4.fittedvalues

y_hat_avg.head()
#print(fit1.fittedvalues)
```

```{code-cell} ipython3
#The Exponential Smoothing Forcasting  I know that i've implemented it correctly, but i do not understand how it works 
# in python.  Need to study 

#y_hat_avg = test.copy()
#y_hat_avg['SES'] = fit2.forecast(len(test))
plt.figure(figsize=(16,8))
plt.plot(allData['sales'], label='Actual Sales')
#plt.plot(test['sales'], label='Test')
plt.plot(y_hat_avg['Simple_Exponential_Smoothing_alpha=.3'], label='SES.3')
plt.plot(y_hat_avg['Simple_Exponential_Smoothing_alpha=.2'], label='SES.2')
plt.plot(y_hat_avg['Simple_Exponential_Smoothing_alpha=.5'], label='SES.5')
plt.plot(y_hat_avg['Simple_Exponential_Smoothing_alpha_Optimum'], label='SES_Optimum')

plt.legend(loc='best')
plt.show()
    
rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha=.3']))
rmseDictionary["Exponential_Smoothing.3"] = rmse

rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha=.2']))
rmseDictionary["Exponential_Smoothing.2"] = rmse

rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha=.5']))
rmseDictionary["Exponential_Smoothing.5"] = rmse

rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha_Optimum']))
rmseDictionary["Exponential_Smoothing_Optimum"] = rmse


mape = mape_vectorized_v2(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha=.3'])
mapeDictionary['Simple_Exponential_Smoothing.3'] = mape 

mape = mape_vectorized_v2(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha=.2'])
mapeDictionary['Simple_Exponential_Smoothing.2'] = mape 

mape = mape_vectorized_v2(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha=.5'])
mapeDictionary['Simple_Exponential_Smoothing.5'] = mape 

mape = mape_vectorized_v2(allData.sales, y_hat_avg['Simple_Exponential_Smoothing_alpha_Optimum'])
mapeDictionary['Simple_Exponential_Smoothing_Optimum'] = mape 


#y_hat_avg.head()
```

```{code-cell} ipython3
#Tests Data for trends, seasonality, etc to preprocess for Holt Winter

sm.tsa.seasonal_decompose(allData.sales).plot()
result = sm.tsa.stattools.adfuller(allData.sales)
plt.show()
```

```{code-cell} ipython3
#The Holt Winter method forcasts according to trend, season, and means.  The data under consideration does not have a
#trend.  


#y_hat_avg = test.copy()
model = ExponentialSmoothing(np.asarray(allData['sales']) ,seasonal_periods=7 ,trend=None, seasonal='add')
fit1 = model.fit(optimized = True)
fit2 = model.fit(smoothing_level=.5, smoothing_slope=None, smoothing_seasonal=.5)
fit3 = model.fit(smoothing_level=.3, smoothing_slope=None, smoothing_seasonal=.3)


y_hat_avg['Holt_Winter_Optimum'] = fit1.forecast(len(allData))
y_hat_avg['Holt_Winter_.5'] = fit2.forecast(len(allData))
y_hat_avg['Holt_Winter_.3'] = fit3.forecast(len(allData))

#y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))

plt.figure(figsize=(16,8))
plt.plot(allData['sales'], label='Actual Sales')

plt.plot(y_hat_avg['Holt_Winter_Optimum'], label='Holt Winter Optimized')
plt.plot(y_hat_avg['Holt_Winter_.5'], label='Holt Winter .5')
plt.plot(y_hat_avg['Holt_Winter_.3'], label='Holt Winter .3')
          
#plt.plot( historic['sales'], label='Historic')
#plt.plot(test['sales'], label='Test')
#plt.plot(y_hat_avg['Holt_Winter'], label='Holt_Winter')
plt.legend(loc='best')
plt.show()
   
    
    
rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg['Holt_Winter_Optimum']))
rmseDictionary["Holt_Winter_Optimum"] = rmse

rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg['Holt_Winter_.5']))
rmseDictionary["Holt_Winter_.5"] = rmse

rmse = sqrt(mean_squared_error(allData.sales, y_hat_avg['Holt_Winter_.3']))
rmseDictionary["Holt_Winter_.3"] = rmse
    
#rmse = sqrt(mean_squared_error(test.sales, y_hat_avg.Holt_Winter))

#rmseDictionary["Holt Winter"] = rmse

#print("The RMSE for the Holt Winter Model is equal to {}\n".format(rmse))

mape = mape_vectorized_v2(allData.sales, y_hat_avg.Holt_Winter_Optimum)
mapeDictionary['Holt_Winter_Optimum'] = mape 

mape = mape_vectorized_v2(allData.sales, y_hat_avg['Holt_Winter_.5'])
mapeDictionary['Holt_Winter_.5'] = mape 

mape = mape_vectorized_v2(allData.sales, y_hat_avg['Holt_Winter_.3'])
mapeDictionary['Holt_Winter_.3'] = mape 

y_hat_avg.head()
```

```{code-cell} ipython3
#the Sarina Model is another seasonal model. I don't know how it works exactly.  I need to review the math and the
#documentation.  I am getting a convergence error.  Will fix immediatly

y_hat_avg = test.copy()
fit1 = sm.tsa.statespace.SARIMAX(historic.sales, order=(2, 1, 4),seasonal_order=(0,1,1,7)).fit()
y_hat_avg['SARIMA'] = fit1.forecast(len(test.sales), dynamic=True)
plt.figure(figsize=(16,8))
plt.plot( historic['sales'], label='Historic')
plt.plot(test['sales'], label='Test')
plt.plot(y_hat_avg['SARIMA'], label='SARIMA')
plt.legend(loc='best')
plt.show()
    
rmse = sqrt(mean_squared_error(test.sales, y_hat_avg.SARIMA))
rmseDictionary["SARIMA"] = rmse

mape = mape_vectorized_v2(test.sales, y_hat_avg['SARIMA'])
mapeDictionary['SARIMA'] = mape 

#print("The RMSE for the SARIMA Model is equal to {}\n".format(rmse))
   
```

```{code-cell} ipython3
print(rmseDictionary)

mn = min(rmseDictionary.items(), key=operator.itemgetter(1))[0]
print("The Best Model is {}".format(mn))
```

```{code-cell} ipython3
print (mapeDictionary)

mn = min(mapeDictionary.items(), key=operator.itemgetter(1))[0]
print("The Best Model is {}".format(mn))
```

```{code-cell} ipython3

```
