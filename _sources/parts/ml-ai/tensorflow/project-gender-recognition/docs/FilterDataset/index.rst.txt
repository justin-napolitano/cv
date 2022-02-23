:py:mod:`FilterDataset`
=======================

.. py:module:: FilterDataset


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   FilterDataset.ImageClass



Functions
~~~~~~~~~

.. autoapisummary::

   FilterDataset.get_dataset
   FilterDataset.filter_dataset
   FilterDataset.clean_directory
   FilterDataset.validate_dataset
   FilterDataset.test_dateset
   FilterDataset.validate_data



Attributes
~~~~~~~~~~

.. autoapisummary::

   FilterDataset.logger
   FilterDataset.parser


.. py:data:: logger
   

   

.. py:function:: get_dataset(input_directory)


.. py:function:: filter_dataset(dataset, min_images_per_label=10)


.. py:function:: clean_directory(input_dir, dataset, out_dir)


.. py:function:: validate_dataset(dataset, input_dir, output_dir)


.. py:function:: test_dateset(dataset, good_dir, test_dir, validate_dir, input_dir)


.. py:class:: ImageClass(name, image_paths)

   .. py:method:: __str__(self)

      Return str(self).


   .. py:method:: __len__(self)



.. py:function:: validate_data(input_directory)


.. py:data:: parser
   

   

