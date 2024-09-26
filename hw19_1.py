"""
a:
on delete cascade automatically deletes all records in the employees table that reference
a deleted record in the departments table.


b:
The difference is that a regular foreign key stops you from deleting a table 1 record if there are related to table 2
records, while on delete cascade lets you delete the table 1 record and also removes the related table 2 records
automatically.


c:
on delete cascade can be risky because it might delete important related data without you noticing, but it also helps
keep everything organized by automatically removing any leftover data that's no longer needed.
"""