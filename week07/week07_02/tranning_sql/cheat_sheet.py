'''
    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index
'''

SELECT column_name FROM table_name
SELECT column_name FROM table_name WHERE 1 = 1
SELECT column_name FROM table_name WHERE 1 = 1 AND 2 = 2
SELECT column_name FROM table_name WHERE 1 = 1 OR 3 = 4
INSERT INTO table_name VALUES(value1, value2, value3)
UPDATE table_name SET column1=value1,column2=value2 WHERE some_column=some_value;






