import sqlite3
import pandas as pd
import numpy as np

# step 1: connect to in-memory DB
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# step 2: create a sample table
cursor.execute('''
CREATE TABLE employees (
               id INTEGER,
               name TEXT,
               department TEXT,
               salary INTEGER
               )
''')

# step 3: insert some rows
employees = [
    (1, 'Alice', 'Sales', 50000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'IT', 55000)
]

cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees)
conn.commit()

# step 4: Query using pandas
df = pd.read_sql_query('SELECT * FROM employees', conn)
print(df)

# employees in sales department
print(pd.read_sql_query("SELECT * FROM employees WHERE department = 'Sales'", conn))

# employees earning more than 50000
print(pd.read_sql_query('SELECT department, AVG(salary) as avg_salary FROM employees GROUP BY department', conn))


# top highest paid employees
print(pd.read_sql_query('SELECT * FROM employees ORDER BY salary DESC LIMIT 2', conn))


# Part 2: joining two tables
cursor.execute('''
               CREATE TABLE projects (
               emp_id INTEGER, 
               project TEXT
               )
               ''')

projects = [
    (1, 'Website redesign'),
    (2, 'Ad campaign'),
    (3, 'Network upgrade')
]

cursor.executemany('INSERT INTO projects VALUES (?, ?)', projects)
conn.commit()

# joining two tables
sql = '''
SELECT e.name, e.department, e.salary, p.project
FROM employees e
LEFT JOIN projects p ON e.id = p.emp_id
'''

df_joined = pd.read_sql_query(sql, conn)
print(df_joined)

"""

# LOAD FROM A FILE-BASED DB
conn = sqlite3.connect('yourfile.db')
df.to_sql('your_table', conn, index=False, if_exists='replace')

"""


