import sqlite3


class CompanyMaker:

    def __init__(self):
        self.db= sqlite3.connect('company.sqlite')
        self.cursor = self.db.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY,
                name TEXT,
                monthly_salary INT,
                yearly_bonus INT,
                position TEXT)''')

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        query = '''
            INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)
            '''
        self.cursor.execute(query, (name, monthly_salary, yearly_bonus, position))
        self.db.commit()

    def list_employees(self):
        query = '''
            SELECT name, position FROM employees
            '''
        return self.cursor.execute(query)





# TESTS
# cm = CompanyMaker()
# cm.add_employee('gogo', 100, 1111, 'drinker')
# print(cm.list_employees())
