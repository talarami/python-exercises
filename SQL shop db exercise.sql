use shop;

# Find out how many sales (amount) were recorded each week, per day

select week, day, sum(SalesAmount) as TotalSalesAmount
from sales1
group by week, day
order by week, day;

# Change the name of salesperson Inga to be Annette instead, but only where
# Ignas Sales are <20.

update sales1
set SalesPerson = replace(SalesPerson, "Inga", "Annette")
where SalesAmount < 20;

# Find out how many sales the Dusseldorf office logged
# Note we’re looking for quantity here - e.g. if Dusseldorf did 6 sales, then the output would be 6

select count(Store)
from sales1
where Store = "Dusseldorf";

# Find the total (sum) sales amount by each person by day

select day, SalesPerson, sum(SalesAmount) as SumOfSales
from sales1 
group by day, SalesPerson
order by day, SalesPerson;

# How much (sum) each person sold for between week 2 and week 4

select SalesPerson, sum(SalesAmount) as PersonSales
from sales1
where week between 2 and 4
group by SalesPersonSalesPerson
order by SalesPerson;

# For each store:

# The total of their sales;
select Store, sum(SalesAmount)
from sales1
group by Store
order by Store;

# The number of sales;
select Store, count(SalesAmount)
from sales1
group by Store
order by Store;

# Their average sales;
select Store, avg(SalesAmount)
from sales1
group by Store
order by Store;

# Their lowest sales amount;
select Store, min(SalesAmount)
from sales1
group by Store
order by Store;

# Their highest sales amount.
select Store, max(SalesAmount)
from sales1
group by Store
order by Store;

# Count the number of sales by each person if they had more than or equal to 2 sales for the past period

select month, SalesPerson, count(SalesAmount)
from sales1
where SalesAmount >= 2
group by month, SalesPerson
order by month, SalesPerson;

# Count the number of sales by each person if they had more than or equal to 2 sales for the past period

select SalesPerson, count(SalesAmount) as AllSales
from sales1
where week between 2 and 4
group by SalesPerson
having count(SalesAmount) >= 2;

# Find the number (count) of sales by each person, but only if they made less than £300 worth of sales for the past period.

select SalesPerson, count(SalesAmount)
from sales1
where week between 2 and 4
group by SalesPerson
having sum(SalesAmount) < 300;

select * from sales1;
