Enter password: **************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 21
Server version: 8.0.41 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| laplateforme       |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.02 sec)

mysql> SHOW TABLES;
ERROR 1046 (3D000): No database selected
mysql> USE Laplateforme
Database changed
mysql> SHOW TABLES
    -> ;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etudiants              |
+------------------------+
1 row in set (0.01 sec)

mysql> DESCRIBE etudians,
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',' at line 1
mysql> DESCRIBE etudiants;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int unsigned | NO   | PRI | NULL    | auto_increment |
| nom    | varchar(255) | NO   |     | NULL    |                |
| prenom | varchar(255) | NO   |     | NULL    |                |
| age    | int unsigned | NO   |     | NULL    |                |
| email  | varchar(255) | NO   |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

mysql> INSERT INTO etudiants ( nom, prenom, birth, email) VALUES
    -> ('Spaghetti', 'Jenny', '23', 'betty.Spaghetti@laplateforme.io'),
    -> ('Steak', 'Chuck', '45', 'chuck.steak@laplateforme.io'),
    -> ('Doe', 'John', '18', 'john.doe@laplateforme.io'),
    -> ('Barnes', 'Binkie', '16', 'binkie.barnes@laplateforme.io'),
    -> ('Dupuis', 'Gertrude', '20', 'gertrude.dupuis@laplateforme.io')
    -> ;
ERROR 1054 (42S22): Unknown column 'birth' in 'field list'
mysql> INSERT INTO etudiants ( nom, prenom, age, email) VALUES
    -> ('Spaghetti', 'Jenny', '23', 'betty.Spaghetti@laplateforme.io'),
    -> ('Steak', 'Chuck', '45', 'chuck.steak@laplateforme.io'),
    -> ('Doe', 'John', '18', 'john.doe@laplateforme.io'),
    -> ('Barnes', 'Binkie', '16', 'binkie.barnes@laplateforme.io'),
    -> ('Dupuis', 'Gertrude', '20', 'gertrude.dupuis@laplateforme.io')
    -> ;
Query OK, 5 rows affected (0.02 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> SELECT *FROM etudiants;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Jenny    |  23 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
+----+-----------+----------+-----+---------------------------------+
5 rows in set (0.01 sec)

mysql>