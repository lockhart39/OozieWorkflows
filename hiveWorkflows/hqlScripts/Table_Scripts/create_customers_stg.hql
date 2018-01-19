CREATE EXTERNAL TABLE IF NOT EXISTS retail_stg.customers_stg (
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
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001';
