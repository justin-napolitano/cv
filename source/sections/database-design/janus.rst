################################################
Janus Graph Python Library
################################################


Summary
----------
* An extension of the python-gremlin library. The API is designed to work well with pandas DataFrames.
* The collection of functions are written to permit an asynchronous df.apply() across n threads to mimic transaction functionality of spark df’s without the overhead of running a local Spark cluster.
* Runner applications are also included that create example city and zip code graphs

Links
------
`GitHub <https://github.com/justin-napolitano/JanusGraphAPI>`_

Gremlin Connect
----------------

Connects to the stack.

.. code-block:: python

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

Query
------

.. code-block:: python

    from GremlinConnect import GremlinConnection
    from PandasFunctions import PandasFunctions as PF
    from pprint import pprint
    import json


    def get_janus_graph_traversal(connection_driver):
        print("&&& Calling Gremlin Connect &&& ")
        gremlin_traversal= GremlinConnection.traversal_connection(connection_driver)
        print("&&& Gremlin is Lived  &&& ")
        return gremlin_traversal

    def get_janus_graph_connection_driver():
        host= '192.168.1.195'
        port = '8182'
        driver = GremlinConnection.connection_driver(host,port)
        print("&&& Gremlin is Alive  &&& ")
        return driver


    def query_graph_by_property_value(traversal,property,value):
        orlando_zip_codes = traversal.V().has(property, value).toList()
        pprint(orlando_zip_codes)

    def get_list_of_all_vertex(traversal):
        vertex_list = traversal.V().toList()
        #pprint(vertex_list)
        return vertex_list

    def get_list_of_all_vertex_by_label(traversal,label):
        vertex_list = traversal.V().hasLabel(label).toList()
        return vertex_list
        #pprint(vertex_list)



    def main():
        connection_driver = get_janus_graph_connection_driver()
        traversal = get_janus_graph_traversal(connection_driver)
        #query_graph_by_property_value(traversal = traversal, property = 'State', value= "FL")
        #et_list_of_all_vertex(traversal)
        get_list_of_all_vertex_by_label(traversal=traversal,label = 'city')
        connection_driver.close()



    if __name__ == "__main__":
        main()

Submit transaction
-------------------

