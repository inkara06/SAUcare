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
    # 1) View the first lines of billing
    "Billing sample": "SELECT * FROM billing LIMIT 10;",

    # 2) Oncologists
    "Oncology doctors": "SELECT first_name, last_name, specialization FROM doctors WHERE specialization = 'Oncology' ORDER BY last_name;",

    # 3) Experience of doctors by specialization
    "Doctors experience stats": "SELECT specialization, AVG(years_experience) AS avg_experience, MIN(years_experience) AS min_experience, MAX(years_experience) AS max_experience FROM doctors GROUP BY specialization ORDER BY avg_experience DESC;",

    # 4)Doctors and patients through appointments (INNER JOIN)
    "Doctor-patient pairs": "SELECT d.doctor_id, d.last_name || ' ' || d.first_name AS doctor_name, p.patient_id, p.last_name || ' ' || p.first_name AS patient_name FROM Doctors d INNER JOIN Appointments a ON d.doctor_id = a.doctor_id INNER JOIN Patients p ON a.patient_id = p.patient_id;",
}

# Execute and print results
for title, query in queries.items():
    print(f"\n▶ {title}")
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Save to CSV
    if rows:
        df = pd.DataFrame(rows)
        df.to_csv(f"output_{title.replace(' ', '_').lower()}.csv", index=False)

# Close connection
cur.close()
conn.close()
print("\n Connection closed")
