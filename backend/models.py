from db_config import get_db_connection

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def get_all_todos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return todos

def add_todo(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (title) VALUES (%s)", (title,))
    conn.commit()
    cursor.close()
    conn.close()

def update_todo(todo_id, completed):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET completed=%s WHERE id=%s", (completed, todo_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_todo(todo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id=%s", (todo_id,))
    conn.commit()
    cursor.close()
    conn.close()
