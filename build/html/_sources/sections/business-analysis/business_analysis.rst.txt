.. _businessanalysis:



#####################################
Business Analysis & Sales Forecasting
#####################################



.. topic:: Overview

    This Section introduces the background of the Kurdish-Turkish Conflict and describes the intent of the research. 


    :Date: |today|
    :Author: **Justin Napolitano**



.. contents:: 
    :depth: 3


***************
Graph Analysis
***************


Real Estate Analysis Engine
===========================

Description
----------------------

* A graph of relationships between real estate agents and locations that can be used to identify regional clusters of top performing agents.  
* I designed this solution for a marketing firm that needed to identify valuable agents in order to sell marketing services.

How to Improve
-------------------

* Transforming this graph into a POLE style would improve analytic capability.
* I would like to add objects such homes, condos, or any other fungible asset sold by Real Estate Agents and events such as meetings, calls, and sales to the graph.

Janus Stack
---------------
* JanusGraph Server 
* Casandra Database backend
* Elastic Search Indexing 

JanusGraph API
---------------

* To deploy the graph I used the JanusGraph API tool that I had written in Python.
* links here

Sample Data
--------------

Below are some samples of the data in various formats.


.. Danger:: 

    This is a dead link mr napolitano.

Links
---------


.. danger:: 

    These are dead links.  You better fix them mr napolitano.  



**********************************************************
Sales Forecasting
**********************************************************

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

Cigarette Sales Forecasting and Order Prediction
=================================================

Description
------------------------
* I wrote this program as a project to help a midsized retail company forecast their cigarette sales.
* It works by pulling data from a SQL server into dataframes.  
* I then calculate the weekly average sales volume for each cigarrette brand accross 58 retail locactions.
* If the total number of cartons sold of a brand per week is greater than the minimum inventory value for that brand than the program would produce an order output.
* The data was then exported to an excel spreadhseet that could be distributed to each store manager.

How to Improve
------------------------------
* I discovered that the true number of items inventory was often less than the predicted amount according to average sales data.
* When comparing averages to invoices some items appeared to be sold at volumes much greater than reported in sales reports.
* For this report to accurately model the flow of reatila commerce it must account for the average number of items "lost" in transport and those that "dissapear" from the shelves.


Links
-----
* `GitHub <https://github.com/justin-napolitano/Cigarette-Forecasting-and-Ordering>`_
  
Code
------


.. code-block:: python

    #cigarette_sales_order_form.py
    #Justin Napolitano
    #05/08/2020

    #Reads data from CSV into dataframe
    #Converts numbers into readable data
    #Exports requested data to Excel Spreadsheet
    #If a product requires ordering it will appear on the spreadsheet with the barcode

    import pandas as pd 
    import numpy as np
    import os

    #Setting Cwd
    cwd = (os.path.dirname(os.path.realpath(__file__)))

    #Reading Data in dataframe
    #Manipulating dataframe to prep for analysis

    pd.set_option('display.max_rows', None)
    df = pd.read_csv(cwd + '/CigSales.csv')
    df['timestamp'] = pd.to_datetime(df.Date)
    df.index = df.timestamp
    df['Total Cartons Sold'] = df['Quantity Sold'] * df['Sell Unit Quantity']
    df['week number'] = df.timestamp.dt.week

    #Creating a second data frame with the following indexes
    df2 = df.set_index(['week number','Store','Cigarette Name','Cigarette UPC', 'Item Number', 'Sell Unit Quantity'])
    df2 = df2.groupby(["week number", 'Store', 'Cigarette Name', "Cigarette UPC","Item Number", "Sell Unit Quantity"]).sum()

    #df3 = df2.groupby(["week number", "Cigarette Name","Cigarette UPC","Item Number", "Store"]).sum()

    df2["Total Cartons Sold"] = df2["Total Cartons Sold"] /10

    #Joining a weekly average dataframe to the main dataframe
    weekly_average = pd.DataFrame()
    weekly_average["Average Cartons Sold Weekly"] = df2["Total Cartons Sold"].groupby('Cigarette Name').mean()
    df2 = df2.join(weekly_average, on="Cigarette Name")
    df2 = df2.sort_values(by=['week number'], ascending =False)


    #Adding the Order collumn to frame
    df2["Order"] = None



    #Ccomparing average to total carton sales
    #df2['Order'] = np.where((df2['Average Cartons Sold Weekly'] >= df2['Total Cartons Sold'] )
    #                    , True, False)

    df2['Order'] = np.where((df2['Average Cartons Sold Weekly'] <= df2['Total Cartons Sold']) & (df2["Total Cartons Sold"] >=1)
                        , True, False)

    #df2['Order'] = np.where(df2['Average Cartons Sold Weekly'] >= df2['Total Cartons Sold'] ) #and np.where(df2["Total Cartons Sold"]>=1)                  

    #Creating DataFrame to display.  Only one week of data at a time
    x = df2.index[0][0]
    for i in range (len(df2.index)) :
        if df2.index[i][0] == x:
            max_i = i 


    df3 = df2[:max_i + 1]
    df3 = df3.sort_values(by=['Cigarette Name'], ascending =True)

    #exporting to excel
    df3.to_csv(cwd + "/order_form.csv")
    df2.to_csv(cwd + "/all_data.csv")

****************
Sales Reporting
****************

Sales Reporting CLI Program
============================

Description
--------------
* A CLI tool written in python that is designed to imitate dos-ibm systems.
* The program stores common reports that can be selected via a decision tree.
* The program was written as a proof of concept that the management team could use a familiar interface to replace multiple sql specialists that simply wrote stored proceudres. 

How to Improve
------------------
* Rewrite into a functional paradigm.
* Rewrite into multiple services.
* Ensure the scope of the project is understood as best as possible before writing any code.
* Store sql scripts external to the program itself.
* Use YAML to manage jobs and eliminate the user driven configuration interface.

