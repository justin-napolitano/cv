.. _LLC:

BTJN, LLC
=========

.. _founder:

Founder and Lead Programmer
----------------------------

.. topic:: Overview

    I founded this company to complete contract work.

    Below are my notable projects. 

 Data Stream Management Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. card:: 

    * I wrote python scripts that manipulated the Google Sheets API to make a makeshift CRM application for a marketing firm.
    * I managed write an application that autonomously streamed, filtered, transformed and uploaded an average of 10,000 leads per week.


Google Sheets and Drive Library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. card:: 

    * To streamline my work flow in the data stream management application I saved common functions into a class that could be employed across a number of workflows.
    * I currently use it whenever I need to upload or download data from google sheets or create files in the google drive.  

Neo4j Realtor Graph
^^^^^^^^^^^^^^^^^^^^^

.. card:: 
    * With the data collected from the Data Stream Management Application I designed a graph of my leads to pinpoint high quality leads.
    * I initially wrote the scripts in python to use a Neo4j backend.  I discovered that the published library was lacking.  I therefore extended it slightly to achieve my use case. The link is here....

JanusGraph Realtor Graph
^^^^^^^^^^^^^^^^^^^^^^^^^
.. card:: 

    * Due to licensing limitations with Neo4j I pivotted to JanusGraph to build a realtor graph.
    * I collected the functions I used to build the graph into a class that can be viewed here.....


CRM Database and Python Management Scripting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. card:: 
    
    * I was contracted by a public health company that required a CRM application to sell consultations to organizations at the height of the Covid pandemic. 
    * They had initially requested a SQL backend which I accomplished with an Azure deployed SQL server.
    * My employers later requested a transition to an excel based implementation due to cost concerns.  
    * I then wrote Python scripts that integrated and filtered data from user created excel spreadsheets.  