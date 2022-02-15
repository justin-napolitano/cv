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