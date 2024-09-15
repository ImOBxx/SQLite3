import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employee(
            first text,
            last text,
            pay integer
            )""")


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

print(emp_1.first)


c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 500000)")

conn.commit()

c.execute("SELECT * FROM employees WHERE last = 'Smith'")

print(c.fetchone())

conn.commit()

conn.close()

