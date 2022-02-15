#cigarette_sales_order_form.py
#Justin Napolitano
#05/08/2020

#Reads data from CSV into dataframe
#Converts numbers into readable data
#Exports requested data to Excel Spreadsheet
#If a product requires ordering it will appear on the spreadsheet with the barcode
#Sphinx didn't like that I had moved the "pointer" of df2 so many times.
#So I appended the operation to the name of each dataframe instead of keeping the df2 name..  Though confusing
#next time i will also keep df2 so i know the origin.  

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
grouped_df = df2.groupby(["week number", 'Store', 'Cigarette Name', "Cigarette UPC","Item Number", "Sell Unit Quantity"]).sum()

#df3 = df2.groupby(["week number", "Cigarette Name","Cigarette UPC","Item Number", "Store"]).sum()

grouped_df["Total Cartons Sold"] = grouped_df["Total Cartons Sold"] /10

#Joining a weekly average dataframe to the main dataframe
weekly_average = pd.DataFrame()
weekly_average["Average Cartons Sold Weekly"] = grouped_df["Total Cartons Sold"].groupby('Cigarette Name').mean()
joined_grouped_df = grouped_df.join(weekly_average, on="Cigarette Name")
sorted_joined_grouped_df = joined_grouped_df.sort_values(by=['week number'], ascending =False)


#Adding the Order collumn to frame
sorted_joined_grouped_df["Order"] = None



#Ccomparing average to total carton sales
#df2['Order'] = np.where((df2['Average Cartons Sold Weekly'] >= df2['Total Cartons Sold'] )
#                    , True, False)

sorted_joined_grouped_df['Order'] = np.where((sorted_joined_grouped_df['Average Cartons Sold Weekly'] <= sorted_joined_grouped_df['Total Cartons Sold']) & (df2["Total Cartons Sold"] >=1)
                    , True, False)

#df2['Order'] = np.where(df2['Average Cartons Sold Weekly'] >= df2['Total Cartons Sold'] ) #and np.where(df2["Total Cartons Sold"]>=1)                  

#Creating DataFrame to display.  Only one week of data at a time
x = sorted_joined_grouped_df.index[0][0]
for i in range (len(sorted_joined_grouped_df.index)) :
    if sorted_joined_grouped_df.index[i][0] == x:
        max_i = i 


maxed_sorted_joined_grouped_df = sorted_joined_grouped_df[:max_i + 1]
sorted_maxed_sorted_joined_grouped_df = maxed_sorted_joined_grouped_df.sort_values(by=['Cigarette Name'], ascending =True)

#exporting to excel
sorted_maxed_sorted_joined_grouped_df.to_csv(cwd + "/order_form.csv")
sorted_joined_grouped_df.to_csv(cwd + "/all_data.csv")

