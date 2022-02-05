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

