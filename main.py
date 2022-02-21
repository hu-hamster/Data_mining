from pyspark.sql import SparkSession
from pyspark.context import SparkContext
import pandas as pd


# create session
sc = SparkContext("local")
spark = SparkSession(sc)
df = spark.read.csv(r"data/heart_2020_cleaned.csv", header=True)
df = df.select("HeartDisease", "AlcoholDrinking", "Stroke", "MentalHealth")
df.show(10)
# heart_cat = heart.select_dtypes(include="object")
# heart["HeartDisease"] = heart["HeartDisease"].replace({"No": 0, "Yes": 1})
# print(heart["HeartDisease"].unique())
