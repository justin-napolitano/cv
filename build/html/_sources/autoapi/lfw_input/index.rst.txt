:py:mod:`lfw_input`
===================

.. py:module:: lfw_input


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   lfw_input.ImageClass



Functions
~~~~~~~~~

.. autoapisummary::

   lfw_input.read_data
   lfw_input.read_image_from_disk
   lfw_input.get_image_paths_and_labels
   lfw_input.get_dataset
   lfw_input.filter_dataset
   lfw_input.split_dataset



Attributes
~~~~~~~~~~

.. autoapisummary::

   lfw_input.logger


.. py:data:: logger
   

   

.. py:function:: read_data(image_paths, label_list, image_size, batch_size, max_nrof_epochs, num_threads, shuffle, random_flip, random_brightness, random_contrast)

   Creates Tensorflow Queue to batch load images. Applies transformations to images as they are loaded.
   :param random_brightness:
   :param random_flip:
   :param image_paths: image paths to load
   :param label_list: class labels for image paths
   :param image_size: size to resize images to
   :param batch_size: num of images to load in batch
   :param max_nrof_epochs: total number of epochs to read through image list
   :param num_threads: num threads to use
   :param shuffle: Shuffle images
   :param random_flip: Random Flip image
   :param random_brightness: Apply random brightness transform to image
   :param random_contrast: Apply random contrast transform to image
   :return: images and labels of batch_size


.. py:function:: read_image_from_disk(filename_to_label_tuple)

   Consumes input tensor and loads image
   :param filename_to_label_tuple:
   :type filename_to_label_tuple: list
   :return: tuple of image and label


.. py:function:: get_image_paths_and_labels(dataset)


.. py:function:: get_dataset(input_directory)


.. py:function:: filter_dataset(dataset, min_images_per_label=10)


.. py:function:: split_dataset(dataset, split_ratio=0.8)


.. py:class:: ImageClass(name, image_paths)

   .. py:method:: __str__(self)

      Return str(self).


   .. py:method:: __len__(self)



