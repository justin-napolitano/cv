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