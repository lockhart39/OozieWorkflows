SET hive.exec.dynamic.partition.mode=non-strict;

INSERT INTO TABLE ${prqdb}.${prqtablename}
SELECT ${columns} FROM ${stgdb}.${stgtablename};
