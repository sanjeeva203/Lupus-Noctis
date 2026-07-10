import sqlite3

DATABASE = "lupus.db"

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        study_hours REAL,
        time_wasted INTEGER,
        discipline_score INTEGER,
        completed_tasks INTEGER,
        pending_tasks INTEGER
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
