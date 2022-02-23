:py:mod:`SupremeCourtPredictionsCase`
=====================================

.. py:module:: SupremeCourtPredictionsCase
   :noindex:


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   SupremeCourtPredictionsCase.get_environmental_variables
   SupremeCourtPredictionsCase.load_data
   SupremeCourtPredictionsCase.split_datframe
   SupremeCourtPredictionsCase.df_to_dataset
   SupremeCourtPredictionsCase.get_input_pipeline
   SupremeCourtPredictionsCase.get_feature_layer
   SupremeCourtPredictionsCase.understand_input_pipeline
   SupremeCourtPredictionsCase.create_model
   SupremeCourtPredictionsCase.plot_history
   SupremeCourtPredictionsCase.explain_kernal


Attributes
~~~~~~~~~~

.. autoapisummary::

   SupremeCourtPredictionsCase.df


.. py:function:: get_environmental_variables()
   :noindex:


.. py:function:: load_data(cwd)
   :noindex:

.. py:function:: split_datframe(dataframe)
   :noindex:

.. py:function:: df_to_dataset(dataframe, shuffle=True, batch_size=32)
   :noindex:

.. py:function:: get_input_pipeline(train, test, val, batch_size=32, shuffle=True)
   :noindex:

.. py:function:: get_feature_layer(cwd)
   :noindex:

.. py:function:: understand_input_pipeline(train_ds)
   :noindex:

.. py:function:: create_model(log_dir, feature_layer, train_ds, val_ds, epochs=5)
   :noindex:

.. py:function:: plot_history(history)
   :noindex:

.. py:function:: explain_kernal(df_train, model, train_ds)
   :noindex:

.. py:data:: df
   :noindex:   

   

