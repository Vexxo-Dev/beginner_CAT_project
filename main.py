import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv
import argparse
from tabulate import tabulate
from datetime import datetime

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')


def create_connection():
    """ create a database connection to the MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"Error: '{e}' occurred")
    is_connected = connection.is_connected() if connection else False
    return connection

def create_table(connection):
    """ create tasks table if not exists """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        status VARCHAR(50) DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

def add_task(connection, title, description):
    """ Add a new task to the tasks table """
    insert_task_query = """
    INSERT INTO tasks (title, description) VALUES (%s, %s);
    """
    cursor = connection.cursor()
    cursor.execute(insert_task_query, (title, description))
    connection.commit()
    cursor.close()
    print("Task added successfully.")

def list_tasks(connection):
    """ List all tasks from the tasks table """
    select_tasks_query = "SELECT id, title, description, status, created_at FROM tasks;"
    cursor = connection.cursor()
    cursor.execute(select_tasks_query)
    rows = cursor.fetchall()
    cursor.close()
    if rows:
        print(tabulate(rows, headers=["ID", "Title", "Description", "Status", "Created At"], tablefmt="grid"))
    else:
        print("No tasks found.")

def update_task_status(connection, task_id, status):
    """ Update the status of a task """
    update_status_query = "UPDATE tasks SET status = %s WHERE id = %s;"
    cursor = connection.cursor()
    cursor.execute(update_status_query, (status, task_id))
    connection.commit()
    cursor.close()
    print("Task status updated successfully.")

def main():
    parser = argparse.ArgumentParser(description="To-Do List CLI")
    parser.add_argument('--add', nargs=2, metavar=('TITLE', 'DESCRIPTION'), help="Add a new task")
    parser.add_argument('--list', action='store_true', help="List all tasks")
    args = parser.parse_args()
    connection = create_connection()
    create_table(connection)
    if args.add:
        title, description = args.add
        add_task(connection, title, description)
    elif args.list:
        list_tasks(connection)
    else:
        parser.print_help()
    if connection and connection.is_connected():
        connection.close()
if __name__ == "__main__":
    main()