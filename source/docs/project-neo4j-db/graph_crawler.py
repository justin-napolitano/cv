#graph_crawler.py

#from py2neo import Graph
from logging import root
import neo_native_apy as neo
import requests
from bs4 import BeautifulSoup
import lxml.etree as etree
import xml.etree.ElementTree as ET
import json
import pandas as pd
from pprint import pprint
import math


def instantiate_neo_driver():
    bolt = "bolt://0.0.0.0:7687"
    password = '5995Oscar'
    user = 'neo4j'
    driver = neo.NeoSandboxApp(bolt,user,password)
    driver.run_test_query()
    return driver

#def get_root_url():
class Realtor_Url_Data():

    def __init__(self,root_url) :

        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.11 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
                    'Accept-Encoding': 'identity'}
        response = self.get_request(root_url, headers)
        soup = self.get_soup(root_url,response)
        data = self.get_web_data(soup)
        max_it = self.calculate_number_of_pages(data)
        self.url_list =self.create_url_list(max_it,root_url)

    def create_url_list(self,max_it,root_url):
        url_list = []
        for i in range(1,max_it+1):
            url_string = root_url
            url_string  = url_string + '/pg-'
            url_string = url_string +str(i)
            url_list.append(url_string)
        return url_list

        
    def calculate_number_of_pages(self,data):
        max_it = math.ceil(data['props']['pageProps']['pageData']['matching_rows'] / 20)
        return max_it

    def get_soup(self,real_url,response):
        try:
            print("scraping {}".format(real_url))
            soup=BeautifulSoup(response.content,'lxml')

        except:
            print('beauty soup could not scrape parse the content')
        
        return soup
        
    def get_web_data(self,soup):
        try:
            print("parsing data")
            data = json.loads(soup.find('script', type='application/json').string)
            #pprint(data['props']['pageProps']['pageData']['agents'])
        except:
            print('the website data could not be loaded to memory')

        return data

    def get_request(self,real_url,headers):
        try:
            print("requesting {}".format(real_url))
            response = requests.get(real_url,headers=headers)
            #pprint(response)
        except:
            print('could not get a response from realtor.com')
        return response

def get_data_from_realtor_url(url):
    #root_url = "https://www.realtor.com/realestateagents/ridgeway_ak/sort-activelistings"
    root_url = url
    #pprint(root_url)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.11 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
    'Accept-Encoding': 'identity'}
    


    response = Realtor_Url_Data.get_request(root_url, headers)
    soup = Realtor_Url_Data.get_soup(root_url,response)
    data = Realtor_Url_Data.get_web_data(soup)

    max_it = Realtor_Url_Data.calculate_number_of_pages(data)
    url_list = Realtor_Url_Data.create_url_list(max_it,root_url)

    return url_list

def get_root_url(neo_driver):
    search_string = "match (n:Realtor_Search_URL {is_root: True}) where (n.sprouted = False ) with apoc.convert.toJson(n) as output return output  limit 1"
    result = neo_driver.return_root_url(search_string)
    x = result[0]['output']
    root_node = json.loads(x)
    return root_node
    pprint(result)


def get_non_processed_node(neo_driver):
    #app = neo.NeoSandboxApp(bolt="0.0.0.38:7687",user='neo4j',password="5995Oscar")
    result = neo_driver.return_node_related_to_node(node_1="Stack",relation_to="IS_NOT_PROCESSED",node_2="Realtor_Search_URL",limit=1)
    #node_list = []
    #for result in result:
    #    x = result['output']
    #    node_list.append(json.loads(x))
    #pprint(node_list)
    x = result[0]['output']
    non_processed_node = json.loads(x)
    return non_processed_node
    
def create_friendship(neo_driver):
    neo_driver.create_friendship(person1_name="Jack", person2_name="Jill")

def create_url_list(non_processed_node):
    root_url = non_processed_node['properties']['url']
    root_url = root_url.replace("'" , "")
    pprint(root_url)
    data = Realtor_Url_Data(root_url)
    #pprint(data.url_list)
    return data.url_list





    
class Realtor_Search_URL():
    def __init__(self, url, label, processed = False, is_root =False,is_child =False,is_parent= False, is_sibling= False):
        self.label = label
        self.type = "Realtor_Search_URL"
        self.url =  url
        self.is_root = is_root
        self.is_child = is_child
        self.is_parent = is_parent
        self.is_sibling = is_sibling
        self.processed = processed
        self.node_struct = (
            f"{self.label}:{self.type} {{url: '{self.url}', is_root:{self.is_root}, is_child:{self.is_child}, is_parent: {self.is_parent}, is_sibling: {self.is_sibling}, processed: {self.processed} }}"  
        )



