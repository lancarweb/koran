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
    .option("url", "jdbc:system:password123:@192.168.77.12:1521:FREE") \
    .option("query", "from * from POWER_PLANTS") \
    .option("user", "system") \
    .option("password", "password123") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()