--1. Number of patients by gender
SELECT gender, COUNT(*) AS total_patients
FROM patients
GROUP BY gender;
--2. Average age of patients
SELECT ROUND(AVG(EXTRACT(YEAR FROM AGE(current_date, date_of_birth)))) AS avg_age
FROM patients;
--3.Number of doctors by specialization
SELECT specialization, COUNT(*) AS total_doctors
FROM doctors
GROUP BY specialization
ORDER BY total_doctors DESC;

-- 4. Average work experience of doctors
SELECT ROUND(AVG(years_experience), 2) AS avg_experience
FROM doctors;

-- 5. Number of appointments with each doctor
SELECT d.doctor_id, d.first_name || ' ' || d.last_name AS doctor_name,
       COUNT(a.appointment_id) AS total_appointments
FROM doctors d
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, doctor_name
ORDER BY total_appointments DESC;


-- 6. Average number of appointments per patient
SELECT ROUND(AVG(appt_count), 2) AS avg_appointments_per_patient
FROM (
    SELECT p.patient_id, COUNT(a.appointment_id) AS appt_count
    FROM patients p
    LEFT JOIN appointments a ON p.patient_id = a.patient_id
    GROUP BY p.patient_id
) sub;
-- 7. Total invoiced amount
SELECT SUM(amount) AS total_billed
FROM billing;

-- 8. Revenue by payment method
SELECT payment_method, SUM(amount) AS total_amount
FROM billing
GROUP BY payment_method;
-- 9. Most expensive procedures
SELECT treatment_type, MAX(cost) AS max_cost
FROM treatments
GROUP BY treatment_type
ORDER BY max_cost DESC
LIMIT 5;

-- 10. Number of completed appointments by month
SELECT DATE_TRUNC('month', appointment_date) AS month,
       COUNT(*) AS completed_appointments
FROM appointments
WHERE status = 'Completed'
GROUP BY month
ORDER BY month;

