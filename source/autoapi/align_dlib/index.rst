:py:mod:`align_dlib`
====================

.. py:module:: align_dlib

.. autoapi-nested-parse::

   Module for dlib-based alignment.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   align_dlib.AlignDlib




Attributes
~~~~~~~~~~

.. autoapisummary::

   align_dlib.TEMPLATE
   align_dlib.INV_TEMPLATE
   align_dlib.MINMAX_TEMPLATE


.. py:data:: TEMPLATE
   

   

.. py:data:: INV_TEMPLATE
   

   

.. py:data:: MINMAX_TEMPLATE
   

   

.. py:class:: AlignDlib(facePredictor)

   Use `dlib's landmark estimation <http://blog.dlib.net/2014/08/real-time-face-pose-estimation.html>`_ to align faces.

   The alignment preprocess faces for input into a neural network.
   Faces are resized to the same size (such as 96x96) and transformed
   to make landmarks (such as the eyes and nose) appear at the same
   location on every image.

   Normalized landmarks:

   .. image:: ../images/dlib-landmark-mean.png

   .. py:attribute:: INNER_EYES_AND_BOTTOM_LIP
      :annotation: = [39, 42, 57]

      

   .. py:attribute:: OUTER_EYES_AND_NOSE
      :annotation: = [36, 45, 33]

      

   .. py:method:: getAllFaceBoundingBoxes(self, rgbImg)

      Find all face bounding boxes in an image.

      :param rgbImg: RGB image to process. Shape: (height, width, 3)
      :type rgbImg: numpy.ndarray
      :return: All face bounding boxes in an image.
      :rtype: dlib.rectangles


   .. py:method:: getLargestFaceBoundingBox(self, rgbImg, skipMulti=False)

      Find the largest face bounding box in an image.

      :param rgbImg: RGB image to process. Shape: (height, width, 3)
      :type rgbImg: numpy.ndarray
      :param skipMulti: Skip image if more than one face detected.
      :type skipMulti: bool
      :return: The largest face bounding box in an image, or None.
      :rtype: dlib.rectangle


   .. py:method:: findLandmarks(self, rgbImg, bb)

      Find the landmarks of a face.

      :param rgbImg: RGB image to process. Shape: (height, width, 3)
      :type rgbImg: numpy.ndarray
      :param bb: Bounding box around the face to find landmarks for.
      :type bb: dlib.rectangle
      :return: Detected landmark locations.
      :rtype: list of (x,y) tuples


   .. py:method:: align(self, imgDim, rgbImg, bb=None, landmarks=None, landmarkIndices=INNER_EYES_AND_BOTTOM_LIP, skipMulti=False, scale=1.0)

      align(imgDim, rgbImg, bb=None, landmarks=None, landmarkIndices=INNER_EYES_AND_BOTTOM_LIP)

      Transform and align a face in an image.

      :param imgDim: The edge length in pixels of the square the image is resized to.
      :type imgDim: int
      :param rgbImg: RGB image to process. Shape: (height, width, 3)
      :type rgbImg: numpy.ndarray
      :param bb: Bounding box around the face to align. \
                 Defaults to the largest face.
      :type bb: dlib.rectangle
      :param landmarks: Detected landmark locations. \
                        Landmarks found on `bb` if not provided.
      :type landmarks: list of (x,y) tuples
      :param landmarkIndices: The indices to transform to.
      :type landmarkIndices: list of ints
      :param skipMulti: Skip image if more than one face detected.
      :type skipMulti: bool
      :param scale: Scale image before cropping to the size given by imgDim.
      :type scale: float
      :return: The aligned RGB image. Shape: (imgDim, imgDim, 3)
      :rtype: numpy.ndarray