.. code-block:: python

    #Application.python

    from GremlinConnect import GremlinConnection
    from PandasFunctions import PandasFunctions as PF
    from pprint import pprint
    import json
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


    def connect_to_janus_server():
        print("&&& Calling Gremlin Connect &&& ")
        host= '192.168.1.195'
        port = '8182'
        Gremlin = GremlinConnection.client_connection(host,port)
        print("&&& Gremlin is Lived  &&& ")
        return Gremlin

    def get_janus_graph_traversal(connection_driver):
        print("&&& Calling Gremlin Connect &&& ")
        gremlin_traversal= GremlinConnection.traversal_connection(connection_driver)
        print("&&& Gremlin is Lived  &&& ")
        return gremlin_traversal

    def get_janus_graph_connection_driver():
        host= '192.168.1.195'
        port = '8182'
        driver = GremlinConnection.connection_driver(host,port)
        print("&&& Gremlin is Alive  &&& ")
        return driver


    def add_vertex(traversal):
        vertex = traversal.addV('person').property('name', 'chris').next()
        print(vertex)
        #name = traversal.V().name.toList()
        name = traversal.V().values('name').toList()
        ##g.V().name.toList()
        return name

    def add_vertex_traversal(traversal, label, properties):
        vertex_traversal = GremlinConnection.add_vertex_traversal(traversal, label, properties)
        return vertex_traversal

    def add_zip_code_vertex(traversal):
        label = "zip_code"
    
        properties = {"zip_code": 800,
        "type": 'standard',
        "primary_city": 'example',
        "state": 'hickerton',
        "county":'bitch town',
        'timezone': 'middle_of_nowhere', 
        'area_codes':333,
        'world_region': 'USA FUCK YEAH',
        "country": 'USA USA USA',
        'latitude': 'up your',
        'longitude': 'your butt',
        'population_2015': 69
        }
        vertex = traversal.addV(label).property(properties)
        vertex.next()
        print(vertex)
        return vertex
        

    def get_value_map(traversal):
        value_map = traversal.V().valueMap().toList()
        print(value_map)

    def load_zip_code_df():
        zip_code_df = PF.Load.csv_to_df('zip_code_db.csv')
        #pprint(zip_code_df)
        return zip_code_df

    def create_traversal_df(zip_code_df,traversal):
        #zip_code_df['traversal'] = zip_code_df.apply(lambda x: print(x['vertice_property']), axis = 1) inject_vertex_properties(traversal,properties,label):
        zip_code_df['traversal'] = zip_code_df.apply(lambda x: inject_vertex_properties(traversal = traversal, label = 'zip', properties = x['vertice_property']),axis= 1)
        #pprint(zip_code_df)
        return zip_code_df

    def submit_traversal(traversal_df):
        #pprint(traversal_df['traversal'])
        traversal_df['vertex_submission'] = traversal_df.apply(lambda x: x['traversal'].next(), axis = 1)
        return traversal_df

    def close_connection(connection_driver):
        connection_driver.close()

    def inject_vertex_properties(traversal,properties,label):
        vertex = GremlinConnection.inject_vertex_properties(traversal,properties,label)
        return vertex
    def transaction_injection_vertex_properties(traversal, zip_code_df):
        zip_code_df['traversal'] = zip_code_df.apply(lambda x: inject_vertex_properties(traversal = traversal, label = 'zip', properties = x['vertice_property']),axis= 1)
        #pprint(zip_code_df)
        return zip_code_df

        
    def main():
        zip_code_df = load_zip_code_df()
        #test = json.loads(zip_code_df['vertice_property'][0])
        #pprint(test)
        connection_driver = get_janus_graph_connection_driver()
        traversal = get_janus_graph_traversal(connection_driver)
        #vertex = inject_vertex_properties(traversal,test,'zip_code')
        #pprint(vertex)
        #pprint(traversal)
        #vertex_traversal_test = add_vertex_traversal(traversal= traversal, label='zip', properties = test)
        #vertex_traversal_test = transaction_injection_vertex_properties(traversal= traversal, zip_code_df= zip_code_df)
        #pprint(vertex_traversal_test)
        #vertex = add_zip_code_vertex(traversal)
        #vertex.next()
        #pprint(vertex)
        
        #pprint(zip_code_df)
        #connection_driver = get_janus_graph_connection_driver()
        
        #traversal = get_janus_graph_traversal(connection_driver)
        
        traversal_df = create_traversal_df(zip_code_df=zip_code_df, traversal=traversal)
        pprint(traversal_df)
        #pprint(traversal_df['traversal'][0])
        #pprint(traversal_df['traversal'][1].next())
        #pprint(traversal_df['traversal'][1].next())
        submit_df = submit_traversal(traversal_df)
        pprint(submit_df)
        #pprint(submit_df)
        #pprint(traversal_df)


        #print(traversal)
        #vertex_added = add_zip_code_vertex(traversal)
        #vertex_added = add_vertex(traversal)
        #print(vertex_added)
        #get_value_map(traversal)
        #closed_connection = close_connection(connection_driver)
        #mgmt = Gremlin.graph.openManagement()
        #mgmt.printSchema()
        connection_driver.close()


    if __name__ == "__main__":
        main()


Add Root
---------

Adds a root property to the graph.

.. code-block:: python

    #add_is_root_property.py

    from Query import get_list_of_all_vertex_by_label as get_vertex
    from GremlinConnect import GremlinConnection
    from pprint import pprint
    import json

    def get_list(traversal, label):
        vertex_list = get_vertex(traversal, label)
        return vertex_list

    def get_janus_graph_traversal(connection_driver):
        print("&&& Calling Gremlin Connect &&& ")
        gremlin_traversal= GremlinConnection.traversal_connection(connection_driver)
        print("&&& Gremlin is Lived  &&& ")
        return gremlin_traversal

    def get_janus_graph_connection_driver():
        host= '192.168.1.195'
        port = '8182'
        driver = GremlinConnection.connection_driver(host,port)
        print("&&& Gremlin is Alive  &&& ")
        return driver

    def add_is_root_property(traversal,list):
        for vertex in list:
            submission = traversal.V(vertex.id).property("is_root", True).iterate()
            print("1 done")
        print('done')

    def main():
        connection_driver = get_janus_graph_connection_driver()
        traversal = get_janus_graph_traversal(connection_driver)
        list = get_list(traversal = traversal, label = 'city')
        add_is_root_property(traversal=traversal, list = list)
        connection_driver.close()


    if __name__ == "__main__":
        main()


