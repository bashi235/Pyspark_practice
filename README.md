# 🚀 PySpark with Databricks – Complete Learning Journey

## 📌 Overview
This repository tracks my **step-by-step learning journey of PySpark using Databricks**.  
Learning is documented using **numbered PDF notes** (concepts) and **corresponding practice code files** (hands-on).

Each numbered set represents **one learning phase**, making it easy for visitors to follow the progression.

---

## 🎯 Purpose of This Repository
- Maintain a **structured PySpark learning record**
- Combine **theory (PDF notes)** with **practice (code)**
- Apply concepts on **real-world datasets**
- Build strong **data engineering fundamentals**

---

## 📂 Learning Index

### 🔹 Phase 1 – PySpark & DataFrame Fundamentals

#### 📘 `1_pyspark_rdd_select_withColumn_filter_distinct_dedup_to_date_date.pdf`
**Covers:**
- What is Apache Spark
- Spark vs Hadoop / MapReduce
- Spark architecture & execution flow
- RDD fundamentals and use cases
- RDD vs DataFrame comparison
- DataFrame basics
- Reading CSV & JSON files
- `select()` (column-based & index-based)
- `withColumn()` and `withColumnRenamed()`
- Data cleaning and type casting
- `filter()` conditions
- `distinct()` and `dropDuplicates()`
- Date handling using `to_date()` and `date_format()`
- Understanding data type vs display format

---

#### 🧪 `1_select-withColumn-data_cleaning-data_handling-filter-groupBy-orderBy-limit.py`
**Practices:**
- Reading CSV data with and without schema inference
- Exploring DataFrame schema and columns
- Column selection (name-based & index-based)
- Cleaning numeric columns using `withColumn` and `regexp_replace`
- Casting columns to appropriate data types
- Date conversion and extracting year/month
- Creating calculated columns
- Filtering data using multiple conditions
- Aggregations using `groupBy` and `agg`
- Sorting and limiting results
- Answering basic business questions using PySpark
- Working with a real-world dataset (Adidas US Sales)

---
### 🔹 Phase 2 – Sorting, Aggregations & Joins

#### 📘 `2_orderBy_groupBy_joins_left_right_outer_left_semi_left_anti_cross.pdf`
**Covers:**
- `orderBy()` and `sort()` operations
- `groupBy()` with aggregate functions
- Understanding join fundamentals
- Inner join
- Left join & Right join
- Full outer join
- Left semi join
- Left anti join
- Cross join
- Join behavior with nulls
- Real-world join use cases and cautions

---

### 🔹 Phase 3 – Null Handling & Data Quality Functions

#### 📘 `3_Null_handling_functions_fill_fillna_dropna_isNull_isNotNull_coalesce.pdf`
**Covers:**
- Understanding nulls in Spark
- `isNull()` and `isNotNull()`
- `fill()` and `fillna()`
- Column-level vs DataFrame-level fill
- `dropna()` (row removal strategies)
- Using `coalesce()` for null-safe logic
- Best practices for null handling in production data

---

### 🔹 Phase 4 – Actions, Schema Control & Reshaping Data

#### 📘 `4_collect_StructType_StructField_pivot_unpivot.pdf`
**Covers:**
- `collect()` action and memory implications
- When (and when not) to use `collect()`
- `StructType` and `StructField`
- Explicit schema definition
- Nested schema creation
- Reading data with predefined schema
- `pivot()` for row-to-column transformation
- `unpivot()` using `stack()`
- Schema normalization use cases

---

### 🔹 Phase 5 – UDFs, Transformations & Temporary Views

#### 📘 `5_udf_transform_tempView_globalTempView.pdf`
**Covers:**
- User Defined Functions (UDFs)
- When to avoid UDFs
- Performance impact of UDFs
- `transform()` for DataFrame-level logic
- Chaining transformations
- Parameterized transformations
- Creating temporary views
- Using Spark SQL on temp views
- Global temporary views
- Temp view vs Global temp view comparison

---

### 🔹 Phase 6 – Window Functions Fundamentals

#### 📘 `6_Window_aggregate_functions_over_clause_partitionBy_orderBy_.pdf`
**Covers:**
- What are window functions
- `over()` clause fundamentals
- `partitionBy()` behavior
- `orderBy()` inside windows
- Difference between `groupBy` and window functions
- Window aggregate functions:
  - `sum()`, `avg()`, `count()`
  - `min()`, `max()`
  - `stddev()`, `variance()`
- Running totals and running averages
- Global vs partitioned windows

---

### 🔹 Phase 7 – Frame Clause & Window Boundaries

#### 📘 `7_over-clause_frame-clause_rowsBetween_rangeBetween.pdf`
**Covers:**
- What is a frame clause
- Default window frame behavior
- `rowsBetween()` usage
- `rangeBetween()` usage
- Difference between row-based and value-based frames
- Unbounded preceding & following
- Sliding windows
- When to use rows vs range frames
- Interview-focused frame clause insights

---

### 🔹 Phase 8 – Window Ranking Functions

#### 📘 `8_Window_rank_Functions_row_number_rank_dense_rank_percent_rank.pdf`
**Covers:**
- `row_number()`
- `rank()` and tie handling
- `dense_rank()` and gapless ranking
- `percent_rank()`
- `ntile(n)`
- `cume_dist()`
- Ranking with `partitionBy`
- Top-N problems per group
- Deduplication using window functions
- Real-world ranking use cases

---

### 🔹 Phase 9 – Window Value Functions

#### 📘 `9_Window_Value_Functions_lag_lead_first_value_last_value_nth_value.pdf`
**Covers:**
- Value-based window functions overview
- `lag()` and offsets
- `lead()` and offsets
- Handling missing previous/next rows
- `first_value()` with different frames
- `last_value()` pitfalls and correct usage
- `nth_value()` behavior
- Frame clause impact on value functions
- Difference between ranking and value functions
- Real-world analytical use cases

## 📈 Future Learning Phases
Additional learning phases will be added in the same structured format:
-
-
-
-
-
-
-




Each new phase will extend this README with:
- File name
- Covered concepts
- Practiced operations

---

## 🛠️ Tools & Platform
- PySpark
- Databricks
- Apache Spark
- Real-world CSV datasets

---

## 🚧 Status
🔄 **Ongoing Learning Journey**  
This repository is actively updated as I progress through more advanced PySpark and Databricks topics.

---

## 📝 Note
- Detailed explanations are intentionally kept inside the **PDF notes**
- Code files focus purely on **practice and implementation**
- This repository reflects **learning progression**, not production pipelines


