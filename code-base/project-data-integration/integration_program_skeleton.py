#program_skeleton.py
#import load_json_files as bm

import write
import merge as m
import load_df as ldf
import load_vars as lv
import log as log
import clean_df as clean
import download as dl
import gc

"""
master program skeleton for mergeing files to to a crm
"""
def program_skeleton(dictionary: dict, garbage_log):

## Batch Merge creates a back_up of contacts from csv in batches no greater than 500 contacts per document.  Can be expanded.  Keeps files from getting to large
    if dictionary['tasks']['load_json_files']['run'] == True:
        dictionary['tasks']['load_json_files']['log']['paths_loaded'] = lv.load_paths(dictionary['tasks']['load_json_files'])
        dictionary['tasks']['load_json_files']['log']['paths_loaded'] = lv.load_files(dictionary['tasks']['load_json_files'])
        dictionary['tasks']['load_json_files']['log']['date_loaded'] = lv.load_date(dictionary['tasks']['load_json_files'])
        log.json_dump(dictionary['tasks']['load_json_files'])
        log.csv_dump(dictionary['tasks']['load_json_files'])
        clean_df = m.load_json_files(dictionary['tasks']['load_json_files'])
        clean.clean_df(clean_df)
        clean.series_col(clean_df)
        clean.subject_col(clean_df)
        clean.pdf_col(clean_df)
        clean_df = clean.output_df(clean_df,dictionary['tasks']['load_json_files'])
        write.df_toCsv(clean_df,dictionary['tasks']['load_json_files'])
        write.df_toJson(clean_df,dictionary['tasks']['load_json_files'])
        gc.collect
        #print(clean_df)



#  downloads pdf's associated with supreme court case. 
    if dictionary['tasks']['download_pdf']['run'] == True:
        dictionary['tasks']['download_pdf']['log']['paths_loaded'] = lv.load_paths(dictionary['tasks']['download_pdf'])
        #dictionary['tasks']['download_pdf']['log']['paths_loaded'] = lv.load_files(dictionary['tasks']['download_pdf'])
        dictionary['tasks']['download_pdf']['log']['date_loaded'] = lv.load_date(dictionary['tasks']['download_pdf'])
        #print(dictionary['tasks']['download_pdf'])
        log.json_dump(dictionary['tasks']['download_pdf'])
        log.csv_dump(dictionary['tasks']['download_pdf'])

        master_df = ldf.load_cases_df(dictionary['tasks'])
        dl.download_pdf(master_df)




### Dumb merge creates the Master file.  One big file containing all contacts
    if dictionary['tasks']['dumb_merge']['run'] == True:
        dictionary['tasks']['dumb_merge']['log']['paths_loaded'] = lv.load_paths(dictionary['tasks']['dumb_merge'])
        dictionary['tasks']['dumb_merge']['log']['paths_loaded'] = lv.load_files(dictionary['tasks']['dumb_merge'])
        dictionary['tasks']['dumb_merge']['log']['date_loaded'] = lv.load_date(dictionary['tasks']['dumb_merge'])

        dumb_merge = m.dumb_merge(dictionary['tasks']['dumb_merge'])
        write.df_toCsv(dumb_merge,dictionary['tasks']['dumb_merge'],dictionary['tasks']['dumb_merge']['files']['output_prefix'])
        dictionary['dumb_merged'] = True
    #    merge.mastermerge(dictionary)
    #if dictionary['backup'] = True:
    #    backup.backup(dictionary)

    if dictionary['tasks']['unsubscribe']['run'] == True:
        dictionary['tasks']['unsubscribe']['log']['paths_loaded'] = lv.load_paths(dictionary['tasks']['unsubscribe'])
        dictionary['tasks']['unsubscribe']['log']['paths_loaded'] = lv.load_files(dictionary['tasks']['unsubscribe'])
        dictionary['tasks']['unsubscribe']['log']['date_loaded'] = lv.load_date(dictionary['tasks']['unsubscribe'])
        log.json_dump(dictionary['tasks']['unsubscribe'])
        log.csv_dump(dictionary['tasks']['unsubscribe'])
        master_df, unsubscriber_df = ldf.unsubcribe_master(dictionary['tasks'])
        write.df_toCsv(master_df,dictionary['tasks']['dumb_merge'],dictionary['tasks']['dumb_merge']['files']['output_prefix'])
        write.df_toCsv(unsubscriber_df,dictionary['tasks']['unsubscribe'],dictionary['tasks']['unsubscribe']['files']['output_prefix'])

        load_json_files = ldf.unsubscribe_batches(dictionary['tasks'])
        counter = 0
        for i in load_json_files:
            #print(i)
            name = '_'.join((str(counter),dictionary['tasks']['load_json_files']['files']['output_prefix']))
            #write.df_toCsv(i,dictionary['tasks']['load_json_files'], name)
            #counter = counter + 1
            print(name)
            write.df_toCsv(i,dictionary['tasks']['load_json_files'], name)
            counter = counter + 1
            print(i)





###Removes subcribers from contact list


##Remaining functions create Views
    if dictionary['tasks']['create_POC_table']['run'] == True:
        dictionary['tasks']['create_POC_table']['log']['paths_loaded'] = lv.load_paths(dictionary['tasks']['create_POC_table'])
        dictionary['tasks']['create_POC_table']['log']['paths_loaded'] = lv.load_files(dictionary['tasks']['create_POC_table'])
        dictionary['tasks']['create_POC_table']['log']['date_loaded'] = lv.load_date(dictionary['tasks']['create_POC_table'])
        log.json_dump(dictionary['tasks']['create_POC_table'])
        log.csv_dump(dictionary['tasks']['create_POC_table'])
        #print(dictionary)
        POC_df = ldf.load_POC(dictionary['tasks'])
        write.df_toCsv(POC_df,dictionary['tasks']['create_POC_table'],dictionary['tasks']['create_POC_table']['files']['output_prefix'])
        #print("true")

    if dictionary['tasks']['create_company_table']['run'] == True: 
        dictionary['tasks']['create_company_table']['log']['paths_loaded'] = lv.load_paths(dictionary['tasks']['create_company_table'])
        dictionary['tasks']['create_company_table']['log']['paths_loaded'] = lv.load_files(dictionary['tasks']['create_company_table'])
        dictionary['tasks']['create_company_table']['log']['date_loaded'] = lv.load_date(dictionary['tasks']['create_company_table'])
        log.json_dump(dictionary['tasks']['create_company_table'])
        log.csv_dump(dictionary['tasks']['create_company_table'])
        company_table = ldf.load_company_table(dictionary['tasks'])
        write.df_toCsv(company_table ,dictionary['tasks']['create_company_table'],dictionary['tasks']['create_company_table']['files']['output_prefix'])


