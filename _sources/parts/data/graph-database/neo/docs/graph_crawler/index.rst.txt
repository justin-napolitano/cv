:py:mod:`graph_crawler`
=======================

.. py:module:: graph_crawler


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   graph_crawler.Realtor_Url_Data
   graph_crawler.Realtor_Search_URL
   graph_crawler.TO_PROCESS
   graph_crawler.IS_CHILD
   graph_crawler.IS_ROOT
   graph_crawler.IS_SIBLING
   graph_crawler.to_process_node_struct
   graph_crawler.id_label
   graph_crawler.UpdateGraph



Functions
~~~~~~~~~

.. autoapisummary::

   graph_crawler.instantiate_neo_driver
   graph_crawler.get_data_from_realtor_url
   graph_crawler.get_root_url
   graph_crawler.get_non_processed_node
   graph_crawler.create_friendship
   graph_crawler.create_url_list
   graph_crawler.update_graph
   graph_crawler.crawl_graph



Attributes
~~~~~~~~~~

.. autoapisummary::

   graph_crawler.neo_driver


.. py:function:: instantiate_neo_driver()


.. py:class:: Realtor_Url_Data(root_url)

   .. py:method:: create_url_list(self, max_it, root_url)


   .. py:method:: calculate_number_of_pages(self, data)


   .. py:method:: get_soup(self, real_url, response)


   .. py:method:: get_web_data(self, soup)


   .. py:method:: get_request(self, real_url, headers)



.. py:function:: get_data_from_realtor_url(url)


.. py:function:: get_root_url(neo_driver)


.. py:function:: get_non_processed_node(neo_driver)


.. py:function:: create_friendship(neo_driver)


.. py:function:: create_url_list(non_processed_node)


.. py:class:: Realtor_Search_URL(url, label, processed=False, is_root=False, is_child=False, is_parent=False, is_sibling=False)


.. py:class:: TO_PROCESS(priority=0)


.. py:class:: IS_CHILD(priority=0)


.. py:class:: IS_ROOT(priority=0)


.. py:class:: IS_SIBLING(priority=0)


.. py:class:: to_process_node_struct(label, type_property_of_node)


.. py:class:: id_label(id, label)


.. py:class:: UpdateGraph(neo_driver)

   .. py:method:: get_root_url(self)


   .. py:method:: create_url_list(self, non_processed_node)


   .. py:method:: set_node_to_sprouted(self, node, property, value)


   .. py:method:: create_node_struct(self, url, label, processed=False, is_root=False, is_child=False, is_parent=False, is_sibling=False)


   .. py:method:: create_relationship_last_to_current_node(self)


   .. py:method:: create_to_process_node_property_struct(self, label='To_Process')


   .. py:method:: get_to_process_node(self, node_property_struct, limit=1)


   .. py:method:: create_to_process_relationship_struct(self)


   .. py:method:: create_is_child_relationship(self)


   .. py:method:: create_is_root_relationship(self)


   .. py:method:: create_is_sibling_relationship(self)


   .. py:method:: create_id_struct_from_node(self, node)


   .. py:method:: create_relationship_by_id(self, node_1, node_2, relationship_struct, relationship_type=None)


   .. py:method:: add_node(self, node_struct, node_label)



.. py:function:: update_graph(neo_driver)


.. py:function:: crawl_graph()

   #find all ancestors and descendents
       MATCH (n:Node2)
       WITH n, [(n)<-[:Child*]-(x) | x] as ancestors,  [(x)<-[:Child*]-(n) | x] as descendants

       #find 1 parent and 1 child
       MATCH (n:Node2)
       WITH n, [(n)<-[:Child]-(x) | x][0] as parent,  [(x)<-[:Child]-(n) | x] as children
       RETURN n, parent, children
       RETURN n, ancestors, descendants

       #set state all descendents of root
       match (n:Realtor_Search_URL) where (n.is_root = True and n.sprouted = True and n.processed = False) return n limit 100
       match n [:IS_STATE_OF] -> (state)
       pull 100 url's at a time by state

       n:Realtor_Search_URL where n.processed = false
       match n -{'is_state_of'} ->[]

       n:Realtor_Search_URL related to to_process

       #create or stack??/ or just do it randomly?


.. py:data:: neo_driver
   

   

