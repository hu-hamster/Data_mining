from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.linalg import Vectors

def Random(spark, filename):
    data = spark.read.format("libsvm").load(filename)
    labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(data)
    featureIndexer = \
        VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])
    rf = RandomForestClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures", numTrees=10)
    labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel",
                                   labels=labelIndexer.labels)
    pipeline = Pipeline(stages=[labelIndexer, featureIndexer, rf, labelConverter])
    model = pipeline.fit(trainingData)
    predictions = model.transform(testData)
    predictions.select("predictedLabel", "label", "features").show(5)
    evaluator = MulticlassClassificationEvaluator(
        labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test Error = %g" % (1.0 - accuracy))
    rfModel = model.stages[2]
    print(rfModel)