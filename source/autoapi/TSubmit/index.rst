:py:mod:`TSubmit`
=================

.. py:module:: TSubmit


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   TSubmit.connect_to_janus_server
   TSubmit.get_janus_graph_traversal
   TSubmit.get_janus_graph_connection_driver
   TSubmit.add_vertex
   TSubmit.add_vertex_traversal
   TSubmit.add_zip_code_vertex
   TSubmit.get_value_map
   TSubmit.load_zip_code_df
   TSubmit.create_traversal_df
   TSubmit.submit_traversal
   TSubmit.close_connection
   TSubmit.inject_vertex_properties
   TSubmit.transaction_injection_vertex_properties
   TSubmit.main



.. py:function:: connect_to_janus_server()


.. py:function:: get_janus_graph_traversal(connection_driver)


.. py:function:: get_janus_graph_connection_driver()


.. py:function:: add_vertex(traversal)


.. py:function:: add_vertex_traversal(traversal, label, properties)


.. py:function:: add_zip_code_vertex(traversal)


.. py:function:: get_value_map(traversal)


.. py:function:: load_zip_code_df()


.. py:function:: create_traversal_df(zip_code_df, traversal)


.. py:function:: submit_traversal(traversal_df)


.. py:function:: close_connection(connection_driver)


.. py:function:: inject_vertex_properties(traversal, properties, label)


.. py:function:: transaction_injection_vertex_properties(traversal, zip_code_df)


.. py:function:: main()


