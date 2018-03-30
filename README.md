# Stocktaking

Make inventory check quicker

Database structure:
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| id               | int(11)      | NO   | PRI | NULL    | auto_increment |
| barcode          | varchar(30)  | YES  |     | NULL    |                |
| indeks           | varchar(30)  | YES  |     | NULL    |                |
| name             | varchar(50)  | YES  |     | NULL    |                |
| catalogue_number | int(11)      | YES  |     | NULL    |                |
| state            | varchar(30)  | YES  |     | NULL    |                |
| description      | varchar(200) | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
