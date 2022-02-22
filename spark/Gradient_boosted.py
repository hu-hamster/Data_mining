from pyspark.ml import Pipeline
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def Gradient_boosted(spark, filename):
    data = spark.read.format("libsvm").load(filename)
    labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(data)
    featureIndexer = \
        VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])
    gbt = GBTClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures", maxIter=10)
    pipeline = Pipeline(stages=[labelIndexer, featureIndexer, gbt])
    model = pipeline.fit(trainingData)
    predictions = model.transform(testData)
    predictions.select("prediction", "indexedLabel", "features").show(5)
    evaluator = MulticlassClassificationEvaluator(
        labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test Error = %g" % (1.0 - accuracy))
    gbtModel = model.stages[2]
    print(gbtModel)