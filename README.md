# This README includes 3 instructions: 
## 1. Prerequisites for running the files <br />2. Migration and Rollback intructions <br />3.Detailed explaination of both Migration and Rollback files. <br /> 

### Prerequisites

1. PostgreSQL installed on your system.
2. Python installed on your system.
3. psycopg2 library installed for Python. <br />You can install it via pip
      ``` pip install psycopg2 ```

### Migration Instructions

1. **Configure Database Parameters**: <br />
Open both migration.py and rollback.py files in a code editor.

Replace the placeholder values in **DB_PARAMS** dictionary with your PostgreSQL database parameters. Make sure you replace entities such as **dbname**, **user**, **password**, **host**, and **port**.

2. **Migration File**:<br />
* Open migration.py. This file contains migration SQL commands for "students" and "interests" tables.
* Each SQL command is stored in lists STUDENTS_MIGRATION_SQL and INTERESTS_MIGRATION_SQL respectively, ensuring a sequential execution of SQL commands.
* The ```connect_to_database()``` function establishes a connection to the PostgreSQL database using the provided parameters.
* The ```execute_migration()``` function takes a cursor and a list of SQL commands, executes each command one by one, and handles any errors.
* The ```migrate_students_table()``` and ```migrate_interests_table()``` functions call ```execute_migration()``` with the respective SQL lists.
* The ```migrate()``` function runs the migration process, executing SQL commands for both tables within a transaction and committing changes if successful.
* To run Migration, type the following command ```python migration.py```
   
