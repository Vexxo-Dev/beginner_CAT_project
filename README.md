# 📝 To-Do List CLI

A simple yet powerful command-line interface (CLI) application for managing your tasks, built with Python and MySQL.

## ✨ Features

- **Add Tasks**: Create new tasks with titles and descriptions
- **List Tasks**: View all your tasks in a beautifully formatted table
- **Update Status**: Mark tasks as completed or change their status
- **Database Persistence**: All tasks are stored in a MySQL database

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **MySQL**: Database for persistent storage
- **mysql-connector-python**: MySQL database connector
- **python-dotenv**: Environment variable management
- **argparse**: Command-line argument parsing
- **tabulate**: Beautiful table formatting in the terminal

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.x installed
- MySQL server installed and running
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vexxo-Dev/beginner_CAT_project,git
   cd beginner_CAT_project
   ```

2. **Install required packages**
   ```bash
   pip install mysql-connector-python python-dotenv tabulate
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root directory:
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_DATABASE=your_database_name
   DB_USERNAME=your_username
   DB_PASSWORD=your_password
   ```

4. **Create the database**
   
   Log into MySQL and create a database:
   ```sql
   CREATE DATABASE your_database_name;
   ```

## 💻 Usage

### Add a New Task

```bash
python main.py --add "Task Title" "Task Description"
```

**Example:**
```bash
python main.py --add "Buy groceries" "Get milk, bread, and eggs from the store"
```

### List All Tasks

```bash
python main.py --list
```

This will display all tasks in a formatted table showing:
- ID
- Title
- Description
- Status
- Created At (timestamp)

### Get Help

```bash
python main.py --help
```

## 📊 Database Schema

The application automatically creates a `tasks` table with the following structure:

| Column      | Type         | Description                    |
|-------------|--------------|--------------------------------|
| id          | INT          | Auto-incrementing primary key  |
| title       | VARCHAR(255) | Task title                     |
| description | TEXT         | Task description               |
| status      | VARCHAR(50)  | Task status (default: pending) |
| created_at  | TIMESTAMP    | Creation timestamp             |

## 🔒 Environment Variables

| Variable     | Description                    | Example       |
|--------------|--------------------------------|---------------|
| DB_HOST      | MySQL server host              | localhost     |
| DB_PORT      | MySQL server port              | 3306          |
| DB_DATABASE  | Database name                  | todo_db       |
| DB_USERNAME  | MySQL username                 | root          |
| DB_PASSWORD  | MySQL password                 | password123   |

This Project is task for submiting at CAT Reloaded 