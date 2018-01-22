DROP TABLE IF EXISTS sportinggoods_prod.products2;
CREATE EXTERNAL TABLE IF NOT EXISTS sportinggoods_prod.products2 (
product_id int
,product_category_id int
,product_name string
,product_description string
,product_price decimal(10,2)
,product_image string
)
STORED AS PARQUET
TBLPROPERTIES("parquet.compression"="SNAPPY");
