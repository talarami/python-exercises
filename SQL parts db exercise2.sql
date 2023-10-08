use parts;

select * from part;
select * from project;
select * from supplier;
select * from supply;

# Return the PartID, Colour and Supplier name, where the supplier’s surname 
# contains ‘LA’ (can be preceded or followed by other characters), and the Supplier city is not Athens. Ensure the values are Unique.

# distinct returns only different values

select distinct part.p_id as PartID, part.colour as Colour, supplier.sname as SupplierName 
from part
inner join supply on part.p_id = supply.p_id
inner join supplier on supply.s_id = supplier.s_id
where supplier.sname like '%LA%'
and supplier.city != 'ATHENS';

# Return the supplier name, part name and project name for each case where the following conditions are true:
# The supplier supplies a project with a part;
# And where the supplier’s city, project city and part city are all different.

select supplier.sname as SupplierName, part.pname as PartName, project.jname as ProjectName
from supply 
inner join supplier on supply.s_id = supplier.s_id
inner join part on supply.p_id = part.p_id
inner join project on supply.j_id = project.j_id
where supplier.city != project.city and supplier.city != part.city and project.city != part.city;


