# Databricks notebook source
# MAGIC %md ### Import Registered Model
# MAGIC 
# MAGIC ##### Overview
# MAGIC 
# MAGIC * Import a registered model from a folder.
# MAGIC * See notebook [Export_Model]($Export_Model).
# MAGIC 
# MAGIC ##### Widgets
# MAGIC * `1. Model name` - new registered model name.
# MAGIC * `2. Destination experiment name` - contains runs created for model versions.
# MAGIC * `3. Input directory` - Input directory containing the exported model.
# MAGIC * `4. Delete model` - delete model and its versions before importing.
# MAGIC 
# MAGIC #### Limitations
# MAGIC * There is a bug where you cannot create a model with the same name as a deleted model.

# COMMAND ----------

# MAGIC %md ### Include setup

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------

# MAGIC %md ### Widget setup

# COMMAND ----------

dbutils.widgets.text("1. Model name", "") 
model_name = dbutils.widgets.get("1. Model name")

dbutils.widgets.text("2. Destination experiment name", "") 
experiment_name = dbutils.widgets.get("2. Destination experiment name")

dbutils.widgets.text("3. Input directory", "") 
input_dir = dbutils.widgets.get("3. Input directory")

dbutils.widgets.dropdown("4. Delete model","no",["yes","no"])
delete_model = dbutils.widgets.get("4. Delete model") == "yes"

dbutils.widgets.dropdown("5. Import source tags","no",["yes","no"])
import_source_tags = dbutils.widgets.get("5. Import source tags") == "yes"

import os
os.environ["INPUT_DIR"] = input_dir.replace("dbfs:","/dbfs")

print("model_name:", model_name)
print("input_dir:", input_dir)
print("experiment_name:", experiment_name)
print("delete_model:", delete_model)
print("import_source_tags:", import_source_tags)

# COMMAND ----------

assert_widget(model_name, "1. Model name")
assert_widget(experiment_name, "2. Destination experiment name")
assert_widget(input_dir, "3. Input directory")

# COMMAND ----------

# MAGIC %md ### Display model files to be imported

# COMMAND ----------

# MAGIC %sh cat $INPUT_DIR/model.json

# COMMAND ----------

# MAGIC %sh ls -l $INPUT_DIR

# COMMAND ----------

# MAGIC %md ### Import model

# COMMAND ----------

from mlflow_export_import.model.import_model import import_model

import_model(
  model_name =model_name, 
  experiment_name = experiment_name, 
  input_dir = input_dir, 
  delete_model = delete_model,
  import_source_tags = import_source_tags
)
