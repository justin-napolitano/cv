Retail Sales Forecasting
==========================

Description
------------

* This project was completed with Jupyter Notebooks and Python.
* It will complete sales forecasting for any fungible retail item in a server.
* The most accurate model is confirmed and the results are recommended to the user.

Models Tested
-------------
* Simple Average
* Moving Average
* Exponential Smoothing
* Sarina
* Holt-Winter

How to Improve
------------------
* Add more models.


Links
------
* `GitHub <https://github.com/justin-napolitano/sales-forecasting>`_

Code (With Output)
-------------------

.. code-block:: python

    #salesforecasting.py



    #All Models in this program test the validity of the model at predicting actual values.  



    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt 
    import statsmodels.api as sm
    import operator
    from sklearn.metrics import mean_squared_error




    def mape_vectorized_v2(a, b): 
        mask = a != 0
        return (np.fabs(a - b)/a)[mask].mean() 




    #Creating the initial Data Frame from the potLog6 csv.  Data from 1/1/2020 to 3/31/2020

    df = pd.read_csv('/Users/jnapolitano/projects/CoxOil/potLog6.csv')

    #creating the dictionary to hold the Errors of each method.  Will find minimum(best) value at the end
    rmseDictionary = {}

    mapeDictionary = {}




    #Rearanging data into two new data frames aggregated by the sums of days
    #historic data contains the months of jan and february
    #test data is the month of march

    allData = df.copy()
    allData['Timestamp'] = pd.to_datetime(allData.date,format='%Y-%m-%d')
    allData.index = allData.Timestamp
    allData = allData.resample('D').sum()
    allData = allData.drop(columns=['hour', 'week'])





    #Plotting the Historic and Test data on the same plane

    historic.sales.plot(figsize=(15,8), title= 'Sales', fontsize=14)
    test.sales.plot(figsize=(15,8), title= 'Sales', fontsize=14)

    plt.show()





    dd= np.asarray(allData.sales)
    y_hat_avg = allData.copy()
    y_hat_avg['naive'] = 0 
    #print (y_hat_avg['sales'][3])
    #print (len(y_hat_avg))

    y_hat_avg['naive'][0] = allData.sales[0]
    i = 1
    for index, row in y_hat_avg.iterrows():
        if i < len(y_hat_avg):




    # The easy or naive forecasting method.  It predicts values according to the value of the previous day 
    #This needs to be redone.  It shuold not be a straight line but rather a scatter plot

    #dd= np.asarray(allData.sales)
    #y_hat_avg = test.copy()
    #y_hat_avg['naive'] = dd[len(dd)-1]
    plt.figure(figsize=(12,8))
    #plt.plot(historic.index, historic['sales'], label='Historic Sales')
    plt.plot(allData.index,allData['sales'], label='Actual')
    plt.plot(y_hat_avg.index,y_hat_avg['naive'], label='Predicted')






    #The Simple Average forcasting method forcasts according the overall average of sales

    #y_hat_avg = test.copy()
    y_hat_avg['avg_forecast'] = allData['sales'].mean()


    plt.figure(figsize=(12,8))
    plt.plot(historic['sales'], label='Historic')
    plt.plot(test['sales'], label='Test')
    plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')




    #The moving average forecasting method forecasts according the average of a number of units.  In this case we use 7 days 
    #or one week.  More testing should be done to discover the best number of days to use for average
    #This should also shift by values.  Will revisit this 

    #y_hat_avg = test.copy()
    y_hat_avg['moving_avg_forecast'] = allData['sales'].rolling(3).mean()
    y_hat_avg['moving_avg_forecast'][0] = allData['sales'][0].copy()
    y_hat_avg['moving_avg_forecast'][1] = allData['sales'][1].copy()

    model = SimpleExpSmoothing(np.asarray(allData['sales']))
    fit1 = model.fit()
    fit2 = model.fit(smoothing_level=0.2)
    fit3 = model.fit(smoothing_level=0.5)
    fit4 = model.fit(optimized=True)


    y_hat_avg['Simple_Exponential_Smoothing_alpha=.3'] = fit1.fittedvalues
    y_hat_avg['Simple_Exponential_Smoothing_alpha=.2'] = fit2.fittedvalues
    y_hat_avg['Simple_Exponential_Smoothing_alpha=.5'] = fit3.fittedvalues





    #The Exponential Smoothing Forecasting  I know that i've implemented it correctly, but i do not understand how it works 
    # in python.  Need to study 

    #y_hat_avg = test.copy()
    #y_hat_avg['SES'] = fit2.forecast(len(test))
    plt.figure(figsize=(16,8))
    plt.plot(allData['sales'], label='Actual Sales')
    #plt.plot(test['sales'], label='Test')
    plt.plot(y_hat_avg['Simple_Exponential_Smoothing_alpha=.3'], label='SES.3')
    plt.plot(y_hat_avg['Simple_Exponential_Smoothing_alpha=.2'], label='SES.2')






    #Tests Data for trends, seasonality, etc to preprocess for Holt Winter

    sm.tsa.seasonal_decompose(allData.sales).plot()
    result = sm.tsa.stattools.adfuller(allData.sales)
    plt.show()





    #The Holt Winter method forcasts according to trend, season, and means.  The data under consideration does not have a
    #trend.  


    #y_hat_avg = test.copy()
    model = ExponentialSmoothing(np.asarray(allData['sales']) ,seasonal_periods=7 ,trend=None, seasonal='add')
    fit1 = model.fit(optimized = True)
    fit2 = model.fit(smoothing_level=.5, smoothing_slope=None, smoothing_seasonal=.5)
    fit3 = model.fit(smoothing_level=.3, smoothing_slope=None, smoothing_seasonal=.3)






    #the Sarina Model is another seasonal model. I don't know how it works exactly.  I need to review the math and the
    #documentation.  I am getting a convergence error.  Will fix immediatly

    y_hat_avg = test.copy()
    fit1 = sm.tsa.statespace.SARIMAX(historic.sales, order=(2, 1, 4),seasonal_order=(0,1,1,7)).fit()
    y_hat_avg['SARIMA'] = fit1.forecast(len(test.sales), dynamic=True)
    plt.figure(figsize=(16,8))
    plt.plot( historic['sales'], label='Historic')
    plt.plot(test['sales'], label='Test')
    plt.plot(y_h
    /Users/jnapolitano/anaconda3/lib/python3.7/site-packages/statsmodels/base/model.py:512: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
    "Check mle_retvals", ConvergenceWarning)





    print(rmseDictionary)

    # Output
    mn = min(rmseDictionary.items(), key=operator.itemgetter(1))[0]
    print("The Best Model is {}".format(mn))
    
    #Output: {'Naive': 4.650416500311948, 'Simple Average': 3.864665029828413, 'Moving Average': 2.850786580399194, 'Exponential_Smoothing.3': 3.8600633870789793, 'Exponential_Smoothing.2': 3.890728721685838, 'Exponential_Smoothing.5': 4.038706174884183, 'Exponential_Smoothing_Optimum': 3.8600633870789793, 'Holt_Winter_Optimum': 3.725530824214966, 'Holt_Winter_.5': 4.1933419840885, 'Holt_Winter_.3': 4.007981452395329, 'SARIMA': 3.0552405606752404}





    print (mapeDictionary)

    mn = min(mapeDictionary.items(), key=operator.itemgetter(1))[0]
    print("The Best Model is {}".format(mn))

    #Output: {'Naive': 0.4248514297237634, 'Simple_Average': 0.7014871459995661, 'Moving Average': 0.25894232267050626, 'Simple_Exponential_Smoothing.3': 0.5959455591676276, 'Simple_Exponential_Smoothing.2': 0.4765666098796226, 'Simple_Exponential_Smoothing.5': 0.39056705630612926, 'Simple_Exponential_Smoothing_Optimum': 0.5959455591676276, 'Holt_Winter_Optimum': 0.7394870536032403, 'Holt_Winter_.5': 0.840375693885689, 'Holt_Winter_.3': 0.812017129147291, 'SARIMA': 0.26329028489286066}
