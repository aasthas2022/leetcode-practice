/* 1484. Group Sold Products By The Date - https://leetcode.com/problems/group-sold-products-by-the-date/ */

select sell_date, count(distinct product) as num_sold, GROUP_CONCAT(distinct product order by product ASC) as products
from activities
group by sell_date