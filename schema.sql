CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender CHAR(1),
    date_of_birth DATE,
    contact_number TEXT,
    address TEXT,
    registration_date DATE,
    insurance_provider TEXT,
    insurance_number TEXT,
    email TEXT
);
CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender CHAR(1),
    date_of_birth DATE,
    contact_number TEXT,
    address TEXT,
    registration_date DATE,
    insurance_provider TEXT,
    insurance_number TEXT,
    email TEXT
);
CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender CHAR(1),
    date_of_birth DATE,
    contact_number TEXT,
    address TEXT,
    registration_date DATE,
    insurance_provider TEXT,
    insurance_number TEXT,
    email TEXT
);
CREATE TABLE treatments (
    treatment_id TEXT PRIMARY KEY,
    appointment_id TEXT REFERENCES appointments(appointment_id),
    treatment_type TEXT,
    description TEXT,
    cost NUMERIC(10,2),
    treatment_date DATE
);
CREATE TABLE billing (
    bill_id TEXT PRIMARY KEY,
    patient_id TEXT REFERENCES patients(patient_id),
    treatment_id TEXT REFERENCES treatments(treatment_id),
    bill_date DATE,
    amount NUMERIC(10,2),
    payment_method TEXT,
    payment_status TEXT
);



