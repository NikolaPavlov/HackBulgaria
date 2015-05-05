import sqlite3


class CompanyMaker:

    def __init__(self):
        self.db = sqlite3.connect('company.sqlite')
        self.db.row_factory = sqlite3.Row # allow reference by name
        self.cursor = self.db.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY,
                name TEXT,
                monthly_salary INT,
                yearly_bonus INT,
                position TEXT);''')

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        query = '''
            INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?);
            '''
        self.cursor.execute(query, (name, monthly_salary, yearly_bonus, position))
        self.db.commit()

    def list_employees(self):
        query = '''
            SELECT name, position FROM employees;
            '''
        return self.cursor.execute(query)

    def monthly_spendings(self):
        query = '''
            SELECT monthly_salary FROM employees;
            '''
        return sum([sum(x) for x in self.cursor.execute(query)])

    def yearly_spendings(self):
        query = '''
        SELECT yearly_bonus FROM employees;
        '''
        return self.monthly_spendings() + sum([sum(x) for x in self.cursor.execute(query)])

    def delete_employee(self, employee_id):
        query = '''
            DELETE FROM employees WHERE id = ?
            '''
        self.cursor.execute(query, (employee_id,))

    def update_employee(self, emp_id, emp_name, emp_monthly_salary, emp_yearly_bonus, emp_position):
        query = '''
            UPDATE employees SET name = ?,
            monthly_salary = ?,
            yearly_bonus = ?,
            position = ?
            WHERE id = ?
            '''
        self.cursor.execute(query, (emp_name,
            emp_monthly_salary,
            emp_yearly_bonus,
            emp_position,
            emp_id))
