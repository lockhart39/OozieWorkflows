sqoop import \
--connect jdbc:mysql://localhost:3306/retail_db \
--username root \
--password cloudera \
--table orders \
--hive-import \
--hive-overwrite \
--hive-database default \
--hive-table orders_stg \
--create-hive-table

