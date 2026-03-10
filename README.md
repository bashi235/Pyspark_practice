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

---

### 🔹 Phase 10 – Date & Time Functions

#### 📘 `10_Date_n_Time_Functions.pdf`
**Covers:**

**1️⃣ Date Conversion & Parsing**
- `to_date()` (default & custom formats)
- Handling invalid parsing (NULL behavior)
- Managing multiple date formats using `coalesce()`
- Converting timestamp → date
- Default Spark date format expectations

**2️⃣ Timestamp Handling**
- `to_timestamp()` (default & custom formats)
- ISO format handling (`yyyy-MM-dd'T'HH:mm:ss`)
- Comparing `to_date()` vs `to_timestamp()`
- Timestamp precision & timezone behavior
- Converting date → timestamp

**3️⃣ Date Formatting**
- `date_format()` for presentation
- Formatting patterns (`yyyy`, `MM`, `dd`, `HH`, etc.)
- Creating report-friendly columns
- Partition column formatting
- Why NOT to use `date_format()` for filtering

**4️⃣ Current Date & Time**
- `current_date()`
- `current_timestamp()`
- Audit column creation
- Incremental load filtering
- Measuring ingestion delay

**5️⃣ Date Arithmetic**
- `date_add()`
- `date_sub()`
- Using intervals
- Handling negative values
- Timestamp input conversion
- Incremental & SLA use cases

**6️⃣ Month Operations**
- `add_months()`
- Handling month length differences
- Negative month adjustments
- Dynamic month shifting

**7️⃣ Date Difference Functions**
- `datediff()`
- `months_between()`
- Age calculation logic
- Timestamp handling in differences
- Fractional month behavior
- Rounding months

**8️⃣ Date Part Extraction**
- `year()`
- `month()`
- `dayofmonth()`
- `dayofweek()`
- `dayofyear()`
- `weekofyear()`
- ISO week rules
- Weekend identification logic
- Extracting day names using `date_format()`

**9️⃣ Timezone Handling**
- Session timezone awareness
- `from_utc_timestamp()`
- `to_utc_timestamp()`
- Timestamp timezone conversion behavior


---

### 🔹 Phase 11 – RDD Core Transformations & Performance Concepts

#### 📘 `11_rdd_map_flatMap_reduceByKey_groupByKey_partitioning_cache_persist.pdf`
**Covers:**

**RDD Transformations**
- `map()`
- `flatMap()`
- `filter()`
- `reduceByKey()`
- `groupByKey()`
- Difference between `reduceByKey` vs `groupByKey`
- Key-based aggregations

**Partitioning**
- Default partition behavior
- Hash partitioning
- Custom partitioning logic
- Controlling number of partitions
- Performance impact of partition size

**Caching & Persistence**
- `cache()`
- `persist()`
- Storage levels
- Memory vs disk persistence
- When to cache
- When NOT to cache
- Performance optimization strategies

---

### 🔹 Phase 12 – Spark Actions & Driver-Side Operations

#### 📘 `12_collect_take_foreach_toPandas_transformation_action.pdf`
**Covers:**

**Driver-Side Actions**
- `collect()` (full data retrieval)
- `take(n)`
- `foreach()`
- `foreachPartition()`
- `toPandas()`

**Behavior & Internals**
- What happens when `collect()` is called
- Driver memory risks
- Why large collect crashes drivers
- `take()` execution optimization
- Difference between `collect()` and `take()`
- Executor-side execution of `foreach()`
- When to use `foreachPartition()` for database writes
- Why `toPandas()` is memory intensive

**Transformations vs Actions**
- Lazy evaluation
- DAG creation
- Stage creation at shuffle boundaries
- Execution flow when action is triggered
- Why Spark uses lazy execution
- Interview-focused action behavior questions

---

### 🔹 Phase 13 – Advanced Grouping & Approximate Aggregations

#### 📘 `13_cube_rollup_grouping-sets_approx-count-distinct.pdf`
**Covers:**

**Advanced Aggregations**
- `cube()` – multi-dimensional aggregation
- Number of grouping combinations (2^N)
- Null rows meaning in cube output
- Performance impact of cube

**Hierarchical Aggregation**
- `rollup()` – hierarchical subtotal generation
- N+1 grouping levels
- Difference between cube and rollup
- When rollup is preferred

