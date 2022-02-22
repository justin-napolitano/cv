:py:mod:`SupremeCourtPredictionsJustice`
========================================

.. py:module:: SupremeCourtPredictionsJustice
   :noindex:

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

.. py:function:: create_model(log_dir, feature_layer, train_ds, val_ds, epochs=8)
   :noindex:

.. py:function:: plot_history(history)
   :noindex:

.. py:function:: explain_kernal(model, train_ds)
   :noindex:

.. py:data:: df
   :noindex:   

   

