:py:mod:`lok_scraper_1`
=======================

.. py:module:: lok_scraper_1
   :noindex:


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   lok_scraper_1.node_json
   lok_scraper_1.search_result
   lok_scraper_1.google_drive
   lok_scraper_1.google_sheet
   lok_scraper_1.google_creds
   lok_scraper_1.config
   lok_scraper_1.search_results_page



Functions
~~~~~~~~~

.. autoapisummary::

   lok_scraper_1.create_google_credentials_object
   lok_scraper_1.create_config_object
   lok_scraper_1.search_result_generator
   lok_scraper_1.create_search_results_page_object
   lok_scraper_1.create_google_drive_object
   lok_scraper_1.create_google_sheet_object
   lok_scraper_1.create_new_google_sheet
   lok_scraper_1.flatten_result
   lok_scraper_1.main



.. py:class:: node_json(data)
   :noindex:

   .. py:method:: create_node(key)
      :noindex:

   .. py:method:: node_generator(self, data, name='')
      :noindex:


.. py:class:: search_result(dict_item, num_columns, colnum_string)
   :noindex:

   .. py:method:: create_column_request(self)
      :noindex:

   .. py:method:: create_column_range_string(self)
      :noindex:

   .. py:method:: colnum_string(self, num_columns)
      :noindex:


.. py:class:: google_drive(creds)
   :noindex:

   .. py:method:: test(self)
      :noindex:

   .. py:method:: get_drive_service(self, creds)
      :noindex:

      Shows basic usage of the Drive v3 API.
      Prints the names and ids of the first 10 files the user has access to.


   .. py:method:: create_folder(self, title)
      :noindex:

   .. py:method:: add_spreadsheet_to_folder(self, folder_id, title)
      :noindex:


.. py:class:: google_sheet(creds)
   :noindex:

   .. py:method:: get_sheet_service(self, creds)
      :noindex:


.. py:class:: google_creds(creds_path)
   :noindex:

   .. py:method:: get_creds(self, creds_path)
      :noindex:


.. py:class:: config(file_path)
   :noindex:

   .. py:method:: load_config(self, file_path)
      :noindex:


.. py:class:: search_results_page(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1, column_lookup_table={}, num_columns=0)
   :noindex:

   .. py:method:: create_search_result_node(self)
      :noindex:

   .. py:method:: append_to_data_list(self, rnge, d, data_list)
      :noindex:

   .. py:method:: map_columns_to_batch_request_list(self)
      :noindex:

   .. py:method:: colnum_string(self)
      :noindex:

   .. py:method:: map_columns_to_lookup_table(self)
      :noindex:

   .. py:method:: get_next_url(self)
      :noindex:

   .. py:method:: create_search_url(self, base_url, collection, json_parameter, results_per_page, query_param, page_param, page_num)
      :noindex:

   .. py:method:: say_hello(self)
      :noindex:

   .. py:method:: request_data(self)
      :noindex:

   .. py:method:: response_to_json(self)
      :noindex:

   .. py:method:: html_parse(self)
      :noindex:

   .. py:method:: flatten_result(self)
      :noindex:


.. py:function:: create_google_credentials_object(creds_path='credentials.json')
   :noindex:

.. py:function:: create_config_object(file_path='config.yaml')
   :noindex:

.. py:function:: search_result_generator(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1, condition=True)
   :noindex:

.. py:function:: create_search_results_page_object(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1, column_lookup_table={})
   :noindex:

.. py:function:: create_google_drive_object(google_creds)
   :noindex:

.. py:function:: create_google_sheet_object(google_creds)
   :noindex:

.. py:function:: create_new_google_sheet(google_drive_object, folder_id, title)
   :noindex:

.. py:function:: flatten_result(result_json)
   :noindex:

.. py:function:: main()
   :noindex:

