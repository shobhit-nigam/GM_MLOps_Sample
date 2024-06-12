# Databricks notebook source
print("hello world")

# COMMAND ----------

secret_value = dbutils.secrets.get(scope="trial", key="our-key") 

# COMMAND ----------

print(secret_value)

# COMMAND ----------

print("hello")

# COMMAND ----------


