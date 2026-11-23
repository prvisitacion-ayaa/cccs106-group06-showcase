import sqlite3
from pathlib import Path


DATABASE_FILE = Path(__file__).parent / "learn2earn.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_FILE)

    # enable foreign key constraints
    connection.execute("PRAGMA foreign_keys = ON")

    return connection

def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL,
            course TEXT DEFAULT '',
            year_level TEXT DEFAULT '',
            role TEXT NOT NULL DEFAULT 'student',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            subject TEXT,
            topic TEXT,
            course TEXT,
            description TEXT,
            file_path TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS note_evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note_id INTEGER NOT NULL,
            accuracy_score REAL,
            assessment_label TEXT,
            evaluation_summary TEXT,
            supported_information TEXT,
            insufficiently_supported_information TEXT,
            reference_materials TEXT,
            evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (note_id) REFERENCES notes(id)
                ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learnpoints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            points INTEGER NOT NULL,
            reason TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS premium_features (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature_name TEXT NOT NULL UNIQUE,
            description TEXT,
            points_required INTEGER NOT NULL CHECK (points_required > 0),
            is_available INTEGER NOT NULL DEFAULT 1
                CHECK (is_available IN (0, 1))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS premium_redemptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            feature_id INTEGER NOT NULL,
            points_used INTEGER NOT NULL CHECK (points_used > 0),
            redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (feature_id) REFERENCES premium_features(id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moderation_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note_id INTEGER NOT NULL,
            admin_id INTEGER,
            decision TEXT NOT NULL,
            remarks TEXT,
            moderated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (note_id) REFERENCES notes(id)
                ON DELETE CASCADE,
            FOREIGN KEY (admin_id) REFERENCES users(id)
        )
    """)


    # add source note id to track notes who earned points
    cursor.execute("PRAGMA table_info(learnpoints)")
    columns = [column[1] for column in cursor.fetchall()]

    if "source_note_id" not in columns:
        cursor.execute("""
            ALTER TABLE learnpoints
            ADD COLUMN source_note_id INTEGER
            REFERENCES notes(id) ON DELETE SET NULL
        """)

    # prevent the same note from earning points more than once
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS
        idx_learnpoints_source_note_unique
        ON learnpoints(source_note_id)
        WHERE source_note_id IS NOT NULL
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("Database created successfully!")
    print("Database location:", DATABASE_FILE)