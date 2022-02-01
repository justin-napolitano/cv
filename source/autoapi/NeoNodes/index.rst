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




.. py:class:: City(*args, **kwargs)

   Bases: :py:obj:`neomodel.StructuredNode`

   Base class for all node definitions to inherit from.

   If you want to create your own abstract classes set:
       __abstract_node__ = True

   .. py:attribute:: uid
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: state
      

      

   .. py:attribute:: country
      

      


.. py:class:: Country(*args, **kwargs)

   Bases: :py:obj:`neomodel.StructuredNode`

   Base class for all node definitions to inherit from.

   If you want to create your own abstract classes set:
       __abstract_node__ = True

   .. py:attribute:: uid
      

      

   .. py:attribute:: code
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: state
      

      


.. py:class:: State(*args, **kwargs)

   Bases: :py:obj:`neomodel.StructuredNode`

   Base class for all node definitions to inherit from.

   If you want to create your own abstract classes set:
       __abstract_node__ = True

   .. py:attribute:: uid
      

      

   .. py:attribute:: code
      

      

   .. py:attribute:: name
      

      


.. py:class:: URL(*args, **kwargs)

   Bases: :py:obj:`neomodel.StructuredNode`

   Base class for all node definitions to inherit from.

   If you want to create your own abstract classes set:
       __abstract_node__ = True

   .. py:attribute:: uid
      

      

   .. py:attribute:: url
      

      

   .. py:attribute:: searched
      

      

   .. py:attribute:: state
      

      

   .. py:attribute:: city
      

      


.. py:class:: Person(*args, **kwargs)

   Bases: :py:obj:`neomodel.StructuredNode`

   Base class for all node definitions to inherit from.

   If you want to create your own abstract classes set:
       __abstract_node__ = True

   .. py:attribute:: uid
      

      

   .. py:attribute:: full_name
      

      

   .. py:attribute:: email
      

      