Add Children to Root
---------------------

.. code-block:: python
 
    #AddChildrenToRoot

    from GremlinConnect import GremlinConnection
    from pprint import pprint

    def return_arbitrary_root_object(traversal):
        arbitrary_root = traversal.V().hasLabel('zip').elementMap().limit(1).next()
        pprint(arbitrary_root)

        #arbitrary_root = traversal.V().hasLabel('city','state').has('is_root', True).has('sprouted', False).limit(1).next()
        return arbitrary_root
        #
        # 
        #pprint(arbitrary_root)

    def return_arbitrary_root_element_map(traversal):
        arbitrary_root = traversal.V().hasLabel('city').has('is_root', True).has('sprouted', False).limit(1).next()
        return arbitrary_root
        #
        # 
        #pprint(arbitrary_root)
    def find_children_urls(root_url):
            root_url = root_url.replace("'" , "")
            data = Realtor_Url_Data(root_url)
            #pprint(data.url_list)
            return data.url_list


    def get_janus_graph_traversal(connection_driver):
        print("&&& Calling Gremlin Connect &&& ")
        gremlin_traversal= GremlinConnection.traversal_connection(connection_driver)
        print("&&& Gremlin is Lived  &&& ")
        return gremlin_traversal

    def get_janus_graph_connection_driver():
        host= '192.168.1.195'
        port = '8182'
        driver = GremlinConnection.connection_driver(host,port)
        print("&&& Gremlin is Alive  &&& ")
        return driver





    def main():
        connection_driver = get_janus_graph_connection_driver()
        traversal = get_janus_graph_traversal(connection_driver)
        arbitrary_root = return_arbitrary_root_object(traversal)
        #pprint(arbitrary_root)
        #pprint(dir(arbitrary_root))
        #root_url = arbitrary_root_url

        connection_driver.close()


    if __name__ == "__main__":
        main()

Add Sprouted Property
----------------------
Adds a utility isSprouted property to root nodes

.. code-block:: python

    #add_is_root_property.py

    from Query import get_list_of_all_vertex_by_label as get_vertex
    from GremlinConnect import GremlinConnection
    from pprint import pprint
    import json
    import PandasFunctions as PF

    def get_list(traversal, label):
        vertex_list = get_vertex(traversal, label)
        return vertex_list

    def get_janus_graph_traversal(connection_driver):
        print("&&& Calling Gremlin Connect &&& ")
        gremlin_traversal= GremlinConnection.traversal_connection(connection_driver)
        print("&&& Gremlin is Lived  &&& ")
        return gremlin_traversal

    def get_janus_graph_connection_driver():
        host= '192.168.1.195'
        port = '8182'
        driver = GremlinConnection.connection_driver(host,port)
        print("&&& Gremlin is Alive  &&& ")
        return driver

    def add_sprouted_property(traversal,list):
        df = PF.PandasFunctions.Load.create_empty_df()
        df['vertices'] = list 
        df['traversals'] = df.apply(lambda x: traversal.V(x['vertices'].id).property('sprouted',False).iterate(), axis = 1)
        print('done')

    def main():
        connection_driver = get_janus_graph_connection_driver()
        traversal = get_janus_graph_traversal(connection_driver)
        list = get_list(traversal = traversal, label = 'city')
        add_sprouted_property(traversal=traversal, list = list)
        connection_driver.close()


    if __name__ == "__main__":
        main()

Clear Graph
------------------

Clears the Graph

