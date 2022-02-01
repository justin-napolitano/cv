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