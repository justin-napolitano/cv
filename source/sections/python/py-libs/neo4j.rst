.. _neo_4j_lib:

########################
Neo4j Python Library
########################



Description
************
* A collection of common classes that represent nodes in a neo4j graph database.
* A developer may simply call defined classes that instantiate a structure that can be easily appended to a native neo4j transaction call.
* I also include the code that implements the native neo4j app to build a sample db from a csv file.  
* I abandonded the work halfway through as I transitioned to a JanusGraph Stack. Nonetheless the code can be expanded to build graphs of greater complexity.  

Links
********

* `GitHub <https://github.com/justin-napolitano/neo4jAPI>`_



Csv to Neo Application
----------------------


.. code-block:: python

    #realtor_graph.py


    #from neo4j_connect_2 import NeoSandboxApp
    #import neo4j_connect_2 as neo
    import GoogleServices as google
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import struct
    from pprint import pprint
    from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
        UniqueIdProperty, RelationshipTo, BooleanProperty, EmailProperty, Relationship,db)
    import pandas as pd
    #import NeoNodes as nn
    import GoogleServices
    import neo4jClasses
    import sparkAPI as spark
    import neoModelAPI as neo
    import os
    #from neoModelAPI import NeoNodes as nn



    def upload_data_pipeline_to_neo(df_pipeline_dictionary):
        upload = DataUploadFunctions()
        df_pipeline_dictionary['country_df']['country_node'] = upload.upload_df(df_pipeline_dictionary['country_df']['country_node'])
        df_pipeline_dictionary['state_df']['country_node'] = upload.map_to_df(df1 = df_pipeline_dictionary['state_df'],df2 = df_pipeline_dictionary['country_df'],lookup_key='country_code',lookup_value='country_node')
        df_pipeline_dictionary['master_df']['country_node'] = upload.map_to_df(df1 = df_pipeline_dictionary['master_df'],df2 = df_pipeline_dictionary['country_df'],lookup_key='country_code',lookup_value='country_node')

        df_pipeline_dictionary['state_df']['state_node'] = upload.upload_df(df_pipeline_dictionary['state_df']['state_node'])
        df_pipeline_dictionary['master_df']['state_node'] = upload.map_to_df(df1 = df_pipeline_dictionary['master_df'],df2 = df_pipeline_dictionary['state_df'],lookup_key='state_code',lookup_value='state_node')
    
        #pprint(df_pipeline_dictionary['master_df'].columns)

        #pprint(df_pipeline_dictionary['state_df'])
        #df_pipeline_dictionary['state_df']['related'] = df_pipeline_dictionary['state_df'].apply(lambda x : pprint(x.state_node), axis = 1)
        df_pipeline_dictionary['state_df']['state_to_country'] = df_pipeline_dictionary['state_df'].apply(lambda x : upload.set_relationships(x.state_node.country , x.country_node), axis = 1)


        df_pipeline_dictionary['master_df']['city_node'] = upload.upload_df(df_pipeline_dictionary['master_df']['city_node'])
        df_pipeline_dictionary['master_df']['city_to_state'] = df_pipeline_dictionary['master_df'].apply(lambda x : upload.set_relationships(x.city_node.state , x.state_node), axis = 1)

        df_pipeline_dictionary['master_df']['url_node'] = upload.upload_df(df_pipeline_dictionary['master_df']['url_node'])
        df_pipeline_dictionary['master_df']['url_node_to_state'] = df_pipeline_dictionary['master_df'].apply(lambda x : upload.set_relationships(x.url_node.state , x.state_node), axis = 1)


        df_pipeline_dictionary['master_df']['root_node'] = upload.upload_df(df_pipeline_dictionary['master_df']['root_node'])
        df_pipeline_dictionary['master_df']['url_node_to_root_node'] = df_pipeline_dictionary['master_df'].apply(lambda x : upload.set_relationships(x.url_node.root , x.root_node), axis = 1)


        

        return df_pipeline_dictionary








        
        
    class DataUploadFunctions():
        def upload_df(self,df):
            #df.apply(lambda x: pprint(str(x) + str(type(x))))
            
            node_list =  df.apply(lambda x: neo.neoAPI.update(x))
            #pprint(node_list)
            return  node_list
        
        def map_to_df(self,df1,df2,lookup_value :str, lookup_key: str):
            df1[lookup_value] = df1[lookup_key]
            #pprint(df1.columns)
            #pprint(df1)
            
            val  = df1[lookup_value].replace(dict(zip(df2[lookup_key],  df2[lookup_value])))
            return val

        def set_relationships(self,source_node, target_node):
            #pprint(self.df.columns)
            #pprint(source_node)
            rel = neo.neoAPI.create_relationship(source = source_node ,target = target_node)
            return rel



    class DataPipelineFunctions():
        def write_df_to_csv(self,df,path: str):
            cwd = os.getcwd()
            path = os.sep.join([cwd,path])

            with open(path,'w') as f:
                df.to_csv(path, index=False)

            return path

        def create_city_nodes(self,df):
            city_nodes = df['city_name'].apply(lambda x :neo.neoAPI.create_city_node(name = x))
            return city_nodes

        def create_url_nodes(self,df):
            url_nodes = df['root_realtor_url'].apply(lambda x :neo.neoAPI.create_realtor_search_url_node(url= x))
            return url_nodes
        
        def create_root_nodes(self,df):
            root_nodes = df['root_realtor_url'].apply(lambda x :neo.neoAPI.create_root_node(url= x))
            return root_nodes

        def create_country_nodes(self,df):
            country_nodes = df.apply(lambda x :neo.neoAPI.create_country_node(code = x.country_code, name = x.country_name),axis =1)
            return country_nodes
            

        def return_unique_country_df(self,df):
            df = df.drop_duplicates(subset=['country_name']).copy()
            df.drop(df.columns.difference(['country_node','state_node','country_name', 'country_code','state_name']), 1, inplace=True)
            #pprint(df)
            return df


        def create_state_nodes(self,df):
            state_nodes = df.apply(lambda x :neo.neoAPI.create_state_node(code = x.state_code, name = x.state_name),axis =1)
            return state_nodes    

        def return_unique_state_df(self,df):
            df = df.drop_duplicates(subset=['state_name']).copy()
            df.drop(df.columns.difference(['state_node','country_node','country_code','state_name','country_name','state_code']), 1, inplace=True)
            #pprint(df)

            return df

        def rename_columns(self,df, mapper = {'city': 'city_name', 'state': 'state_code','realtor_url': 'root_realtor_url'}):
            return df.rename(columns = mapper)


        def add_country_code(self,country_code = "USA"):
            return country_code

        def add_country_name(self,country_name = "United States of America"):
            return country_name

        def upload_df(self,df):
            #df.apply(lambda x: pprint(str(x) + str(type(x))))
            
            node_list =  df.apply(lambda x: neo.neoAPI.update(x))
            pprint(node_list)
            return  node_list
            #df['server_node'] =  node_list
            #pprint(df)
            
            


        def set_url_relationships(self):
            #pprint(self.df.columns)
            update_list = self.df.apply(lambda x: neo.neoAPI.create_relationship(source = x.url_node.city,target = x.city_node), axis=1)
            pprint(update_list)
            return update_list
            #rel = self.df.url.connect(self.df.city)

        def set_city_relationships(self):
            #pprint(self.df.columns)
            update_list = self.df.apply(lambda x: neo.neoAPI.create_relationship(source = x.city_node.country,target = x.country_node), axis=1)
            update_list = self.df.apply(lambda x: neo.neoAPI.create_relationship(source = x.city_node.state,target = x.state_node), axis=1)
            pprint(update_list)
            #rel = self.df.url.connect(self.df.city)

        def set_state_relationships(self):
            #pprint(self.df.columns)
            neo.neoAPI.create_relationship(source = self.unique_state_nodes.state_node[0].country,target = self.unique_state_nodes.country_node[0])
            #update_list = self.unique_state_nodes.apply(lambda x: neo.neoAPI.create_relationship(source = x.state_node.country,target = x.country_node.name), axis=1)
            #pprint(update_list)
            #rel = self.df.url.connect(self.df.city)




        def group_by_state(self):
            grouped = self.df.groupby(by = "state_name")
            
        def load_data_to_pandas_df(self,file_path = "/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv"):
            with open (file_path) as file:
                df = pd.read_csv(file)
            return df
        
        def nodify_city_column(self):
            self.df['city_node'] = self.df['city'].apply(lambda x : neo.neoAPI.create_city_node(name = x))
            
            
            #pprint(df.city_nodes)



        def nodify_states_column(self):

            unique_states = self.df.drop_duplicates(subset=['state']).copy()
            #pprint(state_dict)

            unique_states['state_node'] = unique_states.apply(lambda x: neo.neoAPI.create_state_node(name = x.state_name, code = x.state), axis=1)
            #pprint(unique_states)
            #self.df['state_nodes'] = unique_states['state_nodes'] where unique_states[state_name] = self.df_stateName
            self.df["state_node"] = self.df['state_name']
            #self.df['state_node'] =
            #pprint(self.df['state_name'].map(unique_states))
            self.df['state_node'] = self.df['state_node'].replace(dict(zip(unique_states.state_name,  unique_states.state_node)))
            #pprint(self.df)

            
        
            #mask = dfd['a'].str.startswith('o')
            
            
            #self.df['state_nodes'] = self.df.apply(lambda x: neo.create_state_node(name = x.state_name, code = x.state) if x not in states_dict else states_dict[x], axis=1)
            
        def nodify_url_column(self):
            self.df['url_node'] = self.df['realtor_url'].apply(lambda x : neo.neoAPI.create_url_node(url = x, searched= False))


        



    def instantiate_google_API():
        print("Instantiating all google apis")
        google_apis = GoogleServices.GoogleAPI()
        return google_apis 

    def instantiate_spark_API():
        print("Instantiating the Spark API")
        sparkAPI = spark.SparkAPI()
        return sparkAPI 

    def prepare_pandas_df():
        prepared_df_obj = PreparePandasDF()
        return prepared_df_obj.df

    def instantiate_neo_model_api():
        return neo.neoAPI()
        

    def upload_df_to_db(df, neo_model_api):
        #neo_model_api.update(df['city_nodes'][2])
        df.unique_state_nodes.apply(lambda x: neo_model_api.update(x))
        df.unique_country_nodes.apply(lambda x: neo_model_api.update(x))
        df.url_nodes.apply(lambda x: neo_model_api.update(x))
        df.city_nodes.apply(lambda x: neo_model_api.update(x))
        

    def load_data_to_spark_df(sparkAPI):
        file_path = "/Users/justinnapolitano/Dropbox/python/Projects/webscraping/realtorGraph/uscities.csv"
        df = sparkAPI.load_spark_data_from_csv(file_path)
        df.show(2,truncate=False) 
        return df

    def prepare_df_for_upload(df):
        df2 = df.withColumn('state_node', struct(df.state_name.alias("state_name"),df.state.alias("state_code")))
        #rdd2 = df.rdd.map(lambda x: func1(x))
        
        df3=rdd2.toDF(['city','state', 'state_name', 'realtor_url', 'searched','state_node'])

        #df 2 = df.withColumn("state_nodedf.select(struct('age', 'name').alias("struct")).collect()
        #NeoNodes.StateNode(df.state_name, df.state))
        df2.show(4,truncate=False) 
        #df3.show(4,truncate=False) 



    def prepare_data_pipeline():
        pipeline_functions = DataPipelineFunctions()
        master_df = pipeline_functions.load_data_to_pandas_df()
        master_df['country_name'] = pipeline_functions.add_country_name()
        master_df['country_code'] = pipeline_functions.add_country_code()
        master_df = pipeline_functions.rename_columns(master_df)
        master_df['city_node'] = pipeline_functions.create_city_nodes(master_df)
        master_df['url_node'] = pipeline_functions.create_url_nodes(master_df)
        master_df['root_node'] = pipeline_functions.create_root_nodes(master_df)

        
        master_df_path = pipeline_functions.write_df_to_csv(master_df,'master_df.csv')

        

        
        state_df = pipeline_functions.return_unique_state_df(master_df)
        state_df['state_node'] = pipeline_functions.create_state_nodes(state_df)
        state_df_path = pipeline_functions.write_df_to_csv(state_df,'state_df.csv')
        

        country_df = pipeline_functions.return_unique_country_df(master_df)
        country_df['country_node'] = pipeline_functions.create_country_nodes(country_df)
        country_df_path = pipeline_functions.write_df_to_csv(country_df,'country.csv')


        



        #upload nodes
        
        return {"master_df" : master_df, 'state_df' : state_df, 'country_df': country_df}


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
        #google_api = googleServices.GoogleAPI()
        neo_model_api = instantiate_neo_model_api()
        df_pipeline_dictionary = prepare_data_pipeline()
        final_df_dictionary = upload_data_pipeline_to_neo(df_pipeline_dictionary)
        #for k,v in final_df_dictionary.items():
        #    cwd = os.getcwd()
        #    path = str(k) +"Final"
        #    path = os.sep.join([cwd,path])

        #   with open(path, "w") as file:
        #       v.to_csv(path, index=False)

        #prepared_dfs = prepare_pandas_df()
        #pprint(prepared_df)
        #upload_df_to_db(df = prepared_df, neo_model_api = neo_model_api)

    

    
    




    
    


