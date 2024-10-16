from pyspark.sql import SparkSession
import os

#-----------------------------------------------------#
#                       MAKE IT WORK
# 1)To make this script work Change the DB options.
# 2)Create the table in the database in advance.
# 3)Just change the Path After "current_dir" variable in Read_CSV functino.
# 4)Change the option DBTABLE too.
#-----------------------------------------------------#

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CSV to Database") \
    .config("spark.some.config.option", "some-value") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0,mysql:mysql-connector-java:8.0.17") \
    .getOrCreate()


# Get the current working directory
current_dir = os.getcwd()

# Read CSV into DataFrame
df = spark.read.csv("file:///" + current_dir + "/previous_application.csv", header=True)

# Write DataFrame to MySQL database by appending to the existing table
df.write \
    .format("jdbc") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://localhost:3306/HomeLoans?serverTimezone=UTC") \
    .option("dbtable", "previous_application") \
    .option("user", "root") \
    .option("password", "-----------") \
    .mode("append") \
    .save()
