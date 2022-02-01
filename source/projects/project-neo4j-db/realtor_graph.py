#realtor_graph.py


from neo4j_connect_2 import NeoSandboxApp
import neo4j_connect_2 as neo
import GoogleServices as google
from pyspark.sql import SparkSession
from pyspark.sql.functions import struct
from pprint import pprint
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, BooleanProperty, EmailProperty, Relationship,db)
import pandas as pd
import NeoNodes as nn







class PandasActions():
        

    def load_data_to_pandas_df(self,file_path = "/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv"):
        with open (file_path) as file:
            df = pd.read_csv(file)
        return df
    
    def nodify_city_column(self,df):
        df['city_nodes'] = df['city'].apply(lambda x : nn.City(name = x))
        #pprint(df.city_nodes)

    def nodify_states_column(self,df):
        df['state_nodes'] = df.apply(lambda x: nn.State(name = x.state_name, code = x.state), axis=1)
        
    def nodify_url_column(self,df):
        df['url_nodes'] = df['realtor_url'].apply(lambda x : nn.URL(url = x, searched= False))

    def nodify_country_column(self,df):
        df["country_nodes"] = nn.Country(code = "USA", name = "United States of America")
        







class NeoAPI():

    

    def __init__(self):
        self.NeoSandboxApp = self.instantiate_neo_sandbox_app()
        self.run_test_query()

    def run_test_query(self):
        self.NeoSandboxApp.run_test_query()


    def instantiate_neo_sandbox_app(self):
        bolt = "bolt://54.147.65.170:7687"
        user = "neo4j"
        password = "pulses-blank-dittos"
        pprint("Instantiating Neo Sandbox Application Interface")
        
        return neo.NeoSandboxApp(bolt = bolt, user = user, password = password)

    def instantiate_neo_aura_app(self):
        neo_uri = "neo4j+s://b121e108.databases.neo4j.io"
        neo_user = "<neo4j>"
        neo_password = "<STbDZyKf5_5Nd26AkXcpI__XnGX2VjKfbVY_rPO3uYI>"

        pprint("Instantiating Neo4j Application Interface")
        print(' ')
        print(' ')
        print(' ')

        return neo.NeoApp(neo_uri, neo_user, neo_password)

class GoogleAPIS:
    def __init__(self):
        self.GoogleCredentials = self.load_google_creds()
        self.SheetsApp = self.instantiate_sheets_app()
        self.DriveApp = self.instantiate_drive_app()

    def load_google_creds(self):
        pprint("Getting Google Creds")
        print(' ')
        print(' ')
        print(' ')
        #file_path = "credentials.json"
        return google.creds(file_path = "credentials.json")

    def instantiate_sheets_app(self):
        pprint("instantiating Google Sheets Application Interface")
        print(' ')
        print(' ')
        print(' ')
        #should modify the sheetsapp method to get creds if creds is not valid
        return google.SheetsApp(self.GoogleCredentials.credentials)

    def instantiate_drive_app(self):
        pprint("instantiating Google Drive Application Interface")
        DriveApp = google.DriveApp(self.GoogleCredentials.credentials)
        pprint("testing Drive App by listing files in folder:")
        print(' ')
        print(' ')
        print(' ')
        DriveApp.test_call()
        return DriveApp

    
class SparkAPI():

    def __init__(self):
        self.SparkSession = self.instantiate_spark_session()
    
    def instantiate_spark_session(self):
        pprint("instantiating Spark Session Application Interface")
        print(' ')
        print(' ')
        print(' ')
        return SparkSession.builder.getOrCreate()



    def load_spark_data_from_csv(self,file_path):
        pprint("Reading Data from CSV at Filepath = {}".format(file_path))
        print(' ')
        print(' ')
        print(' ')
        df = self.SparkSession.read.option("header",True).csv(file_path)
        return df

class neoModelAPI():

    def __init__(self):
        self.instantiate_neo_model_session()    
        
    
    def instantiate_neo_model_session(self):
        pprint("instantiating NeoModel Session Application Interface")
        print(' ')
        print(' ')
        print(' ')
        config.DATABASE_URL ="bolt://neo4j:pulses-blank-dittos@54.147.65.170:7687"
    
    
    def update(self,obj):
        with db.transaction:
            obj.save()
        



def instantiate_google_API():
    print("Instantiating all google apis")
    google_apis = GoogleAPIS()
    return google_apis 

def instantiate_spark_API():
    print("Instantiating the Spark API")
    sparkAPI = SparkAPI()
    return sparkAPI 

def load_data_to_spark_df(sparkAPI):
    file_path = "/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv"
    df = sparkAPI.load_spark_data_from_csv(file_path)
    df.show(2,truncate=False) 
    return df

def prepare_df_for_upload(df):
    df2 = df.withColumn('state_node', struct(df.state_name.alias("state_name"),df.state.alias("state_code")))
    rdd2 = df.rdd.map(lambda x: func1(x))
    
    df3=rdd2.toDF(['city','state', 'state_name', 'realtor_url', 'searched','state_node'])

    #df 2 = df.withColumn("state_nodedf.select(struct('age', 'name').alias("struct")).collect()
    #NeoNodes.StateNode(df.state_name, df.state))
    df2.show(4,truncate=False) 
    #df3.show(4,truncate=False) 

def load_data_to_pandas_df():
    file_path = "/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv"
    with open (file_path) as file:
        df = pd.read_csv(file)
    pprint(df)
    return df



def prepare_pandas_df():
    pandas_functions = PandasActions()
    df = pandas_functions.load_data_to_pandas_df()
    pandas_functions.nodify_city_column(df)
    pandas_functions.nodify_states_column(df)
    pandas_functions.nodify_url_column(df)
    pandas_functions.nodify_country_column(df)
    df.drop(['city','state','state_name','realtor_url','searched'], axis = 1, inplace = True)
    #pprint(df)
    return df

def instantiate_neo_model_api():
    return neoModelAPI()
    

def upload_df_to_db(df, neo_model_api):
    #neo_model_api.update(df['city_nodes'][2])
    df.city_nodes.apply(lambda x: neo_model_api.update(x))
    df.state_nodes.apply(lambda x: neo_model_api.update(x))
    df.url_nodes.apply(lambda x: neo_model_api.update(x))
    df.country_nodes.apply(lambda x: neo_model_api.update(x))
    



if __name__ == "__main__":
    #neo_app= instantiate_neo_aura_app()
    #neo_sandbox_app = instantiate_neo_sandbox_app()
    #google_creds = load_google_creds()
    #sheets_app = instantiate_sheets_app(google_creds.credentials)
    #drive_app = instantiate_drive_app(google_creds.credentials)
    #googleAPI = instantiate_google_API()
    #sparkAPI = instantiate_spark_API()
    #neoAPI = NeoAPI()
    #nodified_df = pandas_functions.nodify_dataframe()
    #test()
    neo_model_api = instantiate_neo_model_api()
    prepared_df = prepare_pandas_df()
    #pprint(prepared_df)
    upload_df_to_db(df = prepared_df, neo_model_api = neo_model_api)

    

    
    




    
    