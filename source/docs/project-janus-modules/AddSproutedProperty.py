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