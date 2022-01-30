:py:mod:`loc_scraper`
=====================

.. py:module:: loc_scraper


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   loc_scraper.search_collections



Functions
~~~~~~~~~

.. autoapisummary::

   loc_scraper.create_search_collection_object
   loc_scraper.main



.. py:class:: search_collections(base_url, collection, json_parameter, results_per_page, query_param, page_param, page_num)

   .. py:method:: get_next_url(self)


   .. py:method:: create_search_url(self, base_url, collection, json_parameter, results_per_page, query_param, page_param, page_num)


   .. py:method:: say_hello(self)


   .. py:method:: request_data(self)


   .. py:method:: response_to_json(self)


   .. py:method:: html_parse(self)



.. py:function:: create_search_collection_object(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=240, nxt=True)


.. py:function:: main()


