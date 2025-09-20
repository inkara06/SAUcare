# SAUcare
SAUcare is a regional healthcare provider. This repository contains a data analytics project for the hospital management dataset (patients, doctors, appointments, treatments, billing). The goal is to perform operational and financial analytics: patient demographics, doctor activity, appointment statistics, treatment costs and billing analytics.

## ERD Diagram

![ERD](images/erd.png)
Dataset
Files (CSV) used in the project: (archive)
patients.csv — patient demographic and registration details
doctors.csv — doctor metadata
appointments.csv — scheduled/completed/cancelled appointments
treatments.csv — treatments performed during appointments
billing.csv — billing and payment records
ER diagram: images/erd.img 
##Contents of the repository
schema.sql — CREATE TABLE statements for all tables
queries.sql — 10 analytical SQL queries (with short comments)
main.py — Python script to connect to the DB and run sample queries
requirements.txt — Python dependencies
archive/ — CSV files (not included in repo if large)
images/ — ER diagram, screenshots, notes
Quick setup & run instructions
Below are step-by-step instructions so someone (or you) can run the project locally.
1) Prerequisites
macOS / Linux / Windows
PostgreSQL 14 (or compatible) installed and running
pgAdmin (optional)
Python 3.10+
Git and optionally the GitHub CLI gh (for repo creation and pushing)
2) Create virtual environment and install Python dependencies
# in project folder
python3 -m venv venv
source venv/bin/activate    # macOS / Linux
# Windows PowerShell: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
requirements.txt should include at least:
psycopg2-binary
pandas
sqlalchemy
3) Create PostgreSQL database
If PostgreSQL is installed and createdb is available:
createdb hospital_managemnet
Or in psql:
CREATE DATABASE hospital_managemnet;
4) Create tables
Run the schema.sql file (contains CREATE TABLE statements):
psql -U postgres -d hospital_db -f schema.sql
5) Import CSV data
Recommended: use the client-side \copy (works without server file permissions):
# from project root
psql -U postgres -d hospital_db
-- then in psql shell:
\copy patients(patient_id, first_name, last_name, gender, date_of_birth, contact_number, address, registration_date, insurance_provider, insurance_number, email) FROM 'data/patients.csv' CSV HEADER;
\copy doctors(doctor_id, first_name, last_name, specialization, phone_number, years_experience, hospital_branch, email) FROM 'data/doctors.csv' CSV HEADER;
\copy appointments(appointment_id, patient_id, doctor_id, appointment_date, appointment_time, reason_for_visit, status) FROM 'data/appointments.csv' CSV HEADER;
\copy treatments(treatment_id, appointment_id, treatment_type, description, cost, treatment_date) FROM 'data/treatments.csv' CSV HEADER;
\copy billing(bill_id, patient_id, treatment_id, bill_date, amount, payment_method, payment_status) FROM 'data/billing.csv' CSV HEADER;
You can find this queries in queries.sql

If columns in CSV contain prefixed IDs like P001, ensure corresponding table columns are TEXT (not integer).
6) Run analytical queries
Open queries.sql and run queries in pgAdmin or psql to verify results:
psql -U postgres -d hospital_db -f queries.sql
7) Run Python script
main.py connects to the DB, runs a few queries and prints results. Example:
python main.py
Tools & resources
PostgreSQL 14 (server)
pgAdmin (GUI for DB)
Python 3.10+, pip
psycopg2-binary, pandas, sqlalchemy
Apache Superset (optional dashboard)
VS Code / Sublime Text for editing
Kaggle (source data)

Project author: Inkar Usurbayeva
