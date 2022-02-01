:py:mod:`csv_to_neo`
====================

.. py:module:: csv_to_neo


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   csv_to_neo.DataUploadFunctions
   csv_to_neo.DataPipelineFunctions



Functions
~~~~~~~~~

.. autoapisummary::

   csv_to_neo.upload_data_pipeline_to_neo
   csv_to_neo.instantiate_google_API
   csv_to_neo.instantiate_spark_API
   csv_to_neo.prepare_pandas_df
   csv_to_neo.instantiate_neo_model_api
   csv_to_neo.upload_df_to_db
   csv_to_neo.load_data_to_spark_df
   csv_to_neo.prepare_df_for_upload
   csv_to_neo.prepare_data_pipeline



Attributes
~~~~~~~~~~

.. autoapisummary::

   csv_to_neo.neo_model_api


.. py:function:: upload_data_pipeline_to_neo(df_pipeline_dictionary)


.. py:class:: DataUploadFunctions

   .. py:method:: upload_df(self, df)


   .. py:method:: map_to_df(self, df1, df2, lookup_value: str, lookup_key: str)


   .. py:method:: set_relationships(self, source_node, target_node)



.. py:class:: DataPipelineFunctions

   .. py:method:: write_df_to_csv(self, df, path: str)


   .. py:method:: create_city_nodes(self, df)


   .. py:method:: create_url_nodes(self, df)


   .. py:method:: create_root_nodes(self, df)


   .. py:method:: create_country_nodes(self, df)


   .. py:method:: return_unique_country_df(self, df)


   .. py:method:: create_state_nodes(self, df)


   .. py:method:: return_unique_state_df(self, df)


   .. py:method:: rename_columns(self, df, mapper={'city': 'city_name', 'state': 'state_code', 'realtor_url': 'root_realtor_url'})


   .. py:method:: add_country_code(self, country_code='USA')


   .. py:method:: add_country_name(self, country_name='United States of America')


   .. py:method:: upload_df(self, df)


   .. py:method:: set_url_relationships(self)


   .. py:method:: set_city_relationships(self)


   .. py:method:: set_state_relationships(self)


   .. py:method:: group_by_state(self)


   .. py:method:: load_data_to_pandas_df(self, file_path='/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv')


   .. py:method:: nodify_city_column(self)


   .. py:method:: nodify_states_column(self)


   .. py:method:: nodify_url_column(self)



.. py:function:: instantiate_google_API()


.. py:function:: instantiate_spark_API()


.. py:function:: prepare_pandas_df()


.. py:function:: instantiate_neo_model_api()


.. py:function:: upload_df_to_db(df, neo_model_api)


.. py:function:: load_data_to_spark_df(sparkAPI)


.. py:function:: prepare_df_for_upload(df)


.. py:function:: prepare_data_pipeline()


.. py:data:: neo_model_api
   

   

