:py:mod:`neoModelAPI`
=====================

.. py:module:: neoModelAPI


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   neoModelAPI.neoAPI
   neoModelAPI.Processed
   neoModelAPI.NotProcessed
   neoModelAPI.City
   neoModelAPI.Country
   neoModelAPI.State
   neoModelAPI.Root
   neoModelAPI.Child
   neoModelAPI.Parent
   neoModelAPI.Sibling
   neoModelAPI.Realtor_com
   neoModelAPI.Realtor_Search_URL
   neoModelAPI.Person




.. py:class:: neoAPI

   .. py:method:: instantiate_neo_model_session(self)


   .. py:method:: create_city_node(name)


   .. py:method:: create_country_node(code, name)


   .. py:method:: create_state_node(code, name)


   .. py:method:: create_realtor_search_url_node(url)


   .. py:method:: create_root_node(url, name='realtor.com')


   .. py:method:: create_child_node(url, name='realtor.com')


   .. py:method:: create_parent_node(url, name='realtor.com')


   .. py:method:: create_sibling_node(url, name='realtor.com')


   .. py:method:: create_relationship(source, target)


   .. py:method:: update(obj)



.. py:class:: Processed

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      


.. py:class:: NotProcessed

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      


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
      

      


.. py:class:: State

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: code
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: country
      

      


.. py:class:: Root

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: is_root
      

      

   .. py:attribute:: is_parent
      

      

   .. py:attribute:: is_sibling
      

      

   .. py:attribute:: is_child
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: url
      

      

   .. py:attribute:: processed
      

      

   .. py:attribute:: NotProcessed
      

      

   .. py:attribute:: sibling
      

      

   .. py:attribute:: child
      

      

   .. py:attribute:: parent
      

      

   .. py:attribute:: root
      

      


.. py:class:: Child

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: is_root
      

      

   .. py:attribute:: is_parent
      

      

   .. py:attribute:: is_sibling
      

      

   .. py:attribute:: is_child
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: processed
      

      

   .. py:attribute:: NotProcessed
      

      

   .. py:attribute:: sibling
      

      

   .. py:attribute:: child
      

      

   .. py:attribute:: parent
      

      

   .. py:attribute:: root
      

      


.. py:class:: Parent

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: is_root
      

      

   .. py:attribute:: is_parent
      

      

   .. py:attribute:: is_sibling
      

      

   .. py:attribute:: is_child
      

      

   .. py:attribute:: processed
      

      

   .. py:attribute:: NotProcessed
      

      

   .. py:attribute:: sibling
      

      

   .. py:attribute:: child
      

      

   .. py:attribute:: parent
      

      

   .. py:attribute:: root
      

      


.. py:class:: Sibling

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: is_root
      

      

   .. py:attribute:: is_parent
      

      

   .. py:attribute:: is_sibling
      

      

   .. py:attribute:: is_child
      

      

   .. py:attribute:: name
      

      

   .. py:attribute:: processed
      

      

   .. py:attribute:: NotProcessed
      

      

   .. py:attribute:: sibling
      

      

   .. py:attribute:: child
      

      

   .. py:attribute:: parent
      

      

   .. py:attribute:: root
      

      


.. py:class:: Realtor_com

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: is_realtor_com
      

      

   .. py:attribute:: name
      

      


.. py:class:: Realtor_Search_URL

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: url
      

      

   .. py:attribute:: searched
      

      

   .. py:attribute:: is_root
      

      

   .. py:attribute:: is_child
      

      

   .. py:attribute:: is_parent
      

      

   .. py:attribute:: is_sibling
      

      

   .. py:attribute:: state
      

      

   .. py:attribute:: city
      

      

   .. py:attribute:: root
      

      

   .. py:attribute:: child
      

      

   .. py:attribute:: parent
      

      

   .. py:attribute:: sibling
      

      

   .. py:attribute:: realtor_com
      

      

   .. py:attribute:: processed
      

      

   .. py:attribute:: NotProcessed
      

      


.. py:class:: Person

   Bases: :py:obj:`neomodel.StructuredNode`

   .. py:attribute:: uid
      

      

   .. py:attribute:: full_name
      

      

   .. py:attribute:: email
      

      