.. code-block:: python
    
    from GremlinConnect import GremlinConnection
    from PandasFunctions import PandasFunctions as PF
    from pprint import pprint
    import json


    def get_janus_graph_traversal(connection_driver):
        print("&&& Calling Gremlin Connect &&& ")
        gremlin_traversal= GremlinConnection.traversal_connection(connection_driver)
        print("&&& Gremlin is Lived  &&& ")
        return gremlin_traversal

    def get_janus_graph_connection_driver():
        host= '192.168.1.195'
        port = '8182'
        driver = GremlinConnection.connection_driver(host,port)
        print("&&& Gremlin is Alive  &&& ")
        return driver


    def delete_all_vertex(traversal):
        traversal.V().drop().iterate()
    




    def main():
        connection_driver = get_janus_graph_connection_driver()
        traversal = get_janus_graph_traversal(connection_driver)
        delete_all_vertex(traversal=traversal)
        connection_driver.close()



    if __name__ == "__main__":
        main()


Zip Code DB Runner Application
-------------------------------

.. code-block:: python

    #Application.python

    from GremlinConnect import GremlinConnection
    from PandasFunctions import PandasFunctions as PF
    from pprint import pprint
    import json
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


    def connect_to_janus_server():
        print("&&& Calling Gremlin Connect &&& ")
        host= '192.168.1.195'
        port = '8182'
        Gremlin = GremlinConnection.client_connection(host,port)
        print("&&& Gremlin is Lived  &&& ")
        return Gremlin

    def get_janus_graph_traversal(connection_driver):
        print("&&& Calling Gremlin Connect &&& ")
        gremlin_traversal= GremlinConnection.traversal_connection(connection_driver)
        print("&&& Gremlin is Lived  &&& ")
        return gremlin_traversal

    def get_janus_graph_connection_driver():
        host= '192.168.1.195'
        port = '8182'
        driver = GremlinConnection.connection_driver(host,port)
        print("&&& Gremlin is Alive  &&& ")
        return driver


    def add_vertex(traversal):
        vertex = traversal.addV('person').property('name', 'chris').next()
        print(vertex)
        #name = traversal.V().name.toList()
        name = traversal.V().values('name').toList()
        ##g.V().name.toList()
        return name

    def add_vertex_traversal(traversal, label, properties):
        vertex_traversal = GremlinConnection.add_vertex_traversal(traversal, label, properties)
        return vertex_traversal

    def add_zip_code_vertex(traversal):
        label = "zip_code"
    
        properties = {"zip_code": 800,
        "type": 'standard',
        "primary_city": 'example',
        "state": 'hickerton',
        "county":'bitch town',
        'timezone': 'middle_of_nowhere', 
        'area_codes':333,
        'world_region': 'USA FUCK YEAH',
        "country": 'USA USA USA',
        'latitude': 'up your',
        'longitude': 'your butt',
        'population_2015': 69
        }
        vertex = traversal.addV(label).property(properties)
        vertex.next()
        print(vertex)
        return vertex
        

    def get_value_map(traversal):
        value_map = traversal.V().valueMap().toList()
        print(value_map)

    def load_zip_code_df():
        zip_code_df = PF.Load.csv_to_df('zip_code_db.csv')
        #pprint(zip_code_df)
        return zip_code_df

    def create_traversal_df(zip_code_df,traversal):
        #zip_code_df['traversal'] = zip_code_df.apply(lambda x: print(x['vertice_property']), axis = 1) inject_vertex_properties(traversal,properties,label):
        zip_code_df['traversal'] = zip_code_df.apply(lambda x: inject_vertex_properties(traversal = traversal, label = 'zip.', properties = json.loads(x['vertice_property'])),axis= 1)
        #pprint(zip_code_df)
        return zip_code_df

    def submit_traversal(traversal_df):
        #pprint(traversal_df['traversal'])
        traversal_df['vertex_submission'] = traversal_df.apply(lambda x: x['traversal'].iterate(), axis = 1)
        return traversal_df

    def close_connection(connection_driver):
        connection_driver.close()

    def inject_vertex_properties(traversal,properties,label):
        vertex = GremlinConnection.inject_vertex_properties(traversal,properties,label)
        return vertex


    def main():
        zip_code_df = load_zip_code_df()
        connection_driver = get_janus_graph_connection_driver()
        traversal = get_janus_graph_traversal(connection_driver)
        traversal_df = create_traversal_df(zip_code_df=zip_code_df, traversal=traversal)
        pprint(traversal_df)
        submit_df = submit_traversal(traversal_df)
        pprint(submit_df)
        connection_driver.close()



    if __name__ == "__main__":
        main()
