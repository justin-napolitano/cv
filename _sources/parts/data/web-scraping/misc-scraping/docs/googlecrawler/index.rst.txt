:py:mod:`googlecrawler`
=======================

.. py:module:: googlecrawler


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   googlecrawler.configure_logging
   googlecrawler.get_soup
   googlecrawler.get_query_url
   googlecrawler.extract_images_from_soup
   googlecrawler.extract_images
   googlecrawler.get_raw_image
   googlecrawler.save_image
   googlecrawler.download_images_to_dir
   googlecrawler.run
   googlecrawler.main



Attributes
~~~~~~~~~~

.. autoapisummary::

   googlecrawler.logger
   googlecrawler.REQUEST_HEADER


.. py:function:: configure_logging()


.. py:data:: logger
   

   

.. py:data:: REQUEST_HEADER
   

   

.. py:function:: get_soup(url, header)


.. py:function:: get_query_url(query)


.. py:function:: extract_images_from_soup(soup)


.. py:function:: extract_images(query, num_images)


.. py:function:: get_raw_image(url)


.. py:function:: save_image(raw_image, image_type, save_directory)


.. py:function:: download_images_to_dir(images, save_directory, num_images)


.. py:function:: run(query, save_directory, num_images=100)


.. py:function:: main()


