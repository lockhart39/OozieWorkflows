sqoop import \
--connect jdbc:mysql://localhost:3306/retail_db \
--username root \
--password cloudera \
--table customers \
--hive-import \
--hive-overwrite \
--hive-database retail_stg \
--hive-table customersNamedMary_stg \
--create-hive-table \
--where "customer_fname = 'Mary'" \
--delete-target-dir \
--direct

