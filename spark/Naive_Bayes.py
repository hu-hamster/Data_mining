from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def Naive_Bayes(spark, filename):
    data = spark.read.format("libsvm").load(filename)
    splits = data.randomSplit([0.6, 0.4], 1234)
    train = splits[0]
    test = splits[1]
    nb = NaiveBayes(smoothing=1.0, modelType="multinomial")
    model = nb.fit(train)
    predictions = model.transform(test)
    predictions.show()
    evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction",
                                                  metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test set accuracy = " + str(accuracy))