Links
--------------

* `GitHub <https://github.com/justin-napolitano/sales-reporting-tool>`_

Code
-----------
  

.. code-block:: python

    #test_report_tool-2.6.py
    #Justin Napoliano 
    #06/13/2020
    #Developed for ******

    #Universal imports 
    import platform
    import os
    import pyodbc 
    import pandas as pd
    from pandas import ExcelWriter
    import logging
    import numpy as np
    import csv
    import datetime


    #This class creates the sales report.  Others classes can be added
    #later to build other types of reports.
    class sales_report():
        """
        A class that creates a sales report object.
        initial_parameteres will contain one initial parameters dataframe for each of the product, organization, and calendar tables
        transaction_datframe will contain the component strings to query the sql server, the final query, and the transaction dataframe
        """
        def __init__(self):
            logging.info('Initiating Sales Report Object')
            self.inital_parameters = get_initial_parameters()
            self.transaction_dataframe = create_transaction_dataframe(self.inital_parameters)
            self.custom_dataframe = create_custom_dataframe(self.transaction_dataframe.isf_table)
    #The Selection Levels Class can be used with any report.  IT is 
    #dynamically created.  It will build tables with user selected levels
    #to create custom reports from
    class create_custom_dataframe():

        """
        A class that modifies the dataframe by grouping and adding useful columns.

        """

        def __init__(self, transaction_dataframe):
            #a function asking the user what they would like to include
            #a function that makes all of that happen.  
            #self.transaction_dataframe = transaction_dataframe
            group_by_selection = self.select_group_by(transaction_dataframe)
            self.modified_transaction_table = self.select_transaction_data(group_by_selection, transaction_dataframe) 
            #self.modified_transaction_table = self.group_transaction_table(group_by_selection, transaction_dataframe) 
            #self.modified_transaction_table = self.modify_transaction_table(transaction_dataframe)

        def select_transaction_data(self,group_by_selection,transaction_dataframe):
            
            if group_by_selection[0] == 0 :##State
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe  = modified_dataframe[['GPS_State',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe  = modified_dataframe .groupby(['GPS_State']).agg(np.sum)
            
                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']

            elif group_by_selection[0] == 1: ##PB 
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc']).agg(np.sum)
                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']
            
            elif group_by_selection[0] == 2: ##Cig 
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc']).agg(np.sum)
                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']
            
            elif group_by_selection[0] == 3:  #Supervisor
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc']).agg(np.sum)

                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']

            elif group_by_selection[0] == 4 :##CITY
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City']).agg(np.sum)

                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']

        
            elif group_by_selection[0] == 5: ##Store
                
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc',
                'Sub_Category_ID',
                'Sub_Category_Desc',
                'Item_ID',
                'ENT_Item_Number'
                'Item_Desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude']).agg(np.sum)

                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']

            elif group_by_selection[0] == 6: #Department
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc']).agg(np.sum)

                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']

            elif group_by_selection[0] == 7: #Category
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = transaction_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc']).agg(np.sum)

                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']

            elif group_by_selection[0] == 8: #Sub_Category
                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc',
                'Sub_Category_ID',
                'Sub_Category_Desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]

                """
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc',
                'Sub_Category_ID',
                'Sub_Category_Desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]
                """
                modified_dataframe['Sub_Category_Cost'] = modified_dataframe.groupby(['Site_id','Sub_Category_ID']).Extended_Cost.transform(np.sum)
                modified_dataframe['Sub_Category_Sales'] = modified_dataframe.groupby(['Site_id','Sub_Category_ID']).Extended_Sales.transform(np.sum)
                modified_dataframe['Sub_Category_Profit'] = modified_dataframe['Sub_Category_Sales'] - modified_dataframe['Sub_Category_Cost']
                modified_dataframe['Sub_Category_Overall_Profit'] = modified_dataframe.groupby('Sub_Category_ID').Sub_Category_Profit.transform(np.sum)
                #modified_dataframe['Sub_Category_Percent_Profit'] = (modified_dataframe['Sub_Category_Profit'] / #modified_dataframe['Sub_Category_Overall_Profit']) * 100
                modified_dataframe['Sub_Category_Overall_Average_Sales'] = modified_dataframe.groupby('Sub_Category_ID').Sub_Category_Sales.transform(np.mean)
                modified_dataframe['Sub_Category_Difference_From_Mean'] = modified_dataframe['Sub_Category_Sales'] - modified_dataframe['Sub_Category_Overall_Average_Sales']
                

                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc',
                'Sub_Category_ID',
                'Sub_Category_Desc',
                'Sub_Category_Cost',
                'Sub_Category_Sales',
                'Sub_Category_Profit',
                'Sub_Category_Overall_Profit',
                'Sub_Category_Overall_Average_Sales',
                'Sub_Category_Difference_From_Mean']).agg(np.sum)

            
            elif group_by_selection[0] == 9: #item_number

                modified_dataframe = transaction_dataframe.copy()
                modified_dataframe = modified_dataframe[['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc',
                'Sub_Category_ID',
                'Sub_Category_Desc',
                'Item_ID',
                'Ent_Item_Number',
                'Item_Desc',
                'Qty_Sold',
                'Extended_Cost',
                'Extended_Sales']]

                modified_dataframe['Item_Overall_Cost'] = modified_dataframe.groupby('Item_ID').Extended_Cost.transform(np.sum)
                modified_dataframe['Item_Overall_Sales'] = modified_dataframe.groupby('Item_ID').Extended_Sales.transform(np.sum)
                modified_dataframe['Profit'] = modified_dataframe['Extended_Sales'] - modified_dataframe['Extended_Cost']
                modified_dataframe['Item_Overall_Profit'] = modified_dataframe.groupby('Item_ID').Profit.transform(np.sum)
                modified_dataframe['Percent_Profit'] = (modified_dataframe['Profit'] / modified_dataframe['Item_Overall_Profit']) * 100
            
                modified_dataframe = modified_dataframe.groupby(['GPS_State',
                'GPS_City',
                'Pizza_Brand_desc',
                'PB_Cigs_Zone_desc',
                'Business_Entity_id',
                'Business_Entity_desc',
                'T_Supervisor_desc',
                'Site_id',
                'Site_desc',
                'GPS_Zip',
                'GPS_Longitude', 
                'GPS_Latitude',
                'Department_ID',
                'Department_Desc',
                'Category_ID',
                'Category_Desc',
                'Sub_Category_ID',
                'Sub_Category_Desc',
                'Item_ID',
                'Ent_Item_Number',
                'Item_Desc',
                'Extended_Cost',
                "Extended_Sales",
                'Item_Overall_Cost',
                'Item_Overall_Sales',
                'Profit',
                'Item_Overall_Profit',
                'Percent_Profit']).agg(np.sum)
        

            return modified_dataframe
                
        def select_group_by(self,transaction_datframe):
            logging.info('User is selecting report')
            available_reports_dict = {0 :"State", 
            1 :"Pizza Brand", 
            2: "Cig Zone", 
            3: 'Supervisor',
            4: 'City',
            5:'Store',
            6:'Department', 
            7: 'Category', 
            8: 'Sub_category',
            9: 'Item Number'}
            available_reports_list = []
            report_selection = True

            for key in available_reports_dict:
                available_reports_list.append(key)    

                while report_selection:  
                    print("\n")
                    #print(available_reports_list)
                    print("Group by: \n")
                    for key,value in available_reports_dict.items():
                        print(key,value)
                        print("\n")
                    print("-----------------------------------------------------------------------------")
                    report_selection = input("User input: ")

                    if report_selection == 'q' or report_selection == 'quit':
                        return False
                    else:
                        try: 
                            report_selection = int(report_selection)
                            logging.debug('User Selected {}'.format(available_reports_dict[int(report_selection)]))
                            return (report_selection, available_reports_dict[int(report_selection)])
                        except ValueError:
                            print('The entry is not an integer.\n')
                            print("Enter <q>uit to quit or try again")
                            print("-----------------------------------------------------------------------------")  
                            logging.error('Value Error')
            


    class create_transaction_dataframe():
        """
        A class that will create a dataframe object of transactions as defined by the get_initial_parameters dataframe objects

        """
        def __init__(self,initial_parameters):
            logging.info('Initiating the transaction dataframe')
            self.organization_table_query = self.create_organization_table_query(initial_parameters.organization_table_lookup)
            self.product_table_query = self.create_product_table_query(initial_parameters.product_table_lookup)
            self.calendar_table_query = self.create_calendar_table_query(initial_parameters.calendar_table_lookup, initial_parameters.sql_connection.connection)
            self.query = self.create_isf_table_query()
            self.isf_table = self.create_isf_table_dataframe(self.query, initial_parameters.sql_connection.connection)
            

        def create_organization_table_query(self,organization_table_lookup):
            logging.info('Creating organization table query')
            select_list: list = organization_table_lookup['level_str'].to_list()
            select_list_str = ['O.' + item for item in select_list]
            select_list_str = str(select_list_str)
            select_list_str = select_list_str.replace("'", "")
            select_list_str = select_list_str[1:-1] 
            condition = '[{}] IN ({})'.format(organization_table_lookup['level_str'][0], str(organization_table_lookup['sub_levels'][0])[1:-1])
            for i in range(1,len(organization_table_lookup))  :
                if organization_table_lookup.at[i, 'can_select']  == True:
                    addition = ' AND [{}] IN ({})'.format(organization_table_lookup.at[i, 'level_str'], str(organization_table_lookup.at[i,'sub_levels'])[1:-1])
                    condition = condition + addition 
            select_condition = (select_list_str,condition)
            logging.debug('Select condition for organization table is {}'.format(select_condition))
            return(select_condition)


        def create_product_table_query(self,product_table_lookup):
            logging.info('creating product table query')
            select_list: list = product_table_lookup['level_str'].to_list()
            select_list_str = ['P.' + item for item in select_list]
            select_list_str = str(select_list_str)
            select_list_str = select_list_str.replace("'", "")
            select_list_str = select_list_str[1:-1] 
            condition = ''
            for i in range(len(product_table_lookup))  :
                if product_table_lookup.at[i, 'can_select']  == True:
                    addition = ' AND [{}] IN ({})'.format(product_table_lookup.at[i, 'level_str'], str(product_table_lookup.at[i,'sub_levels'])[1:-1])
                    condition = condition + addition 
            select_condition = (select_list_str,condition)
            logging.debug('Select condition for product table is {}'.format(select_condition))
            return(select_condition)


        def create_calendar_table_query(self,calendar_table_lookup, sql_connection):
            logging.info('creating calendar table query')
            column_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_NAME = 'Calendar' "
            level_str_list = pd.read_sql_query(column_query, sql_connection)
            level_str_list = level_str_list['COLUMN_NAME'].to_list()
            level_str_list = ['C.' + item for item in level_str_list]
            level_str_list = str(level_str_list)
            level_str_list = level_str_list.replace("'", "")
            level_str_list = level_str_list[1:-1] 
            row = calendar_table_lookup[calendar_table_lookup['user_selected'] == True]
            start_date = row.date_range[row.index[0]][0]
            end_date = row.date_range[row.index[0]][1]
            condition = 'AND C.Day BETWEEN {} AND {}'.format(start_date, end_date)
            select_condition = (level_str_list, condition)
            logging.debug('Select condition for calendar table is {}'.format(select_condition))
            return select_condition
            

        def create_isf_table_query(self):
            logging.info('creating the isf table')
            isf_table_select = ('ISF.Qty_Sold, ISF.Extended_Cost,ISF. Extended_Sales')
            #print(self.organization_table_query[0])
            select_statement: str = 'SELECT {}, {}, {}, {}'.format(self.calendar_table_query[0],self.organization_table_query[0], self.product_table_query[0], isf_table_select)
            from_statement: str = ' FROM Item_Sales_Fact AS ISF INNER JOIN Calendar AS C ON ISF.Calendar_key = C.calendar_key INNER JOIN Organization AS O ON ISF.Organization_key = O.organization_key INNER JOIN Product AS P ON ISF.Product_Key = P.Product_Key' 
            conditions: str = ' WHERE {} {} {}'.format(self.organization_table_query[1], self.product_table_query[1], self.calendar_table_query[1])
            query: str = select_statement + from_statement + conditions
            logging.debug('query for isf table is {}'.format(query))
            return query

        def create_isf_table_dataframe(self,query,sql_connection):    
            #print(query)
            print('********************************************************')
            print('Creating your report.  This could take a little while.\n')
            print('********************************************************')
            isf_table_df = pd.read_sql_query(query, sql_connection)
            #print(query)
            #print(isf_table_df)
            return isf_table_df


    class get_initial_parameters():
        """
        A class that gets the initial parameters from the user
        to use in constructing a dataframe of transactions
        """
        #initiates the lookup tables with user selected values for each table from the isf query
        def __init__(self):
            """
            initiates all of the lookup tables that will later be used to construct a query 
            to create a large dataframe of transactions
            """
            logging.info('Inititating sales_report.initial_parameters')
            
            self.sql_connection = sql_connection()
            self.calendar_table_lookup = self.create_calendar_table_lookup()
            self.organization_table_lookup = self.create_organization_table_lookup()
            self.product_table_lookup = self.create_product_table_lookup()
            
            logging.info('Initated sales_report.inital_parameters')
    
        
        #Creates the connection object to use for all queries in the program 
        #NOt in use in  current iteration. The sql_connection class is called instead
        def connect(self):
            server = 'Your Server' 
            database = 'Your Database' 
            username = 'Your Username' 
            password = 'Your Password' 
            return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    
        

        def create_organization_table_lookup(self):
            logging.info('Creating organization table lookup')
            level_str = pd.Series(['Location_ID', 'Organization_Key', 'Location_Desc', 'Last_Tank_Reading_Date', 'First_Transaction_Date', 'Closing_Date', 'GPS_Latitude','GPS_Longitude', 'GPS_Address1','GPS_State','GPS_City','GPS_Zip', 'Corp_Site', 'Time_Zone_ID', 'Site_ID_Formatted', 'Business_Entity_desc', 'Business_Entity_id', 'Corporate_desc','Corporate_id', 'Supervisor_desc', 'Supervisor_id', 'Site_desc', 'Site_id', 'T_Supervisor_desc', 'T_Supervisor_id', 'State_desc', 'State_id', 'PB_Cigs_Zone_desc', 'PB_Cigs_Zone_id', 'Pizza_Brand_desc', 'Pizza_Brand_id', 'Coke_Union_City_desc', 'Coke_Union_City_id' ])
            select_order = pd.Series([0,0,0,0,0,0,0,0,0,4,3,0,0,0,0,0,2,0,0,0,0,0,1,5,0,0,0,0,6,0,7,0,0])
            table_num = pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            table_str = pd.Series(['Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization','Organization'])
            can_select = pd.Series([False, False, False, False, False , False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, True, False, True, False, False])
            #user_selected = pd.Series([False, False, False, False, False , False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
            sub_levels = pd.Series([[],[],[],[],[], [], [] , [] , [] , [], [] , [], [] ,[] , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] , [] ,[]])
            sub_level_select = pd.Series([None, None, None, None, None, None, None, None, None,'[GPS_State]','[GPS_City], [GPS_State]', None, None, None, None, None, '[Business_Entity_id], [Business_Entity_desc]', None, None, None, None, None, '[Site_id], [T_Supervisor_desc], [Business_Entity_desc], [GPS_City], [GPS_State]' , '[T_Supervisor_desc]', None, None, None, None, '[PB_Cigs_Zone_id], [PB_Cigs_Zone_desc]', None, '[Pizza_Brand_id], [Pizza_Brand_desc]' , None, None])   
            organization_table_dict = {
                'level_str' : level_str,
                'select_order' : select_order, #hierarchy value in descending order.  #False means that the level is paired with another level.  
                'table_num':table_num,
                'table_str':table_str, 
                'can_select': can_select,
                #'user_selected': user_selected,
                'sub_levels': sub_levels,
                'sub_level_select' : sub_level_select
            }
        
            organization_table_lookup_df = pd.DataFrame(organization_table_dict)
            organization_table_lookup_df.sort_values(by='select_order', ascending=False, inplace=True)
            organization_table_lookup_df.reset_index(inplace=True, drop = 'index')

            self.select_sub_levels(organization_table_lookup_df)  #passes the updated table to the selecte_sub_levels_function.  Allows users to pick the specific states, citieds, etc they want to include in the reports
            logging.info('returned oranization table lookup')
            return organization_table_lookup_df


        def create_product_table_lookup(self):
            logging.info('creating product table lookup')
            level_str = pd.Series(['Product_Key', 'UPC_Sell_Unit_Desc', 'UPC', 'Sell_Unit_Desc', 'Sell_Unit_Qty', 'Item_ID', 'Item_Desc', 'Sub_Category_ID', 'Sub_Category_Desc', 'Category_ID', 'Category_Desc', 'Department_ID','Department_Desc', 'Size_Desc', 'Item_Type', 'Create_Date', 'Ent_Item_Number', 'UPC_Discontinue_Date', 'Scan_Modifier', 'IsPurchasable', 'Purchase_Discontinue_Date', 'IsSellable', 'Sales_Discontinue_Date', 'Audit_Flag'])
            select_order = pd.Series([0,0,0,0,0,1,0,2,0,3,0,4,0,0,0,0,0,0,0,0,0,0])
            table_num = pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0])
            table_str = pd.Series(['Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product','Product'])
            can_select = pd.Series([False, False, False, False, False, True, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False])
            user_selected = pd.Series([False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
            sub_levels = pd.Series([[] , [], [] ,[] ,[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] , [] ,[]])
            sub_level_select = pd.Series([None, None, None, None,None,  '[Item_ID], [Item_Desc], [Sub_Category_ID], [Sub_Category_Desc], [Category_ID], [Category_Desc]', None, '[Sub_Category_ID], [Sub_Category_Desc], [Category_ID], [Category_Desc], [Department_ID], [Department_Desc]', None, '[Category_ID], [Category_Desc], [Department_ID], [Department_Desc]', None, '[Department_ID], [Department_Desc]', None, None , None, None, None, None, None, None, None, None , None, None])   
            product_table_dict = {
                'level_str' : level_str,
                'select_order' : select_order, #hierarchy value in descending order.  #False means that the level is paired with another level.  
                'table_num':table_num,
                'table_str':table_str, 
                'can_select': can_select,
                'user_selected': user_selected,
                'sub_levels': sub_levels,
                'sub_level_select' : sub_level_select
            }

            product_table_df = pd.DataFrame(product_table_dict)
            product_table_df.sort_values(by='select_order', ascending=False, inplace=True)
            product_table_df.reset_index(inplace=True, drop = 'index')
            self.select_sub_levels(product_table_df)  #passes the updated table to the selecte_sub_levels_function.  Allows users to pick the specific states, citieds, etc they want to include in the reports
            logging.info('returned product table lookup')
            return product_table_df


        def create_calendar_table_lookup(self):
            logging.info('creating calendar table lookup')
            prompt = pd.Series(
                [
                    'Today'
                    ,'Yesterday'
                    ,'Date_Range'
                    , 'Select_Date'
                    , 'Last N Days'
                    , 'Last N Weeks'
                    , 'Last N Months'
                    , 'Month_To_Date'
                ]
            )
        
            calendar_lookup_table_df = pd.DataFrame()
            calendar_lookup_table_df['prompt'] =  prompt
            calendar_lookup_table_df['user_selected'] = self.select_date_range(calendar_lookup_table_df)
            calendar_lookup_table_df['user_input'] = self.input_date_range(calendar_lookup_table_df)
            calendar_lookup_table_df['date_range'] = self.sql_date_range(calendar_lookup_table_df)
        
            #print(calendar_lookup_table_df)
            logging.info('Returned calendar table lookup')
            return calendar_lookup_table_df

    
        def select_date_range(self, calendar_lookup_table_df):
            logging.info('User Selecting desired date range')
            user_selected = pd.Series(
                [
                    False
                    ,False
                    ,False
                    ,False
                    ,False
                    ,False 
                    ,False
                    ,False
                ]
            )

            user_selection_int: int = None
            #prompt = calendar_lookup_table_df['prompt']
            #print(prompt)
            
            while calendar_lookup_table_df.prompt.any():
                print(calendar_lookup_table_df.prompt)
                print('\n')
                print("Current Selection: \n")
                print("Enter the integer associated to the Date Range* value you want to add to the report")
                print("-----------------------------------------------------------------------------")
                user_selection = input("User Input: \n").lower()
                #print(user_selection)
                #D finishes the loop and returns the list
                    #current_table_row['level_str'] = selected_values_lst 
                #a fills the list with all available values.  #d will do the same if the user did not select any
                if user_selection == '': 
                    logging.info('User entered enter')
                    if user_selection_int == None:
                        print("You did not select a data range")
                        logging.info('user did not select a date range')
                        continue
                    else:
                        print("-----------------------------------------------------------------------------")
                        user_selected[user_selection] = True
                        return user_selected
                    
                elif user_selection == 'q' or user_selection =='quit':
                    return user_selected
            
                #elif current_table_row["user_selected"] == False:
                #    return available_values_df[current_table_row['level_str']].tolist()

                else: 
                    try:
                        user_selection_int = int(user_selection)
                        print(calendar_lookup_table_df['prompt'][user_selection_int])
                        user_selected[user_selection_int] = True
                        logging.debug('user selected date range int is: {}'.format(calendar_lookup_table_df['prompt'][user_selection_int]))
                        return user_selected
                    except KeyError:
                        logging.error('Key Error')
                        print("Your entry does not match up to a column. Try again\n")
                    except ValueError:
                        logging.error('Value Error')
                        print("Your Value is not a character or")


        def input_date_range(self, calendar_lookup_table_df):
            logging.info('creating user_input column of calendar_lookup')
            logging.info('User inputing date range if possible')
            user_input = pd.Series([False, False , (False,False), False, False, False, False, False])
            for i in range(len(calendar_lookup_table_df)) :
        
                if calendar_lookup_table_df.at[i,'user_selected'] == True and i == 0:
                    user_input[i] = True
                    logging.debug('User input at {} is True'.format(i))
        
                elif calendar_lookup_table_df.at[i,'user_selected'] == True and i == 1:
                    user_input[i]  = True
                    logging.debug('User input at {} is True'.format(i))

                elif calendar_lookup_table_df.at[i,'user_selected'] == True and i == 2:
                    while calendar_lookup_table_df.at[i,'user_selected'] == True:
                        start_date = input("Enter a start date\n\n")
                        #create a check here
                        end_date = input("Enter an end Date\n")
                        #create a check here
                        user_input[i] = (start_date,end_date)
                        logging.debug('User input at {} is {}'.format(i,(start_date, end_date)))
                        break

                elif calendar_lookup_table_df.at[i,'user_selected'] == True and i == 3:
                    #print('test')
                    user_response = input('Enter a Date:\n')
                    #calendar_lookup_table_df.at[i,'user_input'] =(user_response, user_response)
                    user_input[i] = user_response
                    logging.debug('User input at {} is {}'.format(i, user_response))
                elif calendar_lookup_table_df.at[i,'user_selected'] == True and i == 4:
                    user_response = input('Enter The number of days back:\n')
                    #calendar_lookup_table_df.at[i,'user_input'] = (user_response, user_response)
                    user_input[i] = user_response
                    logging.debug('User input at {} is {}'.format(i, user_response))
                elif calendar_lookup_table_df.at[i,'user_selected'] == True and i == 5:
                    user_response = input('Enter The number of weeks back:\n')
                    #calendar_lookup_table_df.at[i,'user_input'] = (user_response, user_response)
                    user_input[i] = user_response
                    logging.debug('User input at {} is {}'.format(i, user_response))
                elif calendar_lookup_table_df.at[i,'user_selected'] == True and i == 6:
                    user_response = input('Enter The number of Months back:\n')
                    #calendar_lookup_table_df.at[i,'user_input'] = (user_response, user_response)
                    user_input[i] = user_response
                    logging.debug('User input at {} is {}'.format(i, user_response))
                elif calendar_lookup_table_df.at[i,'user_selected'] == True and i == 7:
                    #calendar_lookup_table_df.at[i,'user_input'] = (True,True)
                    user_input[i] =  True
                    logging.debug('User input at {} is True'.format(i))
                else:
                continue
            #print(user_input)
            logging.info('Returned user input column of calendar table lookup')
            return(user_input)
                #print(calendar_lookup_table_df)
            

        def sql_date_range(self, calendar_lookup_table_df):
            logging.info('Creating date_range column of calendar table lookup')
            date_range = pd.Series(
                [
                    (
                        'CONVERT(date, GETDATE())'
                        ,'CONVERT(date, GETDATE())'
                    )
                    ,
                    (
                        'DATEADD(day,-1, CONVERT(date, GETDATE()))'
                        ,'DATEADD(day,-1, CONVERT(date, GETDATE()))'
                    )
                    ,
                    ( 
                        calendar_lookup_table_df['user_input'][2][0]
                        ,calendar_lookup_table_df['user_input'][2][1]
                    )
                    ,
                    (
                        calendar_lookup_table_df['user_input'][3]
                        ,calendar_lookup_table_df['user_input'][3]
                    ) 
                    ,
                    (
                        'DATEADD(day,-{}, CONVERT(date, GETDATE()))'.format(calendar_lookup_table_df['user_input'][4])
                        ,'DATEADD(day,-1, CONVERT(date, GETDATE()))'
                    )
                    , 
                    (
                        '(DATEADD(dd,  6, DATEADD(ww, DATEDIFF(ww, 0, DATEADD(dd, -1, CURRENT_TIMESTAMP)) - {}, 0))'.format(calendar_lookup_table_df['user_input'][5])
                        ,'DATEADD(dd,  6, DATEADD(ww, DATEDIFF(ww, 0, DATEADD(dd, -1, CURRENT_TIMESTAMP)) - 1, 0)))'
                    )
                    ,
                    (
                        'DATEADD(month, -1, DATEADD(DAY, 1, EOMONTH(GETDATE(), - {})))'.format(calendar_lookup_table_df['user_input'][6])
                        ,'EOMONTH(GETDATE(), -1)'
                    )
                    , 
                    (
                        'DATEADD(DAY, 1, EOMONTH(GETDATE(), -1))'
                        ,'CONVERT(day, GETDATE()'
                    )
                ]
            )
            #print(date_range)
            logging.info('Returned date column of calendar table lookup')
            return date_range 

        
        def select_sub_levels(self,working_table):
            logging.info('selecting sub levels')
            i: int = 0 
            j: int = 1
            for row in working_table.itertuples():

                if row.can_select == True:
            
                    sub_level_list : list = working_table['sub_levels'][0:i]
                    level_list : list = working_table['level_str'][0:i]
                    level_sub_level_list = tuple(zip(level_list, sub_level_list))
                    #print(select_list)
                    try:
                        working_table.at[i, 'sub_levels'] = self.select_sub_level(level_sub_level_list, row, i)
                        self.display_current_table(working_table,i, j)
                        i += 1
                        j+=1
                        logging.debug('Returned sub levels at {}'.format(i))
                    except KeyError:
                        print("Key Error")
                        logging.error('Key Error')


        def select_sub_level(self, working_lst, current_table_row, i):
            logging.info('User Selecting individual sub-level')
            selected_values_lst : list = []
            query : str = ''
            k: str = ''
            v: list = []
            tup: tuple = ()
            addition: str = ''
            user_selection: str = ''
            user_selection_int: int = -1 
            available_values_df = pd.DataFrame()
            if i == 0:
                query = 'SELECT DISTINCT {} FROM {}'.format(current_table_row.sub_level_select, current_table_row.table_str)
                #print('Query = {}'.format(query))
            else:
                tup = working_lst[0]
                k = tup[0]
                v = tup[1]
                query = 'SELECT DISTINCT {} FROM {} WHERE {} IN ({})'.format(current_table_row.sub_level_select, current_table_row.table_str,k,str(v)[1:-1] )
                for tup in working_lst[1:]:
                    addition = ' AND {} IN ({})'.format(tup[0], str(tup[1])[1:-1])
                    query = query + addition 
                #print('Query = {}'.format(query))
            available_values_df = pd.read_sql_query(query, self.sql_connection.connection)   
            #logging.info('select_sub_level query at {} is {} '.format(i, query)) 
            print("This is the selection table\n")
            #print(available_values_df)
            
            while current_table_row:
                print(available_values_df)
                print('\n')
                print("Current Selection: \n")
                print(selected_values_lst)
                print('\n')
                print("Enter the integer associated to the *{}* value you want to add to the report".format(current_table_row.level_str))
                print("Enter (d)one when finished\n")
                print("-----------------------------------------------------------------------------")
                user_selection = input("User Input: ").lower()
                #print(user_selection)
                #D finishes the loop and returns the list
                if user_selection == 'd' or user_selection == 'done':
                    if selected_values_lst == []:
                        selected_values_lst = available_values_df[current_table_row.level_str].tolist()
                    print("-----------------------------------------------------------------------------")
                    return selected_values_lst
                    #current_table_row['level_str'] = selected_values_lst 
                #a fills the list with all available values.  #d will do the same if the user did not select any
                elif user_selection == 'a' or user_selection == 'all':
                    
                    selected_values_lst = available_values_df[current_table_row.level_str].tolist()
                    print("-----------------------------------------------------------------------------")
                    return selected_values_lst
                    #current_table_row['level_str'] = selected_values_lst                 
                #quit cancels the search all together and returns false.  
                elif user_selection == '': 
                    if selected_values_lst == []:
                        selected_values_lst = available_values_df[current_table_row.level_str].tolist()
                    print("-----------------------------------------------------------------------------")
                    logging.debug('user selected sub values at {} are {}'.format(i, str(selected_values_lst)))
                    return selected_values_lst
                elif user_selection == 'q' or user_selection =='quit':
                    return False       
                
                #elif current_table_row["user_selected"] == False:
                #    return available_values_df[current_table_row['level_str']].tolist()

                else: 
                    try:
                        user_selection_int = int(user_selection)
                        print(available_values_df[current_table_row.level_str][user_selection_int])
                        if available_values_df[current_table_row.level_str][user_selection_int] in selected_values_lst:
                            print("You already selected {}.  Try again\n".format(available_values_df[current_table_row.level_str][user_selection_int]))
                        else: 
                            selected_values_lst.append(available_values_df[current_table_row.level_str][user_selection_int])
                            logging.debug('appended {} to selected sub levels'.format(available_values_df[current_table_row.level_str][user_selection_int]))
                    except KeyError:
                        print("Your entry does not match up to a column. Try again\n")
                        logging.error('Key Error')
                    except ValueError:
                        print("Your Value is not a character or")
                        logging.error('Value Error')

        def display_current_table(self, working_table,i,j ):
            logging.info('Displaying the current table to the user')
            query : str = ''
            k: str = ''
            v: list = []
            tup: tuple = ()
            addition: str = ''

            sub_level_list = working_table['sub_levels'][0:i+1]
            level_list = working_table['level_str'][0:i+1]
            level_sub_level_list = tuple(zip(level_list, sub_level_list))
            select_list = working_table['level_str'][0:j+1].tolist()
            current_table_row = working_table.iloc[i]

            select_list_str = str(select_list)
            select_list_str = select_list_str.replace("'", "")
            select_list_str = select_list_str[1:-1] 
            current_table_df = pd.DataFrame()
            if i == 0:

                sub_list = current_table_row.sub_levels
                query = 'SELECT DISTINCT {} FROM {} WHERE {} IN ({})'.format(current_table_row.level_str, current_table_row.table_str,current_table_row.level_str,str(sub_list)[1:-1] )
                
            else: 
                tup = level_sub_level_list[0]
                k = tup[0]
                v = tup[1]
                query = 'SELECT DISTINCT {} FROM {} WHERE {} IN ({})'.format(select_list_str, current_table_row.table_str,k,str(v)[1:-1] )
                for tup in level_sub_level_list[1:]:
                    addition = ' AND {} IN ({})'.format(tup[0], str(tup[1])[1:-1])
                    query = query + addition 

            print("\n\n\n\n\n")
            print("This is your current Table")
            print("\n")
            #rint(query)
            current_table_df = pd.read_sql_query(query, self.sql_connection.connection)
            print(current_table_df)    
            print("\n\n\n\n\n")


    class report():

        def __init__(self):
            logging.info('Initiating Report Class')
            self.report_selection = self.select_report(True)
            self.report_sorted = self.report_sorter(self.report_selection)
            logging.info('Report Class Initiated')
        
        def report_sorter(self,report_selection):
            logging.info('Report Sorter Called')
            test = int(report_selection[0])
            print(test)
            if report_selection == False:
                print('false')
                logging.info('Report Sorter Returned False')
                return False
            elif report_selection[0] == 0 :
                logging.info('Report Sorter is Creating a Sales Report')
                self.report = sales_report()
                logging.info('Report Sorter Created a Sales Report')
                logging.info('Report_Sorter will return True')
                return True
            elif report_selection[0] == 2: 
                logging.info('Report Sorter is Running the last report')
                self.report = last_report()
                logging.info('Report Sorter Created a Sales Report')
                logging.info('Report_Sorter will return True')
                return True

        def select_report(self,report_selection):
            logging.info('User is selecting report')
            available_reports_dict = {0 :"Sales", 1 :"some other report", 2: "Run Last Report"}
            available_reports_list = []

            for key in available_reports_dict:
                available_reports_list.append(key)    

                while report_selection:  
                    print("\n")
                    #print(available_reports_list)
                    print("Select a Report\n")
                    for key,value in available_reports_dict.items():
                        print(key,value)
                        print("\n")
                    print("-----------------------------------------------------------------------------")
                    report_selection = input("User input: ")

                    if report_selection == 'q' or report_selection == 'quit':
                        return False
                    else:
                        try: 
                            report_selection = int(report_selection)
                            logging.debug('User Selected {}'.format(available_reports_dict[int(report_selection)]))
                            return (report_selection, available_reports_dict[int(report_selection)])
                        except ValueError:
                            print('The entry is not an integer.\n')
                            print("Enter <q>uit to quit or try again")
                            print("-----------------------------------------------------------------------------")  
                            logging.error('Value Error')

    class last_report():
        
        def __init__(self,):
            self.sql_connection = sql_connection()
            self.query = self.get_last_query()
            self.isf_table = self.create_isf_table(self.query,self.sql_connection.connection)
            self.custom_dataframe = create_custom_dataframe(self.isf_table)

        def get_last_query(self):
            cwd = os.path.dirname(os.path.realpath(__file__))
            path = '{}/queries.csv'.format(cwd)
            #fieldnames = ['DateTime', 'User', 'Query']
            with open(path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                #line_count = 0
                for row in csv_reader:
                    last_row = row
                    #line_count +=1
                #print(f'Processed {line_count} lines.')
                #print(last_row[1])
                return last_row[2]

        def create_isf_table(self, query,sql_connection):
            print('********************************************************')
            print('Creating your report.  This could take a little while.\n')
            print('********************************************************')
            isf_table_df = pd.read_sql_query(query, sql_connection)
            #print(query)
            #print(isf_table_df)
            return isf_table_df

    class universal_settings():

        def __init__(self):
            self.cwd = (os.path.dirname(os.path.realpath(__file__)))
            self.user = os.getlogin()
            pandas_options = self.set_pandas_options(self.cwd)
            logging_options = self.set_logging_options(self.cwd)
            
            if pandas_options == True:
                logging.info('Pandas Options Successfully Set')
            if logging_options == True:
                logging.info('Loggin Options Successfully Set')



        def set_pandas_options(self,cwd):
            pd.set_option('display.max_rows', None)
            return True
        def set_logging_options(self,user):
            FORMAT = '%(asctime)-15s %(levelname)s: %(funcName)s %(message)s'
            logging.basicConfig(filename='{}/log.log'.format(self.cwd),format=FORMAT, level=logging.DEBUG)
            return True
    
        
    class write_to_file():
        
        def __init__(self,final_report,cwd): 
            logging.info('Writing to Excel')
            #self.excel_path = cwd + '/program_output.xlsx'
            query_path = cwd + '/queries.csv'
            login = os.getlogin()
            date = datetime.datetime.now()
            datetime_str = date.strftime("%Y-%m-%d %H:%M")
            #self.writer = ExcelWriter(self.excel_path)
            self.looked_up_to_excel = self.lookup_to_excel(final_report, cwd)
            self.ISFed_to_excel = self.ISF_to_Excel(final_report,cwd)
            try:
                self.exported_to_csv = self.export_to_csv(query_path, datetime_str, login, final_report.transaction_dataframe.query)
            except AttributeError:
                pass
            try:
                self.exported_to_csv = self.export_to_csv(query_path, datetime_str, login, final_report.query)
            except AttributeError:
                pass

        def lookup_to_excel(self, final_report, cwd):
            logging.info('Exporting to Excel')
            #writer = ExcelWriter(path)
            print('********************************************************')
            print('Report is Done.  Exporting to Excel.\n')
            print('********************************************************')
            #cwd = (os.path.dirname(os.path.realpath(__file__)))
            try: 
                print('writing org')
                excel_path = cwd + '/lookup_tables.xlsx'
                writer = ExcelWriter(excel_path)
                final_report.inital_parameters.organization_table_lookup.to_excel(writer,'organization_table_lookup')
            except AttributeError:
                pass
            try:
                print('writing product')
                final_report.inital_parameters.product_table_lookup.to_excel(writer,'product_table_lookup')
                writer.save()
            except AttributeError:
                pass
            try:
                print('writing cal')
                final_report.inital_parameters.calendar_table_lookup.to_excel(writer,'calendar_table_lookup')
                writer.save()
            except AttributeError:
                pass
            return True
        def ISF_to_Excel(self, final_report,cwd):

            try:
                print('writing items_sales_Fact')
                excel_path = cwd + '/item_sales_fact.xlsx'
                writer = ExcelWriter(excel_path)
                final_report.custom_dataframe.modified_transaction_table.to_excel(writer,'Item_Sales_Fact_Agg')  #Case of running the last report from file
                writer.save()
            except AttributeError:
                pass
            """
            try:
                print('writing Transaction_Table')
                excel_path = cwd + '/Transaction_Table.xlsx'
                writer = ExcelWriter(excel_path)
                final_report.custom_dataframe.isf_table.to_excel(writer,'Item_Sales_Fact_Agg')  #Case of running the last report from file
                writer.save()
            except AttributeError:
                pass
            """
            #writer.save()
            print('********************************************************')
            print('Exported to Excel.  You can find the data at {}.\n'.format(cwd))
            print('********************************************************')
            logging.info('Exported to Excel')
            return True
        
        def export_to_csv(self,query_path,datetime, login,query):

            with open(query_path, 'a+', newline='') as csvfile:
                query_writer = csv.writer(csvfile, delimiter=',')
                query_writer.writerow([datetime,login,query])
            return True

    class sql_connection():

        def __init__ (self):

            logging.debug('Connecting To Database')
            system = platform.system()
            system = system.lower()
            #print(self.system)
            if system =='windows':
                driver = '{ODBC Driver 17 for SQL Server}'
            else:
                driver = '/usr/local/lib/libmsodbcsql.17.dylib'
            server = 'wouldnt you like to know' 
            database = 'Testing' 
            username = 'jnapolitano' 
            password = '***********' 

            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                                SERVER=' + server + '; \
                                DATABASE=' + database +'; \
                                Trusted_Connection=yes;')
            #driver='/usr/local/lib/libmsodbcsql.17.dylib'
            # self.connection = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            self.cursor = self.connection.cursor()

    if __name__ =='__main__':
        universal_settings = universal_settings()
        logging.info('Testing_Main Function')
        #onnection = sql_connection
        print("******************************************")
        print("***** Oil Report Builder Version 0.0")
        print("******************************************")
        final_report = report()
        write_to_file = write_to_file(final_report.report,universal_settings.cwd)
    
    #The main function. Intitates the process of selecting the reports.  
    #The end.  Watch demo video to see code in action.
        
