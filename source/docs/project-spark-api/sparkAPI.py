from pyspark.sql import SparkSession
class SparkAPI():

    def __init__(self):
        self.SparkSession = self.instantiate_spark_session()
    
    def instantiate_spark_session(self):
        return SparkSession.builder.getOrCreate()



    def load_spark_data_from_csv(self,file_path):
        df = self.SparkSession.read.option("header",True).csv(file_path)
        return df
