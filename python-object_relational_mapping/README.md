# Python - Object-relational mapping

##Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

###General
* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
-  How to INSERT rows in a MySQL table from a Python script
- What ORM means
* How to map a Python Class to a MySQL table

## Table of Contents

- [Tasks](#tasks)
  - [Task 0: Get all states](#task-0-get-all-states)
  - [Task 1: Filter states](#task-1-filter-states)
  - [Task 2: Filter states by user input](#task-2-filter-states-by-user-input)
  - [Task 3: SQL Injection...](#task-3-sql-injection)
  - [Task 4: Cities by states](#task-4-cities-by-states)
  - [Task 5: All cities by state](#task-5-all-cities-by-state)
  - [Task 6: First state model](#task-6-first-state-model)
  - [Task 7: All states via SQLAlchemy](#task-7-all-states-via-sqlalchemy)
  - [Task 8: First state](#task-8-first-state)
  - [Task 9: Contains `a`](#task-9-contains-a)

##More Info
###Install MySQLdb module version 1.3.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 5.7 in Ubuntu 14.04
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
```
##Install SQLAlchemy module version 1.2.x
```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'
```
Also, you can have this warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
You can ignore it.
```
## Tasks

### Task 0: Get all states

**Description:**
Write a script that lists all states from the database hbtn_0e_0_usa.

**Instructions:**
Your script should take 3 arguments: mysql username, mysql password, and database name (no argument validation needed).
You must use the module MySQLdb (import MySQLdb).
Your script should connect to a MySQL server running on localhost at port 3306.
Results must be sorted in ascending order by states.id.
Results must be displayed as they are in the example below.

**Example Usage:**
```
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$ 
...
```

**File Path:**
GitHub repository: alx_python
Directory: python-object_relational_mapping
File: 0-select_states.py

### Task 1: Filter states

**Description:**
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

**Instructions:**
Your script should take 3 arguments: mysql username, mysql password, and database name (no argument validation needed).
You must use the module MySQLdb (import MySQLdb).
Your script should connect to a MySQL server running on localhost at port 3306.
Results must be sorted in ascending order by states.id.
Results must be displayed as they are in the example below.

**Example Usage:**
```sh
$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
...
```

**File Path:**
GitHub repository: alx_python
Directory: python-object_relational_mapping
File: 1-filter_states.py

... (similar sections for other tasks)

