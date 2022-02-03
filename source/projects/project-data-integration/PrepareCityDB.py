#prepare_zipcode_db.py
from PandasFunctions import PandasFunctions as PF
from pprint import pprint
import json

def get_file_buffer():
    file_path = 'uscities.csv'
    file_buffer = open(file_path, "r", encoding="utf-8")
    return file_buffer

def get_df_from_csv(file_buffer = 'uscities.csv'):
    zip_code_df = PF.Load.csv_to_df(file_buffer)
    pprint(zip_code_df)
    return zip_code_df


def return_zip_code_df_to_zip_code_dict(zip_code_df):
    output_list = []
    zip_code_property_list = PF.Transform.df_to_record_dict(df= zip_code_df,orient = 'records')


    for dictionary in zip_code_property_list:
        #print(dictionary)
        dict_string = json.dumps(dictionary)
        print(dict_string)
        #output_list.append(dict_string)


    pprint(output_list[0])
    #zip_code_property_list
    return output_list

def add_property_column_to_the_zip_code_df(df, zip_code_property_list):
    df['vertice_property'] = zip_code_property_list
    return df

def write_zip_code_df_to_file(zip_code_df):
    PF.Write.data_frame_to_csv(zip_code_df,'us_city_db.csv')
    return True



def main():
    #connection_driver = get_janus_graph_connection_driver()
    #traversal = get_janus_graph_traversal(connection_driver)
    #zip_code_csv_file_buffer = get_file_buffer()
    zip_code_df = get_df_from_csv()
    pprint(zip_code_df)
    zip_code_property_list = return_zip_code_df_to_zip_code_dict(zip_code_df)
    #zip_code_df = add_property_column_to_the_zip_code_df(df = zip_code_df,zip_code_property_list=zip_code_property_list)
    #pprint(zip_code_df)
    #written_to_csv = write_zip_code_df_to_file(zip_code_df)


if __name__ == "__main__":
    main()