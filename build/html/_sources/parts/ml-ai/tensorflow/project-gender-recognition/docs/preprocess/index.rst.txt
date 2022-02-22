:py:mod:`preprocess`
====================

.. py:module:: preprocess


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   preprocess.main
   preprocess.preprocess_image
   preprocess._process_image
   preprocess._buffer_image
   preprocess._align_image



Attributes
~~~~~~~~~~

.. autoapisummary::

   preprocess.logger
   preprocess.align_dlib
   preprocess.input_directory


.. py:data:: logger
   

   

.. py:data:: align_dlib
   

   

.. py:function:: main(input_dir, output_dir, crop_dim)


.. py:function:: preprocess_image(input_path, output_path, crop_dim)

   Detect face, align and crop :param input_path. Write output to :param output_path
   :param input_path: Path to input image
   :param output_path: Path to write processed image
   :param crop_dim: dimensions to crop image to


.. py:function:: _process_image(filename, crop_dim)


.. py:function:: _buffer_image(filename)


.. py:function:: _align_image(image, crop_dim)


.. py:data:: input_directory
   :annotation: = C:\Users\jnapolitano\OneDrive\Cox Oil\Cox_Oil_JNAP_Branch\Facial_Recognition\medium-facenet-tutorial\Data

   

