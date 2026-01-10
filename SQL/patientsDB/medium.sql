-- Show unique birth years from patients and order them by ascending.
SELECT distinct year(birth_date) FROM patients order by birth_date asc;

-- Show unique first names from the patients table which only occurs once in the list.
SELECT distinct first_name FROM patients group by first_name having count(first_name) = 1;

-- Show patient_id and first_name from patients where their first_name start and ends with 's' and is at least 6 characters long.
select patient_id, first_name from patients where first_name like 'S%S' and length(first_name) >= 6;

-- Show patient_id, first_name, last_name from patients whos diagnosis is 'Dementia'.
-- Primary diagnosis is stored in the admissions table.
select patients.patient_id, first_name, last_name from patients join admissions on patients.patient_id = admissions.patient_id where diagnosis = 'Dementia';

-- Display every patient's first_name.
-- Order the list by the length of each name and then by alphabetically.
select first_name from patients order by len(first_name), first_name;