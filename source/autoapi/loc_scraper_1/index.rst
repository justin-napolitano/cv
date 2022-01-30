:py:mod:`loc_scraper_1`
=======================

.. py:module:: loc_scraper_1


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   loc_scraper_1.cd
   loc_scraper_1.search_results_page
   loc_scraper_1.search_result
   loc_scraper_1.google_drive
   loc_scraper_1.google_sheet
   loc_scraper_1.google_creds
   loc_scraper_1.config



Functions
~~~~~~~~~

.. autoapisummary::

   loc_scraper_1.create_google_credentials_object
   loc_scraper_1.create_config_object
   loc_scraper_1.search_result_generator
   loc_scraper_1.create_search_results_page_object
   loc_scraper_1.create_google_drive_object
   loc_scraper_1.create_google_sheet_object
   loc_scraper_1.create_new_google_sheet
   loc_scraper_1.flatten_result
   loc_scraper_1.main



.. py:class:: cd(newPath)

   Context manager for changing the current working directory

   .. py:method:: __enter__(self)


   .. py:method:: __exit__(self, etype, value, traceback)



.. py:class:: search_results_page(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1)

   .. py:method:: write_to_file(self, data=None, file_name='result_', file_num=0, extension='.json')


   .. py:method:: node_gen_2(self, data, root='result', node_list=[], edge_list=[], previous_k=None, previous_edge=None, graph=None)


   .. py:method:: node_runner(self, data, graph)


   .. py:method:: node_generator(self, data, root='title_testing', node_list=[], edge_list=[], previous_k=None, previous_edge=None)


   .. py:method:: create_json_graph(self)


   .. py:method:: create_search_result_node(self)


   .. py:method:: append_to_data_list(self, rnge, d)


   .. py:method:: map_column_to_range(self, column_key)


   .. py:method:: colnum_string(self, num_columns)


   .. py:method:: map_columns_to_lookup_table(self)


   .. py:method:: column_request_list_generator(self)


   .. py:method:: get_next_url(self)


   .. py:method:: create_search_url(self, base_url, collection, json_parameter, results_per_page, query_param, page_param, page_num)


   .. py:method:: say_hello(self)


   .. py:method:: request_data(self)


   .. py:method:: response_to_json(self)


   .. py:method:: html_parse(self)


   .. py:method:: flatten_result(self)



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



.. py:function:: create_google_credentials_object(creds_path='credentials.json')


.. py:function:: create_config_object(file_path='config.yaml')


.. py:function:: search_result_generator(condition=True)


.. py:function:: create_search_results_page_object(base_url='https://www.loc.gov/collections', collection='united-states-reports', json_parameter='fo=json', results_per_page='c=150', query_param='?', page_param='sp=', page_num=1)


.. py:function:: create_google_drive_object(google_creds)


.. py:function:: create_google_sheet_object(google_creds)


.. py:function:: create_new_google_sheet(google_drive_object, folder_id, title)


.. py:function:: flatten_result(result_json)


.. py:function:: main()


