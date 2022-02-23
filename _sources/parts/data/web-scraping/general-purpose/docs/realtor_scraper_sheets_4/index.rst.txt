:py:mod:`realtor_scraper_sheets_4`
==================================

.. py:module:: realtor_scraper_sheets_4


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   realtor_scraper_sheets_4.scrape
   realtor_scraper_sheets_4.clean_up_data
   realtor_scraper_sheets_4.append_delete_duplicates_request
   realtor_scraper_sheets_4.drop
   realtor_scraper_sheets_4.pop
   realtor_scraper_sheets_4.get_soup
   realtor_scraper_sheets_4.get_web_data
   realtor_scraper_sheets_4.get_request
   realtor_scraper_sheets_4.send_batch_update_request
   realtor_scraper_sheets_4.append_blank_rows
   realtor_scraper_sheets_4.append_blank_columns
   realtor_scraper_sheets_4.append_columns_to_data_list
   realtor_scraper_sheets_4.append_to_data_list
   realtor_scraper_sheets_4.send_update_values_request
   realtor_scraper_sheets_4.create_spreadsheet
   realtor_scraper_sheets_4.get_drop_list
   realtor_scraper_sheets_4.get_pop_list
   realtor_scraper_sheets_4.check_state_dict
   realtor_scraper_sheets_4.check_columns



.. py:function:: scrape(df, sheets_service, drive_service, folder_id)


.. py:function:: clean_up_data(spreadsheet_id, num_rows, sheets_service)


.. py:function:: append_delete_duplicates_request(spreadsheet_id, requests_list, num_rows)


.. py:function:: drop(normalized, drop_list)


.. py:function:: pop(data, pop_list)


.. py:function:: get_soup(real_url, response)


.. py:function:: get_web_data(soup)


.. py:function:: get_request(real_url, headers)


.. py:function:: send_batch_update_request(requests, spreadsheet_id, sheets_service)


.. py:function:: append_blank_rows(spreadsheet_id, length, requests_list)


.. py:function:: append_blank_columns(spreadsheet_id, length, requests_list)


.. py:function:: append_columns_to_data_list(seen_columns, normalized, data_list, num_rows, start)


.. py:function:: append_to_data_list(rnge, d, data_list)


.. py:function:: send_update_values_request(spreadsheet_id, data_list, sheets_service)


.. py:function:: create_spreadsheet(title, sheets_service)


.. py:function:: get_drop_list()


.. py:function:: get_pop_list()


.. py:function:: check_state_dict(drive_service, sheets_service, folder_id, state_dict, state)


.. py:function:: check_columns(columns, num_columns, seen_columns, spreadsheet_id, requests_list, data_list)


