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