class TO_PROCESS():
    def __init__(self, priority = 0):
        self.type = "TO_PROCESS"
        self.label = self.type.lower()
        date_created_key_str = "date_created".replace(' " ' , " ")
        priority_key_str = "priority".strip(' " " ')
        local_date_time_str = "localdatetime()".strip(' " " ')
        self.properties = f"{{{date_created_key_str}: {local_date_time_str}, {priority_key_str}: {priority}}}"
        self.struct = f"{self.label}:{self.type} {str(self.properties)}"

class IS_CHILD():
    def __init__(self, priority = 0):
        self.type = "IS_CHILD"
        self.label = self.type.lower()
        date_created_key_str = "date_created".replace(' " ' , " ")
        priority_key_str = "priority".strip(' " " ')
        local_date_time_str = "localdatetime()".strip(' " " ')
        self.properties = f"{{{date_created_key_str}: {local_date_time_str}, {priority_key_str}: {priority}}}"
        self.struct = f"{self.label}:{self.type} {str(self.properties)}"
        
        #pprint(self.struct)

class IS_ROOT():
    def __init__(self, priority = 0):
        self.type = "IS_ROOT"
        self.label = self.type.lower()
        date_created_key_str = "date_created".replace(' " ' , " ")
        priority_key_str = "priority".strip(' " " ')
        local_date_time_str = "localdatetime()".strip(' " " ')
        self.properties = f"{{{date_created_key_str}: {local_date_time_str}, {priority_key_str}: {priority}}}"
        self.struct = f"{self.label}:{self.type} {str(self.properties)}"
        #pprint(self.struct)

class IS_SIBLING():
    def __init__(self, priority = 0):
        self.type = "IS_ROOT"
        self.label = self.type.lower()
        self.properties = {'date_created': "localdatetime()", "priority": priority}
        self.struct = f"{self.label}:{self.type} {str(self.properties)}"
        #pprint(self.struct)

class to_process_node_struct():
        def __init__(self,label,type_property_of_node):
            self.label = label
            self.common_label = label.lower()
            self.type = type_property_of_node
            self.type_no_quotes = "type".replace(' " ' , " ")
            self.stripped_str = "type".strip(' " " ')
            #pprint(self.type_no_quotes)
            self.properties = f"{self.stripped_str}: '{self.type}'"
            self.struct = F"{self.common_label}:{self.label} {{{self.properties}}}"
            #pprint(self.struct)

class id_label():
    def __init__(self,id,label):
        self.id = id
        self.label = label



class UpdateGraph():

    def __init__(self,neo_driver):
        self.neo_driver = neo_driver

    def get_root_url(self):
        search_string = "match (n:Realtor_Search_URL {is_root: True}) where (n.sprouted = False ) with apoc.convert.toJson(n) as output return output  limit 1"
        result = self.neo_driver.return_root_url(search_string)
        x = result[0]['output']
        root_node = json.loads(x)
        return root_node
        pprint(result)
    def create_url_list(self, non_processed_node):
        root_url = non_processed_node['properties']['url']
        root_url = root_url.replace("'" , "")
        data = Realtor_Url_Data(root_url)
        #pprint(data.url_list)
        return data.url_list

    def set_node_to_sprouted(self,node, property, value):
        pprint("*****set_property_by_id****")
        property = property.strip(' " " ')

        node_label = node['labels'][0]
        node_id= node['id']
        id_label_obj = id_label(id= node_id,label = node_label)

        
        result = self.neo_driver.set_property_by_id(id_label_obj = id_label_obj,property = property,value = value)
        #pprint(result)
        return result

    def create_node_struct(self, url, label, processed = False, is_root =False,is_child =False,is_parent= False, is_sibling= False):
        node_struct = Realtor_Search_URL(url, label, processed = False, is_root =False,is_child =False,is_parent= False, is_sibling= False)
        return node_struct

    def create_relationship_last_to_current_node(self):
        test

    def create_to_process_node_property_struct(self,label = "To_Process"):
        to_process_node_property_struct = to_process_node_struct(label = label, type_property_of_node= "realtor_stack")
        #pprint(to_process_node_property_struct.search_struct)
        return to_process_node_property_struct

    def get_to_process_node(self,node_property_struct,limit =1):
        #pprint(node_property_struct)
        result = neo_driver.return_to_process_stack_node(node_property_struct = node_property_struct, limit = limit)
        result = json.loads(result[0]['output'])
        return result
    
    def create_to_process_relationship_struct(self):
        relationship_struct = TO_PROCESS()
        return relationship_struct

    def create_is_child_relationship(self):
        is_child_relationship = IS_CHILD()
        return is_child_relationship

    def create_is_root_relationship(self):
        is_root_relationship = IS_ROOT()
        return is_root_relationship

    def create_is_sibling_relationship(self):
        is_sibling_relationship = IS_SIBLING()
        return is_sibling_relationship
    
    def create_id_struct_from_node(self, node):  #create a node_struct class
        node_id = node['id']
        label = node['labels'][0]
        key = label.lower()
        struct = f":{label} {{id: {node_id}}}"
        pprint(struct)
        return struct

    def create_relationship_by_id(self,node_1,node_2,relationship_struct, relationship_type = None):
        pprint("*****create_relationship_by_id****")
        pprint(node_1['labels'])
        
        node_1_label = node_1['labels'][0]
        node_1_id = node_1['id']
        node_2_label = node_2['labels'][0]
        node_2_id = node_2['id']
        id_label_obj_1 = id_label(id= node_1_id,label = node_1_label)
        id_label_obj_2 = id_label(id= node_2_id,label = node_2_label)
        
        
        result = neo_driver.create_relationship_by_id(id_label_obj_1=id_label_obj_1,id_label_obj_2=id_label_obj_2, relationship_struct= relationship_struct, relationship_type = relationship_type)
        #pprint(result)
        return result


    def add_node(self,node_struct, node_label):
        
        node = neo_driver.add_node(node_struct = node_struct, node_label =node_label)
        node = json.loads(node[0]['output'])
        return(node)
        #return node
    


