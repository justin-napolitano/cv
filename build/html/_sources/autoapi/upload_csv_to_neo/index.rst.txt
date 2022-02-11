:py:mod:`upload_csv_to_neo`
===========================

.. py:module:: upload_csv_to_neo


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   upload_csv_to_neo.PreparePandasDF



Functions
~~~~~~~~~

.. autoapisummary::

   upload_csv_to_neo.instantiate_google_API
   upload_csv_to_neo.instantiate_spark_API
   upload_csv_to_neo.prepare_pandas_df
   upload_csv_to_neo.instantiate_neo_model_api
   upload_csv_to_neo.upload_df_to_db
   upload_csv_to_neo.load_data_to_spark_df
   upload_csv_to_neo.prepare_df_for_upload



Attributes
~~~~~~~~~~

.. autoapisummary::

   upload_csv_to_neo.neo_model_api


.. py:class:: PreparePandasDF

   .. py:method:: upload_df(self, df)


   .. py:method:: set_url_relationships(self)


   .. py:method:: set_city_relationships(self)


   .. py:method:: set_state_relationships(self)


   .. py:method:: get_unique_state_nodes(self)


   .. py:method:: get_unique_country_nodes(self)


   .. py:method:: group_by_state(self)


   .. py:method:: load_data_to_pandas_df(self, file_path='/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv')


   .. py:method:: nodify_city_column(self)


   .. py:method:: nodify_states_column(self)


   .. py:method:: nodify_url_column(self)


   .. py:method:: nodify_country_column(self)



.. py:function:: instantiate_google_API()


.. py:function:: instantiate_spark_API()


.. py:function:: prepare_pandas_df()


.. py:function:: instantiate_neo_model_api()


.. py:function:: upload_df_to_db(df, neo_model_api)


.. py:function:: load_data_to_spark_df(sparkAPI)


.. py:function:: prepare_df_for_upload(df)


.. py:data:: neo_model_api
   

   

