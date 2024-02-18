import psycopg2

DB_PARAMS = {
    "dbname": "template1",
    "user": "anar",
    "password": "",
    "host": "",
    "port": "5432"
}

ROLLBACK_SQL = [
    """
    ALTER TABLE students 
    ADD COLUMN st_id INT,
    ALTER COLUMN st_name TYPE VARCHAR(30),
    ALTER COLUMN st_last TYPE VARCHAR(30),
    DROP COLUMN student_id;
    """,
    """
    ALTER TABLE interests 
    ADD COLUMN interest VARCHAR(15);

    INSERT INTO interests(student_id, interest) 
    SELECT student_id, unnest(interests) 
    FROM interests;

    DELETE FROM interests 
    WHERE interest IS NULL;

    ALTER TABLE interests 
    DROP COLUMN interests;
    """
]

def connect_to_database():
    return psycopg2.connect(**DB_PARAMS)

def execute_rollback(cur):
    try:
        for sql in ROLLBACK_SQL:
            cur.execute(sql)
        print("Rollback successful.")
    except psycopg2.Error as e:
        cur.connection.rollback()
        print(f"Rollback failed: {e}")
        raise

def rollback():
    with connect_to_database() as conn:
        with conn.cursor() as cur:
            execute_rollback(cur)
            conn.commit()

if __name__ == "__main__":
    rollback()
