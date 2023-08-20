# Databricks notebook source
print("hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC Select "Hello"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC # My Test

# COMMAND ----------

# MAGIC %run ./Demo/Setup
# MAGIC

# COMMAND ----------

var1

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/databricks-datasets/

# COMMAND ----------

x  = dbutils.fs.ls('/databricks-datasets/')

display(x)

# COMMAND ----------


