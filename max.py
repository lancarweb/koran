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
    .option("url", "jdbc:oracle:thin:@192.168.200.14:1521/MAXDB") \
    .option("query", "select * from MATRECTRANS") \
    .option("user", "maximo") \
    .option("password", "maximo") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()
jdbcDF.show()