import sqlite3
import csv

DB_NAME = "mistakes.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mistakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_feedback TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_mistake(user_input, bot_feedback):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mistakes (user_input, bot_feedback) VALUES (?, ?)", (user_input, bot_feedback))
    conn.commit()
    conn.close()

def get_mistake_summary():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT user_input, bot_feedback FROM mistakes")
    mistakes = cursor.fetchall()
    conn.close()
    return mistakes

def clear_mistakes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mistakes")
    conn.commit()
    conn.close()

def export_mistakes_to_file(filename="mistakes_export.csv"):
    mistakes = get_mistake_summary()
    with open(filename, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["User Input", "Bot Feedback"])
        writer.writerows(mistakes)
