import sqlite3


class Query:

    def __init__(self):
        self.conn = sqlite3.connect('northwind.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

# List all employees with their first name, last name and title.
    def list_emp_names(self):
        query = '''
            SELECT FirstName, LastName, Title FROM Employees;
            '''
        for emp in self.cursor.execute(query):
            print('{}|---|{}|---|{}'.format(emp['FirstName'], emp['LastName'], emp['Title']))

# List all employees from Seattle.
    def list_emp_from_Seattle(self):
        query = '''
            SELECT FirstName, LastName FROM Employees WHERE City='Seattle';
        '''
        for emp in self.cursor.execute(query):
            print('{}|---|{}'.format(emp['FirstName'], emp['LastName']))

# List all employees from London.!!!!!!!
    def list_emp_from_London(self):
        query = '''
            SELECT FirstName, LastName FROM Employees WHERE City='London';
        '''
        for emp in self.cursor.execute(query):
            print('{}|---|{}'.format(emp['FirstName'], emp['LastName']))

# List all employees that work in the Sales department.
    def list_emp_in_sales_dep(self):
        query = """
            Select * FROM employees where Title LIKE '%Sales%';
        """
        for emp in self.cursor.execute(query):
            print('{}|---|{}|---|{}'.format(emp['FirstName'], emp['LastName'], emp['Title']))

# List all females employees that work in the Sales department.
    def list_all_female_from_sales(self):
        query = """
            Select * FROM employees where Title LIKE '%Sales%' AND (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.');
        """
        for emp in self.cursor.execute(query):
            print('{}|---|{}|---|{}|---|{}'.format(emp['FirstName'], emp['LastName'], emp['Title'], emp['TitleOfCourtesy']))

# List the 5 oldest employees.
    def list_5_oldest_emp(self):
        query = """
            SELECT * FROM employees ORDER BY BirthDate LIMIT 5;
        """
        for emp in self.cursor.execute(query):
            print('{}|---|{}|---|{}'.format(emp['FirstName'], emp['LastName'], emp['BirthDate']))

# List the first 5 hires of the company.
    def list_first_5_hires_in_comp(self):
        query = """
            SELECT * FROM employees ORDER BY HireDate LIMIT 5;
        """
        for emp in self.cursor.execute(query):
            print('{}|---|{}|---|{}'.format(emp['FirstName'], emp['LastName'], emp['HireDate']))

# List the employee who reports to no one (the boss)
    def list_emp_reports_to_noone(self):
        '''
        check for empty cell with null !!!
        '''
        query = """
            SELECT * FROM employees WHERE ReportsTo IS null;
        """
        for emp in self.cursor.execute(query):
            print('{}|---|{}|---|{}'.format(emp['FirstName'], emp['LastName'], emp['ReportsTo']))

# List all employes by their first and last name, and the first and last name of the employees that they report to.
    # WTF WTF

# Count all female employees.
    def count_all_female_emp(self):
        query = """
             Select COUNT(*) FROM employees WHERE (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.');
        """
        for i in self.cursor.execute(query):
            print(i['COUNT(*)'])

# Count all male employees.
    def count_all_male_emp(self):
        query = """
            Select COUNT(*) FROM employees WHERE (TitleOfCourtesy = 'Mr.' OR TitleOfCourtesy = 'Dr.');
        """
        for i in self.cursor.execute(query):
                    print(i['COUNT(*)'])




# Tests
q = Query()
# q.list_emp_names()
# q.list_emp_from_Seattle()
# q.list_emp_from_London()
# q.list_emp_in_sales_dep()
# q.list_all_female_from_sales()
# q.list_5_oldest_emp()
# q.list_first_5_hires_in_comp()
# q.list_emp_reports_to_noone()
# q.count_all_female_emp()
q.count_all_male_emp()

