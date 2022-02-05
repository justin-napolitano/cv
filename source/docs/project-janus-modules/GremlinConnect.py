from gremlin_python import statics
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Order
from gremlin_python.process.traversal import Cardinality
from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
from gremlin_python.process.traversal import Operator
from gremlin_python.process.traversal import P
from gremlin_python.process.traversal import Pop
from gremlin_python.process.traversal import Scope
from gremlin_python.process.traversal import Barrier
from gremlin_python.process.traversal import Bindings
from gremlin_python.process.traversal import WithOptions
from gremlin_python.driver import client 
from gremlin_python.process.graph_traversal import select
from gremlin_python.process.graph_traversal import property





class GremlinConnection:

    def inject_vertex_properties(traversal,properties,label):
        try:
            vertex = traversal.inject(properties).unfold().as_('properties')\
            .addV(label).as_('vertex')\
            .sideEffect(
                select('properties').unfold().as_('kv')
                .select('vertex')
                .property(select('kv').by(Column.keys), select('kv').by(Column.values)))
        except Exception as e:
            raise e
        return vertex

    def gtx_inject_vertex_properties(gtx,properties,label):
        try:
            vertex = gtx.inject(properties).unfold().as_('properties')\
            .addV(label).as_('vertex')\
            .sideEffect(
                select('properties').unfold().as_('kv')
                .select('vertex')
                .property(select('kv').by(Column.keys), select('kv').by(Column.values)))
        except Exception as e:
            raise e
        return vertex


    def connection_driver(host,port):
        connection_driver = GremlinConnection._connection_driver(host,port)
        return connection_driver


    def _connection_driver(host,port):
        connect_string = f'ws://{host}:{port}/gremlin'

        try: 
            connection_driver = DriverRemoteConnection(connect_string, 'g')

        except Exception as e:
            raise e

        return connection_driver

    def add_vertex_traversal(traversal, label, properties):

        #This is not commited!!! call next() on what is returned to right to the graph
        vertex = traversal.addV(label).property(properties)
        return vertex
    
    def client_connection(host,port):
        client = GremlinConnection._client_connection(host,port)
        return client

    
    @staticmethod
    def _client_connection(host,port):
        connect_string = f'ws://{host}:{port}/gremlin'
        try: 
            client_ = client.Client('ws://localhost:8182/gremlin', 'g')
            # The connection should be closed on shut down to close open connections with connection.close()
            #g = traversal().withRemote(connection)
        except Exception as e:
            raise e
       
        return client_

    def traversal_connection(connection):

        gremlin = GremlinConnection._traversal_connection(connection)
        return gremlin
    @staticmethod
    def _traversal_connection(connection):
        #connect_string = f'ws://{host}:{port}/gremlin'
        try: 
            #connection = DriverRemoteConnection(connect_string, 'g')
            # The connection should be closed on shut down to close open connections with connection.close()
            g = traversal().withRemote(connection)
        except Exception as e:
            raise e
       
        return g
        # Reuse 'g' across the application  