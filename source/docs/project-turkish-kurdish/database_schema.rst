###################
Schema Definitions
###################

.. topic:: Overview

    This section contains the definitions and descriptions for every variable recorded in the data set. 


    :Date: |today|
    :Author: **Justin Napolitano**


Year
====

Definition 
    Records the year an event occurs

Data Type
    Integer

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`


Aggressor_ID
============


Definition
    Records the ID of the aggressor of an event; the agent or group that commits a human right violation.

Data Type
    Caegorical Integer.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:aggressor table`


Aggressor_Name
==============
    
Definition
    Records the name of the aggressor of an event; the agent or group that commits a human right violation.

Data Type
    String.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:aggressor table`


Victim_ID
=========
    
Definition   
    Records the ID of the victim of an event; the agent or group that is victim to a human right violation commited by the aggressor.

Data Type
    Categorical integer.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:victim table`.

Victim_Name
===========

Definition  
    Records the name of the victim of an event; the agent or group that is victim to a human right violation commited by the aggressor.

Data Type
    String.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:victim table`.

Source_Article
==============

Definition 
    A record of the name, data, and title of the source from which information on an event is gathered.

Data Type
    String.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Source_Date
===========

Definition
    The date the source material containing the information of an event record.

Data Type
    DateStamp.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Source_Headline
===============

Definition
    The title of the source material containing the information of an event record. 

Data Type
    String.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`


Region_Name
===========

Defintion
    The name of the administrative region an event was recorded.  Regions are defined according the offical provincial and administrative regions of the Turkish State.

Data Type
    String.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:region table`


Region_Code
===========

Definition
    The code of the administrative region an event was recorded.  Regions are defined according the offical provincial and administrative regions of the Turkish State.

Data Type
    Categorical Integer.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:region table`

Kurdish_Region
==============

Definition
    A boolean variable that indicates whether a region is predominantly Kurdish by population.

Data Type
    Boolean.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Province_Name
=============

Definition
    The name of the provincial level administrative region an event was recorded.  Provinces are defined according the offical provincial and administrative regions of the Turkish State.

Data Type
    String.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:province table`
    


Province_Code
=============

Definition
    The code of the provincial level administrative region an event was recorded.  Provinces are defined according the offical provincial and administrative regions of the Turkish State.

Data Type
    Categorical Integer.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:province table`


Country
=======

Definition
    The state (country) where an event is recorded.

Data Type
    Integer.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`



Date_Start
==========

Definition
    A record of the day, month, and year in the DD/MM/YYYY format of when an event takes starts.
    If the exact datastamp cannot be determined the best possible date is estimated.

Data Type
    DateStamp DD/MM/YYYY.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Date_End
========

Definition
    A record of the day, month, and yearn in the DD/MM/YYYY format of when an event ends.

Data Type
    DateStamp DD/MM/YYYY.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Women_Killed
=============

Definition
    The best estimate of deaths of women recorded for an event.

Data Type
    Integer.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Children_Killed
===============

Definition
    The best estimate of the number of deaths of children recorded for an event.

Data Type
    Integer.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`


Total_Killed
===============

Definition
    The sum of Women_Killed, Children_Killed, and any other deaths recorded for an event. 

Data Type
    Integer.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Women_Raped
===============

Definition
    The recorded number of women during an event.  

Data Type
    Integer.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Illegal_Arrests
=====================

Definition
    The recorded number of people illegally arrested during an event.  

Data Type
    Integer.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Illegal_Detentions
==================

Definition
    The recorded number of people illegally detained by any non-governmental agent or organization during an event.  

Data Type
    Integer

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

Illegal_Imprisonments
=====================

Definition
    The recorded number of people illegally imprisoned by the Turkish State during an event.  

Data Type
    Integer.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`


Human_Rights_Category_Code
==========================

Definition
    The code of the category of Human Rights violation as defined by Justin Napolitano and Demet Mousseau. Insert a reference here.

Data Type
    Categorical Integer.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:human rights category table`
    



Human_Rights_Category_Name
==========================

Definition
    The name of the category of Human Rights violation as defined by Justin Napolitano and Demet Mousseau. Insert a reference here.

Data Type
    String.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:human rights category table`



Human_Rights_Offense_Code
==========================

Definition
    The code of the offence to Human Rights as defined by the United Nations or Comparable International Treaty Organization.


Data Type
    Categorical Integer.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:human rights offense table`
    



Human_Rights_Offense_Name
==========================

Definition
    The name of the offence to Human Rights as defined by the United Nations or Comparable International Treaty Organization.

Data Type
    String.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:human rights offense table`


Is_Women_Event
==============

Definition
    A boolean variable that designates if an event primarily affects males or females.
        * 0 designates an event as affecting males.
        * 1 designates an event as affecting women.

Data Type
    Boolean.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`


Is_Children_Event
=================

Definition
    A boolean variable that designates if an event primarily affects adults or children.  
        * 0 designates an event as affecting adults. 
        * 1 designates an event as affecting children.

Data Type
    Boolean.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`


Description
===========

Definition
    A description of an event that may contain information that could not be relayed in the coding. 


Data Type
    String.


Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

ID
===

Definition
    A unique identifier for a coded event.
    
    * It is constructed by appending the values of: 
        #. year
        #. Aggressor_ID
        #. Victim_ID
        #. Human_Rights_Category_Code 
        #. Human_Rights_Offense_Code

    * For instance, id 19981265 is an event that occurred in 1998 committed by the Turkish government against women.  It is a broad violation of Collective Developmental rights.  Specifically, the right to freedom of peaceful assembly and association



Data Type
    String.

Reference Table
    :ref:`projects/project-turkish-kurdish/reference_tables:overview table`

