:py:mod:`SupremeCourtPredictionsCase`
=====================================

.. py:module:: SupremeCourtPredictionsCase


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


.. py:function:: load_data(cwd)


.. py:function:: split_datframe(dataframe)


.. py:function:: df_to_dataset(dataframe, shuffle=True, batch_size=32)


.. py:function:: get_input_pipeline(train, test, val, batch_size=32, shuffle=True)


.. py:function:: get_feature_layer(cwd)


.. py:function:: understand_input_pipeline(train_ds)


.. py:function:: create_model(log_dir, feature_layer, train_ds, val_ds, epochs=5)


.. py:function:: plot_history(history)


.. py:function:: explain_kernal(df_train, model, train_ds)


.. py:data:: df
   

   

