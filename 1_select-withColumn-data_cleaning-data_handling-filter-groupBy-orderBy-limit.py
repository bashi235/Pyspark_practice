# Databricks notebook source
# MAGIC %md
# MAGIC ### load csv file

# COMMAND ----------

df = spark.read.format("csv")\
                .option("header",True)\
                .option("inferSchema",True)\
                .load("/Volumes/practice/practice_schema/adidas_us_sales/Adidas US Sales Datasets.csv")

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### reading without inferSchema
# MAGIC every column data with be in string format only

# COMMAND ----------

df2 = spark.read.format("csv")\
                .option("header",True)\
                .load("/Volumes/practice/practice_schema/adidas_us_sales/Adidas US Sales Datasets.csv")

# COMMAND ----------

df2.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## selecting a column types

# COMMAND ----------

df.head()

# COMMAND ----------

display(df.select("Retailer",df.Product,df.columns[-4]))

# COMMAND ----------

display(df.limit(20))

# COMMAND ----------

# MAGIC %md
# MAGIC ### selecting by index based

# COMMAND ----------

display(df.select(df.columns[1:5]))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Cleaning with withColumn (replacing values & casting data types)

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# Remove commas from Units Sold and convert it to Integer.
df = df.withColumn("Units Sold",regexp_replace(col("Units Sold"),",","").cast("int"))
display(df)

# COMMAND ----------

#Remove commas from Total Sales and convert it to Double.
df = df.withColumn("Total Sales",regexp_replace(col("Total Sales"),",","").cast("double"))
display(df)

# COMMAND ----------

# Convert Operating Profit to numeric type.
df = df.withColumn(
    "Operating Profit",
    regexp_replace(col("Operating Profit"),",","").cast("int")
)
display(df)

# COMMAND ----------

# Convert Operating Margin from "50%" → 0.50.
df = df.withColumn(
    "Operating Margin",
    regexp_replace(col("Operating Margin"),"%","").cast("double")/100
)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Date Handling (BASIC) [date operations]

# COMMAND ----------

#Convert Invoice Date from string to date.
df = df.withColumn(
    "Invoice Date",
    to_date(col("Invoice Date"))
)
display(df)

# COMMAND ----------

# Create a new column year from Invoice Date.
df = df.withColumn(
    "Year of Invoice",
    year(col("Invoice Date"))
)
display(df.select(df.columns[-1:-3:-1]))

# COMMAND ----------

# Create a new column month.
df =df.withColumn(
    "Month of Invoice",
    month(col("Invoice Date"))
)
display(df.select(df.columns[-1:-5:-1]))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Calculated Columns (withColumn)

# COMMAND ----------

#Create a column:
#calculated_sales = price_per_unit * units_sold
df = df.withColumn(
    "calculated_sales",
    col("Price per Unit") * col("Units Sold")
)
#Compare calculated_sales with Total Sales.
#Are they equal?
display(df.select("calculated_sales","Total Sales"))

# COMMAND ----------

# DBTITLE 1,Cell 26
#Create a column:
#profit_check = Total Sales - Operating Profit
df = df.withColumn(
    "Operating Profit",
    regexp_replace(col("Operating Profit"), ",", "").cast("int")
)
df = df.withColumn(
    "profit_check",
    col("Total Sales") - col("Operating Profit")
)


# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Filtering (filter / where)

# COMMAND ----------

# Filter all records where:

# Region = 'Northeast'

df_region_northeast = df.filter(col("Region") == "Northeast")
display(df_region_northeast)

# Filter records where:

# Sales Method = 'Online'
df_sales_method_online = df.filter(col("Sales Method") == "Online")
display(df_sales_method_online)

# Filter records where:

# Units Sold > 1000
df_unit_sales =df.filter(col("Units Sold") > 1000)
display(df_unit_sales)

# Filter records where:

# Product contains "Footwear"
df_product_footwear = df.filter(col("Product").like("%Footwear%"))
display(df_product_footwear)

# Filter records for:

# Year = 2021
df_invoice_year = df.filter(col("Year of Invoice") == 2021)
display(df_invoice_year)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Simple Aggregations (groupBy)

# COMMAND ----------

# Total sales by Region.
display(df.groupby("Region").agg(
    sum("Total Sales").alias("total_sales_by_region")
    )
)

# Total sales by Retailer.
display(df.groupBy("Retailer").agg(
        sum(col("Total Sales")).alias("total_sales_by_retailer")
    )
)


# Average operating profit by Product.
display(
    df.groupBy("Product").agg(
        avg("Operating Profit").alias("average_profit_by_product")
    )
)

# Total units sold by Sales Method.
display(
    df.groupBy("Sales Method").agg(
        sum("Units Sold").alias("total_units_by_sales_method")
    )
)

# Count number of transactions per State.
display(
    df.groupBy("State").agg(
        count("*").alias("total_txn")
    )
)


# COMMAND ----------

# MAGIC %md
# MAGIC ### Sorting & Limiting

# COMMAND ----------

# Find top 5 records with highest Total Sales.
display(
    df.orderBy(
        col("Total Sales").desc()
    ).limit(5)
)

# Find bottom 5 records by Operating Profit.
display(
    df.orderBy(
        col("Operating Profit")
    ).limit(5)
)

# Sort sales by:

# Year (ascending)

# Total Sales (descending)
display(
    df.orderBy(
        col("Year of Invoice").asc(),
        col("Total Sales").desc()
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Business Questions (IMPORTANT 🔥)

# COMMAND ----------

# Which Retailer generated the highest total sales?
display(
    df.groupBy("Retailer").agg(
        sum("Total Sales").alias("total_sales")
    )\
    .orderBy(col("total_sales").desc()).limit(1)
)

# Which Product category sells the most units?
display(
    df.groupBy("Product").agg(
        sum("Units Sold").alias("total_units")
    ).orderBy(col("total_units").desc()).limit(1)
)

# Which Region is the most profitable?
display(
    df.groupBy("Region").agg(
        sum("Operating Profit").alias("profit")
    ).orderBy(col("profit").desc()).limit(1)
)

# Which Sales Method performs better overall?
display(
    df.groupBy("Sales Method")
      .agg(sum("Total Sales").alias("total_sales"))
      .orderBy(col("total_sales").desc())
      .limit(1)
)


# COMMAND ----------

