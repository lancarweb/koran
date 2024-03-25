# oracle-example.py
from pyspark.sql import SparkSession

appName = "PySpark Example - Oracle Example"
master = "local"
# Create Spark session
spark = SparkSession.builder \
    .appName(appName) \
    .master(master) \
    .getOrCreate()

jdbcDF = spark.read.format("jdbc") \
    .option("url", "jdbc:oracle:thin:@192.168.77.12:1521/FREE") \
    .option("query", "select JSON_OBJECT(*) from POWER_PLANTS") \
    .option("user", "system") \
    .option("password", "password123") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()
print(jdbcDF.show())