Native Neo Application
------------------------
.. code-block:: python

    from neo4j import GraphDatabase,basic_auth
    import logging
    from neo4j.exceptions import ServiceUnavailable
    import json


    class NeoSandboxApp():
        def __init__(self, bolt, user, password):
            self.driver = GraphDatabase.driver(
            bolt,
            auth=basic_auth(user, password))

        def run_test_query(self):
            limit = 10
            cypher_query = f'''
            MATCH (n)
            RETURN COUNT(n) AS count
            LIMIT {limit}
            '''


            with self.driver.session(database="neo4j") as session:
                results = session.read_transaction(
                    lambda tx: tx.run(cypher_query).data())
                #for record in results:
                #    print(record['count'])
                results = [x['count'] for x in results]
            return results


        def set_property_by_id(self, id_label_obj,property,value):
            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                result = session.write_transaction(
                    self._set_property_by_id, id_label_obj, property, value)
                return result
                

        @staticmethod
        def _set_property_by_id(tx, id_label_obj, property,value):

            # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
            # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
            match_statement = (f"MATCH (n:{id_label_obj.label}) where (id(n) = {id_label_obj.id} )")
            set_statement = (f"SET n.{property} =  {value}")
            query = " ".join([match_statement,set_statement])
            try:
                #print(query)
                result = tx.run(query) 
                result = [record for record in result]
                return result
            # Capture any errors along with the query and data for traceabilityx    
            except ServiceUnavailable as exception:
                logging.error("{query} raised an error: \n {exception}".format(
                    query=query, exception=exception))
                raise

        def create_relationship_by_id(self, id_label_obj_1,id_label_obj_2, relationship_struct,relationship_type):
            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                result = session.write_transaction(
                    self._create_relationship_by_id, id_label_obj_1, id_label_obj_2,relationship_struct,relationship_type)
                return result
                

        @staticmethod
        def _create_relationship_by_id(tx, id_label_obj_1, id_label_obj_2, relationship_struct,relationship_type):

            # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
            # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
            match_and_return = (f"MATCH (n1:{id_label_obj_1.label}) where id(n1) = {id_label_obj_1.id} MATCH (n2:{id_label_obj_2.label}) where id(n2) = {id_label_obj_2.id}")
            query = (f"{match_and_return} CREATE (n1)-[ {relationship_struct} ]->(n2) return {relationship_type}")
            #query_2 = ("MATCH (n1:$id_label_obj_1.label) where id(n1) = $id_label_obj_1.id MATCH (n2:$id_label_obj_2.label) where id(n2) = $id_label_obj_2.id RETURN n1,n2 CREATE (n1)-[$relationship_struct]->(n2))")
            #print(relationship_part)
            #query = (f"MATCH (n1{node_1_struct}) Match (n2{node_2_struct}) return n1,n2")
            #print(query_2)
            try:
                #result = tx.run("MATCH (n1: $label_1 ) where id(n1) = $id_1 .id MATCH (n2: $label_2 ) where id(n2) = $id_2 RETURN n1,n2 CREATE (n1)-[ $relationship_struct ]->(n2))",label_1 = id_label_obj_1.label,id_1= id_label_obj_1.id, label_2 = id_label_obj_2.label, id_2 = id_label_obj_2.id,relationship_struct= relationship_struct)
                result = tx.run(query) 
                result = [record for record in result]
                return result
            # Capture any errors along with the query and data for traceabilityx    
            except ServiceUnavailable as exception:
                logging.error("{query} raised an error: \n {exception}".format(
                    query=query, exception=exception))
                raise


        def return_root_url(self, search_string):

            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                print("start")
                result = session.write_transaction(self._match_and_return_search_url, search_string)
            return result

        @staticmethod
        def _match_and_return_search_url(tx,search_url):
            query = search_url
            #print(query)
            result = tx.run(query)
            result = [record for record in result]
            return result


        def create_relationship(self, node_1,node_2, relationship_struct):

            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                print("start")
                result = session.write_transaction(self._create_relationship, node_1, node_2, relationship_struct)
            return result

        @staticmethod
        def _create_relationship(tx,node_1,node_2, relationship_struct):
            query = (
                f"CREATE ({node_struct})\
                return apoc.convert.toJson({node_label}) as output"
                )
            #print(query)
            result = tx.run(query)
            result = [record for record in result]
            return result

        def add_node(self,node_struct,node_label):
            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                print("start")
                result = session.write_transaction(self._add_node, node_struct,node_label)
            return result

        @staticmethod    
        def _add_node(tx,node_struct,node_label):
            query = (
                f"CREATE ({node_struct})\
                return apoc.convert.toJson({node_label}) as output"
                )
            #print(query)
            try:
                result = tx.run(query)
                result = [record for record in result]
                return result
            except:
                return False

        def return_to_process_stack_node(self, node_property_struct, limit = 1):
            common_label = node_property_struct.common_label
            node_label = node_property_struct.label
            node_property_struct = node_property_struct.struct
            limit = limit

            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                    print("start")
                    result = session.read_transaction(self._match_and_return_node, node_property_struct,common_label,limit)
                    #print(result)
                #print(result)
            return result 
        
        @staticmethod
        def _match_and_return_node(tx,node_property_struct, common_label, limit):
            query = (
                f"MATCH ({node_property_struct}) with apoc.convert.toJson({common_label}) as output RETURN output limit {limit}"
            )
            #print(query)
            result = tx.run(query)
            print(result)
            

            result = [record for record in result]
            #result = json.dumps(result)

            try:
                return(result)
                
            except ServiceUnavailable as exception:
                logging.error("{query} raised an error: \n {exception}".format(
                    query=query, exception=exception))
                raise


        def return_node_related_to_node(self,node_1,relation_to,node_2 ,limit):

                with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                    print("start")
                    result = session.read_transaction(self._match_and_return_related_node, node_1, relation_to, node_2, limit)
                    #print(result)
                #print(result)
                return result 
        
        @staticmethod
        def _match_and_return_related_node(tx,node_1,relation_to,node_2,limit):
            query = (
                f"MATCH (n: {node_1})-[r: {relation_to} ]->(search_node: {node_2}) with apoc.convert.toJson(search_node) as output RETURN output limit {limit}"
            )
            #print(query)
            result = tx.run(query)
            print(result)
            

            result = [record for record in result]
            #result = json.dumps(result)

            try:
                return(result)
                
            except ServiceUnavailable as exception:
                logging.error("{query} raised an error: \n {exception}".format(
                    query=query, exception=exception))
                raise


        def create_friendship(self, person1_name, person2_name):
            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                result = session.write_transaction(
                    self._create_and_return_friendship, person1_name, person2_name)
                for row in result:
                    print("Created friendship between: {p1}, {p2}".format(p1=row['p1'], p2=row['p2']))

        @staticmethod
        def _create_and_return_friendship(tx, person1_name, person2_name):
            # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
            # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
            query = (
                "CREATE (p1:Person { name: $person1_name }) "
                "CREATE (p2:Person { name: $person2_name }) "
                "CREATE (p1)-[:KNOWS]->(p2) "
                "RETURN p1, p2"
            )
            result = tx.run(query, person1_name=person1_name, person2_name=person2_name)
            try:
                return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
                        for row in result]
            # Capture any errors along with the query and data for traceability
            except ServiceUnavailable as exception:
                logging.error("{query} raised an error: \n {exception}".format(
                    query=query, exception=exception))
                raise

        def find_person(self, person_name):
            with self.driver.session() as session:
                result = session.read_transaction(self._find_and_return_person, person_name)
                for row in result:
                    print("Found person: {row}".format(row=row))

        @staticmethod
        def _find_and_return_person(tx, person_name):
            query = (
                "MATCH (p:Person) "
                "WHERE p.name = $person_name "
                "RETURN p.name AS name"
            )
            result = tx.run(query, person_name=person_name)
            return [row["name"] for row in result]

            
        def close(self):
            self.driver.close()


    class NeoApp:

        def __init__(self, uri, user, password):
            self.driver = GraphDatabase.driver(uri, auth=(user, password))

        def close(self):
            # Don't forget to close the driver connection when you are finished with it
            self.driver.close()
            

        def create_friendship(self, person1_name, person2_name):
            with self.driver.session() as session:
                # Write transactions allow the driver to handle retries and transient errors
                result = session.write_transaction(
                    self._create_and_return_friendship, person1_name, person2_name)
                for row in result:
                    print("Created friendship between: {p1}, {p2}".format(p1=row['p1'], p2=row['p2']))

        @staticmethod
        def _create_and_return_friendship(tx, person1_name, person2_name):
            # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
            # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
            query = (
                "CREATE (p1:Person { name: $person1_name }) "
                "CREATE (p2:Person { name: $person2_name }) "
                "CREATE (p1)-[:KNOWS]->(p2) "
                "RETURN p1, p2"
            )
            result = tx.run(query, person1_name=person1_name, person2_name=person2_name)
            try:
                return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
                        for row in result]
            # Capture any errors along with the query and data for traceability
            except ServiceUnavailable as exception:
                logging.error("{query} raised an error: \n {exception}".format(
                    query=query, exception=exception))
                raise

        def find_person(self, person_name):
            with self.driver.session() as session:
                result = session.read_transaction(self._find_and_return_person, person_name)
                for row in result:
                    print("Found person: {row}".format(row=row))

        @staticmethod
        def _find_and_return_person(tx, person_name):
            query = (
                "MATCH (p:Person) "
                "WHERE p.name = $person_name "
                "RETURN p.name AS name"
            )
            result = tx.run(query, person_name=person_name)
            return [row["name"] for row in result]


        def query(self, query, parameters=None, db=None):
            assert self.__driver is not None, "Driver not initialized!"
            session = None
            response = None
            try: 
                session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
                response = list(session.run(query, parameters))
            except Exception as e:
                print("Query failed:", e)
            finally: 
                if session is not None:
                    session.close()
            return response


    if __name__ == "__main__":
        # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
        uri = "neo4j+s://b121e108.databases.neo4j.io"
        user = "<neo4j>"
        password = "<STbDZyKf5_5Nd26AkXcpI__XnGX2VjKfbVY_rPO3uYI>"
        neo_app = NeoApp(uri, user, password)
        #app.create_friendship("Alice", "David")
        #app.find_person("Alice")
        neo_app.close()
        print("all good!")

