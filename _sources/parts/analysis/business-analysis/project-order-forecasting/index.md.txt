:::{post}
:tags: reporting, analysis, business-analysis
:category: python, reporting, business-analysis
:author: Justin Napolitano
:location: TX
:language: en
:::

:::{eval-rst}

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
  

Code Documentation 
-------------------

.. card:: 

    .. toctree::
        
        docs/cigarette_sales_order_form/index  

:::        