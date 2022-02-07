:py:mod:`SupremeCourtPredictionsJustice`
========================================

.. py:module:: SupremeCourtPredictionsJustice


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   SupremeCourtPredictionsJustice.get_environmental_variables
   SupremeCourtPredictionsJustice.load_data
   SupremeCourtPredictionsJustice.split_datframe
   SupremeCourtPredictionsJustice.df_to_dataset
   SupremeCourtPredictionsJustice.get_input_pipeline
   SupremeCourtPredictionsJustice.get_feature_layer
   SupremeCourtPredictionsJustice.understand_input_pipeline
   SupremeCourtPredictionsJustice.create_model
   SupremeCourtPredictionsJustice.plot_history
   SupremeCourtPredictionsJustice.explain_kernal



Attributes
~~~~~~~~~~

.. autoapisummary::

   SupremeCourtPredictionsJustice.df


.. py:function:: get_environmental_variables()


.. py:function:: load_data(cwd)


.. py:function:: split_datframe(dataframe)


.. py:function:: df_to_dataset(dataframe, shuffle=True, batch_size=32)


.. py:function:: get_input_pipeline(train, test, val, batch_size=32, shuffle=True)


.. py:function:: get_feature_layer(cwd)


.. py:function:: understand_input_pipeline(train_ds)


.. py:function:: create_model(log_dir, feature_layer, train_ds, val_ds, epochs=8)


.. py:function:: plot_history(history)


.. py:function:: explain_kernal(model, train_ds)


.. py:data:: df
   

   