Neo4j Classes
---------------

Connection Driver Sessions


.. code-block:: python

    from neo4j import GraphDatabase,basic_auth
    import logging
    
    from neo4j.exceptions import ServiceUnavailable

    class NeoAuraAPI():


        def __init__(self):
            self.aura_driver = self.instantiate_neo_Aura_app()
            #self.run_test_query()

        def instantiate_neo_aura_app(self):
            neo_uri = "neo4j+s://b121e108.databases.neo4j.io"
            neo_user = "<neo4j>"
            neo_password = "<STbDZyKf5_5Nd26AkXcpI__XnGX2VjKfbVY_rPO3uYI>"

            driver = GraphDatabase.driver(neo_uri, auth=(neo_user, neo_password))
            return driver

        def close(self):
            self.driver.close()


    class NeoSandboxAPI():


        def __init__(self):
            self.sanbox_driver = self.instantiate_neo_sandbox_app()
            self.run_test_query()

        def run_test_query(self):
            limit = 10
            cypher_query = f'''
            MATCH (n)
            RETURN COUNT(n) AS count
            LIMIT {limit}
            '''

            with self.driver.session(database="neo4j") as session:
                results = session.read_transaction(
                    lambda tx: tx.run(cypher_query).data())
                for record in results:
                    print(record['count'])


        def instantiate_neo_sandbox_app(self):
            bolt = "bolt://54.147.65.170:7687"
            user = "neo4j"
            password = "pulses-blank-dittos"
            sandbox_driver = GraphDatabase.driver(bolt,auth=basic_auth(user, password))
            
            return sandbox_driver

        def close(self):
            self.driver.close()

Neo nodes
----------

Easy node creation and implementation.

.. code-block:: python

    from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, BooleanProperty, EmailProperty, Relationship)

    class City(StructuredNode):
        uid = UniqueIdProperty()
        name = StringProperty(unique_index=True, required=True)
        state = Relationship('State', 'OF')
        country = Relationship('Country', 'OF')
        
        
    class Country(StructuredNode):
        uid = UniqueIdProperty()
        code = StringProperty(unique_index=True, required=True)
        name = StringProperty(unique_index=True, required=True)
        state = Relationship('State', 'OF')

    class State(StructuredNode):
        uid = UniqueIdProperty()
        code = StringProperty(unique_index=True, required=True)
        name = StringProperty(unique_index=True, required=True)
        

    class URL(StructuredNode):
        uid = UniqueIdProperty()
        url = StringProperty(unique_index=True, required=True)
        searched = BooleanProperty(unique_index = True, required = True)
        state = Relationship('State', 'OF')
        city = Relationship('City', 'OF')

    class Person(StructuredNode):
        uid = UniqueIdProperty()
        full_name = StringProperty(required = True)
        email = EmailProperty()
