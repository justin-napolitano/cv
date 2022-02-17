:py:mod:`NeoNodes`
==================

.. py:module:: NeoNodes


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   NeoNodes.City
   NeoNodes.Country
   NeoNodes.State
   NeoNodes.URL
   NeoNodes.Person




.. py:class:: City

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: state
      

      

   .. py:attribute:: country
      

      


.. py:class:: Country

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: code
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: state
      

      


.. py:class:: State

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: code
      

      

   .. py:attribute:: name
      

      


.. py:class:: URL

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: url
      

      

   .. py:attribute:: searched
      

      

   .. py:attribute:: state
      

      

   .. py:attribute:: city
      

      


.. py:class:: Person

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: full_name
      

      

   .. py:attribute:: email
      

      


