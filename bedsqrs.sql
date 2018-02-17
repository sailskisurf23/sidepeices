Queries
Using the facility with id 6057, answer the following using SQL.

SQL beds Q1
How many censuses (COUNT) were done at this facility?;

select count(bed_census_date)
from beds
where facility_id = '6057';

select MIN(bed_census_date) as EarliestDate
from beds
where facility_id = '6057';

select bed_census_date
from beds
where facility_id = '6057';

SELECT MIN(date) as EarliestDate
FROM YourTable
WHERE id = 2;

/* Select the facility_id, facility_name, available_residential_beds combinations from the table so that the
 available_residential_beds is the maximum for that facility_id across all time (so there should be
 one record per facility_id). */

 select facility_id, MAX(facility_name), MAX(available_residential_beds) from beds
 order by MAX(available_residential_beds)
 group by facility_id
;



select facility_id, MIN(facility_name) as facility_name, MAX(available_residential_beds) as max_available_residential_beds from beds
group by facility_id
order by MAX
;

 select facility_id, COUNT(facility_name)
 from beds
 group by facility_id;

 select facility_name
 from beds
 where facility_id = '0533';
