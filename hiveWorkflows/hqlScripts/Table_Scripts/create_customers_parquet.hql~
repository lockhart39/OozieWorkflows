DROP TABLE IF EXISTS retail.customers;
CREATE EXTERNAL TABLE IF NOT EXISTS retail.customers (
customer_id int
,customer_fname string
,customer_lname string
,customer_email string
,customer_password string
,customer_street string
,customer_city string
,customer_state string
,customer_zipcode string
)
STORED AS PARQUET
TBLPROPERTIES("parquet.compression"="SNAPPY");
