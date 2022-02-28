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

"""
adds a test traversal vertex.  of type person and properties of name chris.  I retain this function for usage examples
"""
def add_vertex(traversal):
    vertex = traversal.addV('person').property('name', 'chris').next()
    print(vertex)
    #name = traversal.V().name.toList()
    name = traversal.V().values('name').toList()
    ##g.V().name.toList()
    return name

"""
actually adds teh vertex to the graph via the gremlinconnection object. 
"""
def add_vertex_traversal(traversal, label, properties):
    vertex_traversal = GremlinConnection.add_vertex_traversal(traversal, label, properties)
    return vertex_traversal

"""
creates a zip code vertex records that is sent to df
"""
def add_zip_code_vertex(traversal):
    label = "zip_code"
   
    properties = {"zip_code": 901,
     "type": 'standard',
     "primary_city": 'example',
      "state": 'middle',
      "county":'nowhere',
      'timezone': 'middle_of_nowhere', 
      'area_codes':333,
      'world_region': 'USA',
      "country": 'USA USA USA',
      'latitude': 'over',
      'longitude': 'there',
      'population_2015': 72
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