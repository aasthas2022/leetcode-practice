/* 1795. Rearrange Products Table - https://leetcode.com/problems/rearrange-products-table */


/**
Learnings:

`UNION ALL` is a SQL operator used to combine the results of two or more SELECT statements into a single result set. Here's how it works:

1. Combining Results: When you use `UNION ALL`, it concatenates the result sets of all the SELECT statements together. This means that it takes all rows returned by each SELECT statement and puts them one after another in the result set.

2. Duplicate Rows: Unlike `UNION`, which removes duplicate rows from the result set, `UNION ALL` retains all rows, including duplicates. This can be useful if you want to include all rows from both SELECT statements, even if they are identical.

3. Column Matching: The columns selected in each SELECT statement must match in number and data type. The column names in the result set are typically determined by the column names in the first SELECT statement.

4. Order: The order of rows in the final result set is not guaranteed unless you use an ORDER BY clause.

For example, if you have two tables with the same structure and you want to combine their contents vertically, you can use `UNION ALL`. Here's a basic example:

```sql
SELECT column1, column2 FROM table1
UNION ALL
SELECT column1, column2 FROM table2;
```

This query will return all rows from `table1` followed by all rows from `table2`, without removing any duplicates. If you want to remove duplicates, you can simply replace `UNION ALL` with `UNION`.

**/
select product_id, 'store1' as store, store1 as price from products where store1 is not null
union all
select product_id, 'store2' as store, store2 as price from products where store2 is not null
union all
select product_id, 'store3' as store, store3 as price from products where store3 is not null