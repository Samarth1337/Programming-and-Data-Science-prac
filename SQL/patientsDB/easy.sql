-- Show first name, last name, and gender of patients whose gender is 'M'
SELECT first_name, last_name, gender FROM patients where gender is 'M';

-- Show first name and last name of patients who does not have allergies. (null)
SELECT first_name, last_name FROM patients where allergies is null;

-- Show first name of patients that start with the letter 'C'
SELECT first_name FROM patients where first_name like 'C%';

-- Show first name and last name of patients that weight within the range of 100 to 120 (inclusive)
SELECT first_name, last_name FROM patients where weight >= 100 and weight <= 120;
SELECT first_name, last_name FROM patients WHERE weight BETWEEN 100 AND 120;

-- Show unique birth years from patients and order them by ascending.
SELECT distinct year(birth_date) FROM patients order by birth_date asc;