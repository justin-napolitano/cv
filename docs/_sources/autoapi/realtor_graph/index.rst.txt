:py:mod:`realtor_graph`
=======================

.. py:module:: realtor_graph


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   realtor_graph.PandasActions
   realtor_graph.NeoAPI
   realtor_graph.GoogleAPIS
   realtor_graph.SparkAPI
   realtor_graph.neoModelAPI



Functions
~~~~~~~~~

.. autoapisummary::

   realtor_graph.instantiate_google_API
   realtor_graph.instantiate_spark_API
   realtor_graph.load_data_to_spark_df
   realtor_graph.prepare_df_for_upload
   realtor_graph.load_data_to_pandas_df
   realtor_graph.prepare_pandas_df
   realtor_graph.instantiate_neo_model_api
   realtor_graph.upload_df_to_db



Attributes
~~~~~~~~~~

.. autoapisummary::

   realtor_graph.neo_model_api


.. py:class:: PandasActions

   .. py:method:: load_data_to_pandas_df(self, file_path='/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv')


   .. py:method:: nodify_city_column(self, df)


   .. py:method:: nodify_states_column(self, df)


   .. py:method:: nodify_url_column(self, df)


   .. py:method:: nodify_country_column(self, df)



.. py:class:: NeoAPI

   .. py:method:: run_test_query(self)


   .. py:method:: instantiate_neo_sandbox_app(self)


   .. py:method:: instantiate_neo_aura_app(self)



.. py:class:: GoogleAPIS

   .. py:method:: load_google_creds(self)


   .. py:method:: instantiate_sheets_app(self)


   .. py:method:: instantiate_drive_app(self)



.. py:class:: SparkAPI

   .. py:method:: instantiate_spark_session(self)


   .. py:method:: load_spark_data_from_csv(self, file_path)



.. py:class:: neoModelAPI

   .. py:method:: instantiate_neo_model_session(self)


   .. py:method:: update(self, obj)



.. py:function:: instantiate_google_API()


.. py:function:: instantiate_spark_API()


.. py:function:: load_data_to_spark_df(sparkAPI)


.. py:function:: prepare_df_for_upload(df)


.. py:function:: load_data_to_pandas_df()


.. py:function:: prepare_pandas_df()


.. py:function:: instantiate_neo_model_api()


.. py:function:: upload_df_to_db(df, neo_model_api)


.. py:data:: neo_model_api
   

   