**Custom Grouping**
- `grouping sets`
- Selecting specific grouping combinations
- Difference: cube vs rollup vs grouping sets
- Performance considerations

**Approximate Aggregation**
- `approx_count_distinct()`
- HyperLogLog algorithm
- Memory-efficient distinct counting
- Relative error control
- Difference between `countDistinct()` vs `approx_count_distinct()`
- Performance trade-offs


---

### 🔹 Phase 14 – Spark Execution, Optimization & Performance Internals

---

#### 📘 `14_I_Execution-plan-Basics.pdf`
**Covers:**

- What happens internally when an action is triggered
- Logical Plan vs Physical Plan
- Unresolved → Analyzed → Optimized logical plan
- Physical plan creation
- Job → Stage → Task breakdown
- Shuffle boundary & stage splitting
- `explain()` modes:
  - simple
  - extended
  - formatted
- How to read execution plan (bottom-up reading)
- Exchange operator meaning
- Spark UI vs explain comparison

---

#### 📘 `14_II_Catalyst-optimizer.pdf`
**Covers:**

- What is Catalyst Optimizer
- Rule-Based Optimization (RBO)
- Cost-Based Optimization (CBO)
- Predicate Pushdown
- Column Pruning
- Projection Pruning
- Constant Folding
- Join Reordering
- Why transformation order doesn’t matter logically
- Enabling CBO
- Table statistics importance
- Logical vs physical optimization boundaries

---

#### 📘 `14_III_Shuffle-Intervals.pdf`
**Covers:**

- What exactly is Shuffle
- Narrow vs Wide transformations
- When shuffle happens
- Exchange operator types:
  - hashpartitioning
  - rangepartitioning
  - broadcast exchange
- Shuffle write phase
- Shuffle read phase
- `spark.sql.shuffle.partitions`
- Choosing optimal shuffle partitions
- Data skew basics
- Sort-based shuffle
- Why shuffle is expensive:
  - disk IO
  - network transfer
  - serialization/deserialization
  - memory pressure
  - stage boundary cost

---

#### 📘 `14_IV_Partitioning-and-Parallelism.pdf`
**Covers:**

- How number of tasks are determined
- How partitions are created initially
- Effect of file size & block size
- `spark.default.parallelism`
- `spark.sql.files.maxPartitionBytes`
- repartition() vs coalesce()
- Hash partitioning vs Range partitioning
- partitionBy() during write
- Small files problem
- Static partition pruning
- Dynamic partition pruning
- Detecting pruning via explain plan
- How partition count affects parallelism

---

#### 📘 `14_V_Join-Optimization.pdf`
**Covers:**

- Logical vs Physical join
- Physical join strategies:
  - Broadcast Hash Join
  - Sort Merge Join
  - Shuffle Hash Join
  - Broadcast Nested Loop Join
- How Spark chooses join strategy
- autoBroadcastJoinThreshold
- Join hints:
  - BROADCAST
  - MERGE
- Cost-based join decision
- Join skew detection
- Skew join optimization techniques:
  - Salting
  - Broadcast workaround
  - Repartition by extra column
  - Adaptive Query Execution (AQE)
- Detecting skew in Spark UI

---

#### 📘 `14_VI_Caching-and-Memory-Internals.pdf`
**Covers:**

- DataFrame cache vs RDD cache
- Storage levels:
  - MEMORY_ONLY
  - MEMORY_AND_DISK
  - DISK_ONLY
  - OFF_HEAP
  - Serialized storage
- Tungsten Engine
- WholeStageCodegen
- On-Heap vs Off-Heap memory
- GC pressure
- Garbage collection types (Minor vs Full GC)
- Spill behavior (memory spill vs disk spill)
- Detecting spill in Spark UI
- Executor memory breakdown
- When caching slows performance
- persist() strategy selection

---

### 🔹 Phase 15 – Delta Lake (Lakehouse Storage Layer)

---

#### 📘 `15_Delta-Lake_I_Foundations-of-Delta-lake.pdf`
**Covers:**

