.. post:: 
   :tags: python, supreme-court, political-analysis
   :category: political analysis, supreme court
   :author: Justin Napolitano
   :location: TX
   :language: en


MetaData Graph
===================================

Description
----------------------

* The application is written python.
* It scrapes the US Library of Congress API for every Us Supreme Court case to extract metadata that is then imported int a graph for analysis. 
* I also experimented with test driven deleopment on this project to learn the pytest library. 

How to Improve
-------------------

* Import the graph into a Janus Stack
* Recode into a POLE style graph. People would be the Justices;.  Objects would be the issue areas.  Locations may be removed and replaced by outcomes.  Events would be the individual cases. 
* The POLE can be expanded to include interactions between states, practitioners, issues, political party, ad infinitum.  


External Links
----------------

.. card:: 

   * `Github <https://github.com/justin-napolitano/USSupremeCourtMetaDataGraph/blob/main/active_code_base/lok_scraper_1.py>`_
   * `The Supreme Court Datbase <http://scdb.wustl.edu/about.php?s=3>`_
   * `Sphinx Documentation <https://court-behavior.io/metadata-graph/graph-abstract.html>`_



Module Documentation
----------------------

.. card:: 
   
   .. toctree::
      :caption: Module Documentation
      :maxdepth: 2


      docs/lok_scraper_1/index.rst
      docs/loc_scraper_test/index.rst



