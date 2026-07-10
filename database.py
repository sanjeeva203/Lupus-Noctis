import sqlite3

DB_NAME = "lupus.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # User table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        telegram_id INTEGER PRIMARY KEY,
        username TEXT,
        streak INTEGER DEFAULT 0,
        discipline_score INTEGER DEFAULT 100
    )
    """)

    # Morning mission
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS missions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        date TEXT,
        physics TEXT,
        maths TEXT,
        physical_chemistry TEXT,
        organic_chemistry TEXT,
        inorganic_chemistry TEXT,
        revision TEXT,
        exercise TEXT,
        sleep_target TEXT,
        submitted_at TEXT
    )
    """)

    # Midday report
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS midday_reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        date TEXT,
        study_hours REAL,
        time_wasted INTEGER,
        distraction TEXT,
        progress TEXT
    )
    """)

    # Night report
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS night_reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        date TEXT,
        total_hours REAL,
        questions INTEGER,
        time_wasted INTEGER,
        pending_tasks TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("Lupus Noctis Database Ready.")