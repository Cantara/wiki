# MS SQL Server

###### Drop unique constraint

http://stackoverflow.com/questions/3001103/i<sub>~need</sub><sub>to</sub><sub>remove</sub><sub>a</sub><sub>unique</sub><sub>constraints</sub><sub>that</sub><sub>i</sub><sub>dont</sub><sub>know</sub><sub>the</sub>~names-of

```sql
DECLARE @table_name nvarchar(256)
DECLARE @col_name nvarchar(256)
DECLARE @Command  nvarchar(1000)

-- set your table and column name here:
SET @table_name = N'tableName'
SET @col_name = N'columnName'

SELECT @Command = 'ALTER TABLE ' + @table_name + ' DROP CONSTRAINT ' + d.name
FROM sys.tables t
  JOIN sys.indexes d ON d.object_id = t.object_id  AND d.type=2 and d.is_unique=1
  JOIN sys.index_columns ic on d.index_id=ic.index_id and ic.object_id=t.object_id
  JOIN sys.columns c on ic.column_id = c.column_id  and c.object_id=t.object_id
WHERE t.name = @table_name and c.name=@col_name

--if you want to preview the generated command before running
SELECT @Command
--EXEC sp_executesql @Command;
```

###### Drop foreign key

```sql
DECLARE @ConstraintName nvarchar(200)
SELECT
  @ConstraintName = KCU.CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS AS RC
  INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KCU
    ON KCU.CONSTRAINT_CATALOG = RC.CONSTRAINT_CATALOG
       AND KCU.CONSTRAINT_SCHEMA = RC.CONSTRAINT_SCHEMA
       AND KCU.CONSTRAINT_NAME = RC.CONSTRAINT_NAME
WHERE
  KCU.TABLE_NAME = 'tableName' AND
  KCU.COLUMN_NAME = 'columnName'

print @ConstraintName

--EXEC('ALTER TABLE [dbo].[tableName] DROP CONSTRAINT ' + @ConstraintName)
```
