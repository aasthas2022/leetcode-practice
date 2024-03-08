/* 1587. Bank Account Summary II - https://leetcode.com/problems/bank-account-summary-ii/ */

select Users.name as name, sum(Transactions.amount) as balance 
from Users
join Transactions
on Users.account = Transactions.account
group by Users.account
having balance > 10000