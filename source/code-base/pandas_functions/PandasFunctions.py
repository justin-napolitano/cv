import pandas as pd

"""
A class that of a few pandas functions
"""
class PandasFunctions:
    """
    load class with a few loading functions that are modified to my preferences
    """
    class Load:
        """
        converts a csv to df from file
        """
        def csv_to_df(filepath_or_buffer):
            try:
                df = pd.read_csv(filepath_or_buffer, sep=',', header='infer', index_col=None, usecols=None, squeeze=False, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)
            except Exception as e:
                raise e

            return df
        """
        creates a df standard way
        """
        def create_df(list_or_series_or_dictionary):
            df = pd.DataFrame(list_or_series_or_dictionary)
            return df
            """
            creates an empty df
            """
        def create_empty_df():
            df = pd.DataFrame()
            return df
        """
        transform functions
        """
    class Transform:
        def df_to_record_dict(df, orient):
            if orient == 'records':
                return df.to_dict(orient='records')
            elif orient == 'index':
                return df.to_dict(orient= 'index')
            elif orient == 'dict':
                return df.to_dict(orient= 'dict')
    """
    write functions
    """
    class Write:
        def data_frame_to_csv(df,file_path):
            df.to_csv(path_or_buf=file_path, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)

 
        
        