- Problems with traditional Data Lakes (Parquet only)
- Lack of ACID transactions
- No concurrency control
- Difficulty performing UPDATE / DELETE
- Schema enforcement issues
- No built-in version history
- Small file problem
- Introduction to Delta Lake
- Delta architecture
- Delta = Parquet files + Transaction log + Snapshot engine
- Understanding `_delta_log`
- Delta table versioning
- Snapshot concept and how Spark reconstructs table state

---

#### 📘 `15_Delta-Lake_II_Creating-writing-delta-tables.pdf`
**Covers:**

- Creating Delta tables
- Writing data using Delta format
- Managed vs External Delta tables
- Registering existing Delta paths as tables
- Converting Parquet tables to Delta
- Write modes:
  - append
  - overwrite
  - ignore
  - errorIfExists
- Schema enforcement
- Schema evolution
- `mergeSchema`
- Auto merge configuration
- Partitioned Delta tables
- `replaceWhere` for safe partition overwrite
- Constraints in Delta:
  - NOT NULL
  - CHECK constraints
- Generated columns
- Identity columns
- Metadata inspection:
  - DESCRIBE DETAIL
  - DESCRIBE HISTORY

---

#### 📘 `15_Delta-Lake_III_DML-operations.pdf`
**Covers:**

- Delta DML operations
- UPDATE operations
- DELETE operations
- MERGE (UPSERT)
- Merge syntax and workflow
- Multiple `whenMatched` conditions
- Handling duplicate keys in source
- Merge optimization strategies
- Slowly Changing Dimensions (SCD)

**SCD Type 1**
- Overwrite existing records
- Implemented using MERGE

**SCD Type 2**
- Maintaining full historical records
- Expiring old rows
- Creating new versions
- Tracking:
  - start_date
  - end_date
  - is_current

- Hash comparison strategy for change detection

---

#### 📘 `15_Delta-Lake_IV_Change-Data-Feed.pdf`
**Covers:**

- What is Change Data Feed (CDF)
- Why CDF is needed
- Incremental change tracking
- Enabling CDF on Delta tables
- Enabling CDF for existing tables
- Reading CDF data
- Metadata columns in CDF:
  - `_change_type`
  - `_commit_version`
  - `_commit_timestamp`
- Change types tracked:
  - insert
  - delete
  - update_preimage
  - update_postimage
- Using CDF for incremental pipelines
- Using CDF in streaming pipelines
- CDF performance considerations

---

#### 📘 `15_Delta-Lake_V_Time-Travel-and-Data-Recovery.pdf`
**Covers:**

- Delta Time Travel concept
- Reading historical versions of data
- Version-based querying
- Timestamp-based querying
- Query syntax using SQL
- PySpark time travel queries
- Viewing Delta table history
- `DESCRIBE HISTORY`
- Data restoration after accidental delete
- Snapshot reconstruction using `_delta_log`

---

#### 📘 `15_Delta-Lake_VI_Delta-Performance-Optimization.pdf`
**Covers:**

- Why Delta tables become slow over time
- Small file problem
- File compaction
- OPTIMIZE command
- How OPTIMIZE works internally
- Compacting partitions
- Scheduling optimization jobs

**Z-Ordering**

- Clustering related data inside files
- Improving data skipping
- Syntax:
  `OPTIMIZE table ZORDER BY (column)`
- Z-order with multiple columns

**Performance Techniques**

- Data skipping
- Statistics collection
- Predicate pushdown
- Partition pruning vs Z-order
- Bloom filters

---

#### 📘 `15_Delta-Lake_VII_Vaccum-and-storage-managemnet.pdf`
**Covers:**

- VACUUM command
- Cleaning old files from storage
- Retention period
- Default retention (7 days)
- Storage cleanup process
- Why VACUUM can be dangerous
- Impact on time travel
- How Delta tracks active vs inactive files
- Safe VACUUM practices
- Managing Delta storage lifecycle

---

#### 📘 `15_Delta-Lake_VIII_Delta-Internals-and-Architecture.pdf`
**Covers:**

- Delta transaction protocol
- Delta commit process
- ACID guarantees in Delta
- Optimistic Concurrency Control (OCC)
- Conflict detection during commits
- Snapshot isolation
- Write conflict scenarios
- Delta version creation
- Commit workflow
- Delta log structure
- Metadata actions inside `_delta_log`
- How Delta ensures atomic writes
- Delta vs Iceberg vs Hudi comparison
- Delta in streaming architectures


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


