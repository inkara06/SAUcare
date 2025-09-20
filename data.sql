COPY patients(patient_id, first_name, last_name, gender, date_of_birth, contact_number, address, registration_date, insurance_provider, insurance_number, email)
FROM '/path/to/patients.csv'
DELIMITER ','
CSV HEADER;

COPY doctors(doctor_id, first_name, last_name, specialization, phone_number, years_experience, hospital_branch, email)
FROM '/path/to/doctors.csv'
DELIMITER ','
CSV HEADER;

COPY appointments(appointment_id, patient_id, doctor_id, appointment_date, appointment_time, reason_for_visit, status)
FROM '/path/to/appointments.csv'
DELIMITER ','
CSV HEADER;

COPY treatments(treatment_id, appointment_id, treatment_type, description, cost, treatment_date)
FROM '/path/to/treatments.csv'
DELIMITER ','
CSV HEADER;


COPY billing(bill_id, patient_id, treatment_id, bill_date, amount, payment_method, payment_status)
FROM '/path/to/billing.csv'
DELIMITER ','
CSV HEADER;
