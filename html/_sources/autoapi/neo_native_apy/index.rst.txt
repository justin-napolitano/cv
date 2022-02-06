:py:mod:`neo_native_apy`
========================

.. py:module:: neo_native_apy


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   neo_native_apy.NeoSandboxApp
   neo_native_apy.NeoApp




Attributes
~~~~~~~~~~

.. autoapisummary::

   neo_native_apy.uri


.. py:class:: NeoSandboxApp(bolt, user, password)

   .. py:method:: run_test_query(self)


   .. py:method:: set_property_by_id(self, id_label_obj, property, value)


   .. py:method:: _set_property_by_id(tx, id_label_obj, property, value)
      :staticmethod:


   .. py:method:: create_relationship_by_id(self, id_label_obj_1, id_label_obj_2, relationship_struct, relationship_type)


   .. py:method:: _create_relationship_by_id(tx, id_label_obj_1, id_label_obj_2, relationship_struct, relationship_type)
      :staticmethod:


   .. py:method:: return_root_url(self, search_string)


   .. py:method:: _match_and_return_search_url(tx, search_url)
      :staticmethod:


   .. py:method:: create_relationship(self, node_1, node_2, relationship_struct)


   .. py:method:: _create_relationship(tx, node_1, node_2, relationship_struct)
      :staticmethod:


   .. py:method:: add_node(self, node_struct, node_label)


   .. py:method:: _add_node(tx, node_struct, node_label)
      :staticmethod:


   .. py:method:: return_to_process_stack_node(self, node_property_struct, limit=1)


   .. py:method:: _match_and_return_node(tx, node_property_struct, common_label, limit)
      :staticmethod:


   .. py:method:: return_node_related_to_node(self, node_1, relation_to, node_2, limit)


   .. py:method:: _match_and_return_related_node(tx, node_1, relation_to, node_2, limit)
      :staticmethod:


   .. py:method:: create_friendship(self, person1_name, person2_name)


   .. py:method:: _create_and_return_friendship(tx, person1_name, person2_name)
      :staticmethod:


   .. py:method:: find_person(self, person_name)


   .. py:method:: _find_and_return_person(tx, person_name)
      :staticmethod:


   .. py:method:: close(self)



.. py:class:: NeoApp(uri, user, password)

   .. py:method:: close(self)


   .. py:method:: create_friendship(self, person1_name, person2_name)


   .. py:method:: _create_and_return_friendship(tx, person1_name, person2_name)
      :staticmethod:


   .. py:method:: find_person(self, person_name)


   .. py:method:: _find_and_return_person(tx, person_name)
      :staticmethod:


   .. py:method:: query(self, query, parameters=None, db=None)



.. py:data:: uri
   :annotation: = neo4j+s://b121e108.databases.neo4j.io

   

