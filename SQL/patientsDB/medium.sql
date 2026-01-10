-- Show unique birth years from patients and order them by ascending.
SELECT distinct year(birth_date) FROM patients order by birth_date asc;

-- Show unique first names from the patients table which only occurs once in the list.
SELECT distinct first_name FROM patients group by first_name having count(first_name) = 1;
