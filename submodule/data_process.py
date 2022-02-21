"""
** usage: get DataFrame from csv file and isolate useful information
** arguments:
**** spark: SparkSession
**** read_filename: The path of source file
**** filter_items: filter values, such as: [“name”, "age"]
"""
def filter_data(spark, read_filename, filter_items):
    df = spark.read.csv(read_filename, header=True)
    df = df.select(filter_items)
    # df = df.map(lambda x:)
    # return df
