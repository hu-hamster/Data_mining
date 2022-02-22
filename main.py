from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from submodule.data_process import filter_data, replace_elem, get_alone_elem, ToLibSvm
from submodule.visiable import plt_all
from spark.Decision_Tree import Decision
from spark.Random_forest import Random
from spark.Gradient_boosted import Gradient_boosted
from spark.Naive_Bayes import Naive_Bayes
from spark.Decision_tree_regression import Decision_regression


source_file = "data/heart_2020_cleaned.csv"
save_file = "data/Heart.csv"
feature_file = "data/feature.csv"
libSvm_file = "data/libsvm.txt"
filter_item = ["HeartDisease", "AlcoholDrinking", "Stroke", "MentalHealth"]
if __name__ == '__main__':
    # create session
    sc = SparkContext("local")
    spark = SparkSession(sc)
    # Filter out useful information
    filter_data(spark, source_file, save_file, filter_item)
    replace_elem(save_file, feature_file)
    all_element = get_alone_elem(feature_file)
    plt_all(all_element)

    df = spark.read.csv(feature_file, header=True)
    ToLibSvm(feature_file, libSvm_file)
    Decision(spark, libSvm_file)
    Random(spark,libSvm_file)
    Gradient_boosted(spark, libSvm_file)
    Naive_Bayes(spark, libSvm_file)
    Decision_regression(spark, libSvm_file)

