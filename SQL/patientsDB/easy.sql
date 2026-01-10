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

-- Show first name and last name concatenated into one column to show their full name.
SELECT concat(first_name," ", last_name) as full_name FROM patients;

-- Show first name, last name, and the full province name of each patient. Example: 'Ontario' instead of 'ON'
SELECT first_name, last_name, province_name FROM patients join province_names on province_names.province_id = patients.patient_id;

-- Show how many patients have a birth_date with 2010 as the birth year.
select COUNT(*) from patients where year(birth_date) = 2010;

-- Show the first_name, last_name, and height of the patient with the greatest height.
select first_name, last_name, MAX(height) from patients;

-- Show all columns for patients who have one of the following patient_ids:
-- 1,45,534,879,1000
select * from patients where patient_id in (1,45,534,879,1000);