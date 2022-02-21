from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.context import SparkContext
import pandas as pd
from submodule.data_process import filter_data

source_file = "data/heart_2020_cleaned.csv"
filter_item = ["HeartDisease", "AlcoholDrinking", "Stroke", "MentalHealth"]
if __name__ == '__main__':
    # create session
    sc = SparkContext("local")
    spark = SparkSession(sc)
    filter_data(spark, source_file, filter_item)
    # df = spark.read.csv(r"data/heart_2020_cleaned.csv", header=True)
    # df = df.select("HeartDisease", "AlcoholDrinking", "Stroke", "MentalHealth")
    # df.show(10)
    # heart_cat = heart.select_dtypes(include="object")
    # heart["HeartDisease"] = heart["HeartDisease"].replace({"No": 0, "Yes": 1})
    # print(heart["HeartDisease"].unique())
