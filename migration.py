import psycopg2

DB_PARAMS = {
    "dbname": "template1",
    "user": "anar",
    "password": "",
    "host": "",
    "port": "5432"
}

STUDENTS_MIGRATION_SQL = [
    "ALTER TABLE students ADD COLUMN student_id INT;",
    "UPDATE students SET student_id = st_id;",
    "ALTER TABLE students ALTER COLUMN st_name TYPE VARCHAR(30);",
    "ALTER TABLE students ALTER COLUMN st_last TYPE VARCHAR(30);",
    "ALTER TABLE students DROP COLUMN st_id;"
]

INTERESTS_MIGRATION_SQL = [
    "ALTER TABLE interests ADD COLUMN interests VARCHAR(15)[];",
    "INSERT INTO interests(student_id, interests) SELECT student_id, ARRAY_AGG(interest) FROM interests GROUP BY(student_id);",
    "DELETE FROM interests WHERE interests.interests IS NULL;",
    "ALTER TABLE interests DROP COLUMN interest;"
]

def connect_to_database():
    return psycopg2.connect(**DB_PARAMS)

def execute_migration(cur, migration_sql):
    try:
        for sql in migration_sql:
            cur.execute(sql)
        print("Migration successful.")
    except psycopg2.Error as e:
        cur.connection.rollback()
        print(f"Migration failed: {e}")
        raise

def migrate_students_table(cur):
    execute_migration(cur, STUDENTS_MIGRATION_SQL)

def migrate_interests_table(cur):
    execute_migration(cur, INTERESTS_MIGRATION_SQL)

def migrate():
    with connect_to_database() as conn:
        with conn.cursor() as cur:
            migrate_students_table(cur)
            migrate_interests_table(cur)
            conn.commit()

if __name__ == "__main__":
    migrate()
