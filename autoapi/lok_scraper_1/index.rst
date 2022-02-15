:py:mod:`lok_scraper_1`
=======================

.. py:module:: lok_scraper_1


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

   .. py:method:: create_node(key)


   .. py:method:: node_generator(self, data, name='')



.. py:class:: search_result(dict_item, num_columns, colnum_string)

   .. py:method:: create_column_request(self)


   .. py:method:: create_column_range_string(self)


   .. py:method:: colnum_string(self, num_columns)



.. py:class:: google_drive(creds)

   .. py:method:: test(self)


   .. py:method:: get_drive_service(self, creds)

      Shows basic usage of the Drive v3 API.
      Prints the names and ids of the first 10 files the user has access to.


   .. py:method:: create_folder(self, title)


   .. py:method:: add_spreadsheet_to_folder(self, folder_id, title)



.. py:class:: google_sheet(creds)

   .. py:method:: get_sheet_service(self, creds)



.. py:class:: google_creds(creds_path)

   .. py:method:: get_creds(self, creds_path)



.. py:class:: config(file_path)

   .. py:method:: load_config(self, file_path)



.. py:class:: search_results_page(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1, column_lookup_table={}, num_columns=0)

   .. py:method:: create_search_result_node(self)


   .. py:method:: append_to_data_list(self, rnge, d, data_list)


   .. py:method:: map_columns_to_batch_request_list(self)


   .. py:method:: colnum_string(self)


   .. py:method:: map_columns_to_lookup_table(self)


   .. py:method:: get_next_url(self)


   .. py:method:: create_search_url(self, base_url, collection, json_parameter, results_per_page, query_param, page_param, page_num)


   .. py:method:: say_hello(self)


   .. py:method:: request_data(self)


   .. py:method:: response_to_json(self)


   .. py:method:: html_parse(self)


   .. py:method:: flatten_result(self)



.. py:function:: create_google_credentials_object(creds_path='credentials.json')


.. py:function:: create_config_object(file_path='config.yaml')


.. py:function:: search_result_generator(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1, condition=True)


.. py:function:: create_search_results_page_object(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1, column_lookup_table={})


.. py:function:: create_google_drive_object(google_creds)


.. py:function:: create_google_sheet_object(google_creds)


.. py:function:: create_new_google_sheet(google_drive_object, folder_id, title)


.. py:function:: flatten_result(result_json)


.. py:function:: main()


