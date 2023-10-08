use parts;

select * from part;
select * from project;
select * from supplier;
select * from supply;


# Find the name of each part where the weight is less than 14.
select * from part
where weight < 14;

# Find all unique supplier(s) where their status is equal to 30.

select * from supplier
where status = 30

