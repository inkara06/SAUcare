import psycopg2
import pandas as pd

# Database connection settings
DB_NAME = "db_name" #replace with your postgres database name
DB_USER = "user" #replace with your postgres username
DB_PASS = ""  # replace with your postgres password
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    print(" Connected to database successfully")
except Exception as e:
    print("Connection error:", e)
    exit()

# Create a cursor
cur = conn.cursor()

# 10 analytical queries
queries = {
   "Patients by gender": """
        SELECT gender, COUNT(*) AS total_patients
        FROM patients
        GROUP BY gender;
    """,
    "Average patient age": """
        SELECT ROUND(AVG(EXTRACT(YEAR FROM AGE(current_date, date_of_birth)))) AS avg_age
        FROM patients;
    """,
    "Doctors by specialization": """
        SELECT specialization, COUNT(*) AS total_doctors
        FROM doctors
        GROUP BY specialization
        ORDER BY total_doctors DESC;
    """,
    "Average doctor experience": """
        SELECT ROUND(AVG(years_experience), 2) AS avg_experience
        FROM doctors;
    """,
    "Appointments per doctor": """
        SELECT d.doctor_id, d.first_name || ' ' || d.last_name AS doctor_name,
               COUNT(a.appointment_id) AS total_appointments
        FROM doctors d
        LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
        GROUP BY d.doctor_id, doctor_name
        ORDER BY total_appointments DESC;
    """,
    "Average appointments per patient": """
        SELECT ROUND(AVG(appt_count), 2) AS avg_appointments_per_patient
        FROM (
            SELECT p.patient_id, COUNT(a.appointment_id) AS appt_count
            FROM patients p
            LEFT JOIN appointments a ON p.patient_id = a.patient_id
            GROUP BY p.patient_id
        ) sub;
    """,
    "Total invoiced amount": """
        SELECT SUM(amount) AS total_billed
        FROM billing;
    """,
    "Revenue by payment method": """
        SELECT payment_method, SUM(amount) AS total_amount
        FROM billing
        GROUP BY payment_method;
    """,
    "Most expensive procedures": """
        SELECT treatment_type, MAX(cost) AS max_cost
        FROM treatments
        GROUP BY treatment_type
        ORDER BY max_cost DESC
        LIMIT 5;
    """,
    "Completed appointments by month": """
        SELECT DATE_TRUNC('month', appointment_date) AS month,
               COUNT(*) AS completed_appointments
        FROM appointments
        WHERE status = 'Completed'
        GROUP BY month
        ORDER BY month;
    """
}

for name, query in queries.items():
    print(f"\n--- {name} ---")
    df = pd.read_sql(query, conn)
    print(df)

  
    file_name = name.lower().replace(" ", "_") + ".csv"
    df.to_csv(file_name, index=False)
    print(f"Saved to {file_name}")

conn.close()