def update_graph(neo_driver):
    update_functions = UpdateGraph(neo_driver=neo_driver)
    could_not_add_list = []
    
    root_node = update_functions.get_root_url()
    while root_node:
        url_list = update_functions.create_url_list(non_processed_node=root_node)
        root_struct = update_functions.create_id_struct_from_node(root_node)
        node_property_struct = update_functions.create_to_process_node_property_struct()
        to_process_relation_obj = update_functions.create_to_process_relationship_struct()
        to_process_node = update_functions.get_to_process_node(node_property_struct = node_property_struct)
        to_process_root_relationship_result = update_functions.create_relationship_by_id(node_1=to_process_node, node_2=root_node, relationship_struct= to_process_relation_obj.struct, relationship_type = "to_process") 
        #to_process_relation = update_functions
        last_node = None
        if url_list:
            for url in url_list:
                current_node = update_functions.create_node_struct(url = url, label = "realtor_search_url")
                pprint(current_node)
                is_root_relationship = update_functions.create_is_root_relationship()
                is_child_relationship = update_functions.create_is_child_relationship()

                
                current_node = update_functions.add_node(node_struct = current_node.node_struct, node_label= current_node.label)
                if current_node:
                    pprint(current_node)
                    #current_node_id_struct = update_functions.create_id_struct_from_node(current_node)
                    #pprint(node_struct)
                    is_root_relationship_result = update_functions.create_relationship_by_id(node_1=current_node, node_2=root_node, relationship_struct= is_root_relationship.struct, relationship_type = "is_root")
                    is_child_relationship_result = update_functions.create_relationship_by_id(node_1=root_node, node_2=current_node, relationship_struct= is_child_relationship.struct, relationship_type = "is_child") 
                    to_process_relationship_result = update_functions.create_relationship_by_id(node_1=to_process_node, node_2=current_node, relationship_struct= to_process_relation_obj.struct, relationship_type = "to_process") 
                    #create_relationship_to_root-node
                    #update_functions.create_relationship(node_1,node_2,relationship = is_root_relationship)
            
                else:
                    print("a node could not be added")
                    could_not_add_list.append(current_node)

                sprouted_node = update_functions.set_node_to_sprouted(node = root_node, property= "sprouted", value = True)
                root_node = update_functions.get_root_url()
        else:
            sprouted_node = update_functions.set_node_to_sprouted(node = root_node, property= "sprouted", value = True)
            root_node = update_functions.get_root_url()
            continue
        
    could_not_add_series = pd.Series(could_not_add_list)
    could_not_add_series.to_csv("could_not_add.csv")   
    return True

def crawl_graph():


    """
    #find all ancestors and descendents
        MATCH (n:Node2)
        WITH n, [(n)<-[:Child*]-(x) | x] as ancestors,  [(x)<-[:Child*]-(n) | x] as descendants

        #find 1 parent and 1 child
        MATCH (n:Node2)
        WITH n, [(n)<-[:Child]-(x) | x][0] as parent,  [(x)<-[:Child]-(n) | x] as children
        RETURN n, parent, children 
        RETURN n, ancestors, descendants 

        #set state all descendents of root 
        match (n:Realtor_Search_URL) where (n.is_root = True and n.sprouted = True and n.processed = False) return n limit 100
        match n [:IS_STATE_OF] -> (state)
        pull 100 url's at a time by state

        n:Realtor_Search_URL where n.processed = false  
        match n -{'is_state_of'} ->[]

        n:Realtor_Search_URL related to to_process

        #create or stack??/ or just do it randomly?
    """


if __name__ == "__main__":
    neo_driver = instantiate_neo_driver()
    completed = update_graph(neo_driver)
    #attach_to_node 
