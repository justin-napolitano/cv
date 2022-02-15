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
    """
    Adds vertices to a df that are then uploaded to janus graph via transactions asynchronously. 
    """
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