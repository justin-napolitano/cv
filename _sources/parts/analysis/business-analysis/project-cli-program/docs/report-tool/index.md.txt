:::{post}
:tags: reporting, analysis, business-analysis
:category: python, reporting, business-analysis
:author: Justin Napolitano
:location: TX
:language: en
:::


```{eval-rst}

:py:mod:`report_tool`
=====================

.. py:module:: report_tool


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   report_tool.sales_report
   report_tool.create_custom_dataframe
   report_tool.create_transaction_dataframe
   report_tool.get_initial_parameters
   report_tool.report
   report_tool.last_report
   report_tool.universal_settings
   report_tool.write_to_file
   report_tool.sql_connection




Attributes
~~~~~~~~~~

.. autoapisummary::

   report_tool.settings


.. py:class:: sales_report

   A class that creates a sales report object.
   initial_parameteres will contain one initial parameters dataframe for each of the product, organization, and calendar tables
   transaction_datframe will contain the component strings to query the sql server, the final query, and the transaction dataframe


.. py:class:: create_custom_dataframe(transaction_dataframe)

   A class that modifies the dataframe by grouping and adding useful columns.


   .. py:method:: select_transaction_data(self, group_by_selection, transaction_dataframe)


   .. py:method:: select_group_by(self, transaction_datframe)



.. py:class:: create_transaction_dataframe(initial_parameters)

   A class that will create a dataframe object of transactions as defined by the get_initial_parameters dataframe objects


   .. py:method:: create_organization_table_query(self, organization_table_lookup)


   .. py:method:: create_product_table_query(self, product_table_lookup)


   .. py:method:: create_calendar_table_query(self, calendar_table_lookup, sql_connection)


   .. py:method:: create_isf_table_query(self)


   .. py:method:: create_isf_table_dataframe(self, query, sql_connection)



.. py:class:: get_initial_parameters

   A class that gets the initial parameters from the user
   to use in constructing a dataframe of transactions

   .. py:method:: connect(self)


   .. py:method:: create_organization_table_lookup(self)


   .. py:method:: create_product_table_lookup(self)


   .. py:method:: create_calendar_table_lookup(self)


   .. py:method:: select_date_range(self, calendar_lookup_table_df)


   .. py:method:: input_date_range(self, calendar_lookup_table_df)


   .. py:method:: sql_date_range(self, calendar_lookup_table_df)


   .. py:method:: select_sub_levels(self, working_table)


   .. py:method:: select_sub_level(self, working_lst, current_table_row, i)


   .. py:method:: display_current_table(self, working_table, i, j)



.. py:class:: report

   .. py:method:: report_sorter(self, report_selection)


   .. py:method:: select_report(self, report_selection)



.. py:class:: last_report

   .. py:method:: get_last_query(self)


   .. py:method:: create_isf_table(self, query, sql_connection)



.. py:class:: universal_settings

   .. py:method:: set_pandas_options(self, cwd)


   .. py:method:: set_logging_options(self, user)



.. py:class:: write_to_file(final_report, cwd)

   .. py:method:: lookup_to_excel(self, final_report, cwd)


   .. py:method:: ISF_to_Excel(self, final_report, cwd)


   .. py:method:: export_to_csv(self, query_path, datetime, login, query)



.. py:class:: sql_connection


.. py:data:: settings
   

   

```