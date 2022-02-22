from pyspark.ml import Pipeline
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator

def Decision_regression(spark, filename):
    data = spark.read.format("libsvm").load(filename)
    featureIndexer = \
        VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])
    dt = DecisionTreeRegressor(featuresCol="indexedFeatures")
    pipeline = Pipeline(stages=[featureIndexer, dt])
    model = pipeline.fit(trainingData)
    predictions = model.transform(testData)
    predictions.select("prediction", "label", "features").show(5)
    evaluator = RegressionEvaluator(
        labelCol="label", predictionCol="prediction", metricName="rmse")
    rmse = evaluator.evaluate(predictions)
    print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)
    treeModel = model.stages[1]
    print(treeModel)