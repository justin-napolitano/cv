#prepare_zipcode_db.py
from PandasFunctions import PandasFunctions as PF
from pprint import pprint


def get_file_buffer():
    file_path = 'zip.csv'
    file_buffer = open(file_path, "r", encoding="utf-8")
    return file_buffer

def get_df_from_csv(file_buffer):
    zip_code_df = PF.csv_to_df(file_buffer)
    pprint(zip_code_df)
    return zip_code_df

def return_zip_code_df_to_zip_code_dict(zip_code_df):
    zip_code_property_list = PF.df_to_record_dict(df= zip_code_df,orient = 'records')
    return zip_code_property_list

def add_property_column_to_the_zip_code_df(df, zip_code_property_list):
    df['vertice_property'] = zip_code_property_list


def main():
    #connection_driver = get_janus_graph_connection_driver()
    #traversal = get_janus_graph_traversal(connection_driver)
    zip_code_csv_file_buffer = get_file_buffer()
    zip_code_df = get_df_from_csv(zip_code_csv_file_buffer)
    zip_code_property_list = return_zip_code_df_to_zip_code_dict(zip_code_df)
    zip_code_df = add_property_column_to_the_zip_code_df(df = zip_code_df,zip_code_property_list=zip_code_property_list)
    pprint(zip_code_df)

    #print(traversal)
    #vertex_added = add_zip_code_vertex(traversal)
    #vertex_added = add_vertex(traversal)
    #print(vertex_added)
    #get_value_map(traversal)
    #closed_connection = close_connection(connection_driver)
    #mgmt = Gremlin.graph.openManagement()
    #mgmt.printSchema()


if __name__ == "__main__":
    main()