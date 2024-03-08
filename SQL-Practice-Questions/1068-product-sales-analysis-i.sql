/* 1068. Product Sales Analysis I - https://leetcode.com/problems/product-sales-analysis-i */

select p.product_name, s.year, s.price
from sales as s
left join product as p on s.product_id = p.product_id;
