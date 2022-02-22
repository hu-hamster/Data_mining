from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def Decision(spark, filename):
    data = spark.read.format("libsvm").load(filename)
    labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(data)
    featureIndexer = \
        VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])
    dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures")
    pipeline = Pipeline(stages=[labelIndexer, featureIndexer, dt])
    model = pipeline.fit(trainingData)
    predictions = model.transform(testData)
    predictions.select("prediction", "indexedLabel", "features").show(5)
    evaluator = MulticlassClassificationEvaluator(
        labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test Error = %g " % (1.0 - accuracy))
    treeModel = model.stages[2]
    print(treeModel)