SET hive.exec.dynamic.partition.mode=non-strict;
SELECT COUNT(*) FROM retail_stg.customers
