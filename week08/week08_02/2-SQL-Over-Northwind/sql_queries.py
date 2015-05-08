import sqlite3


class Query:

    def __init__(self):
        self.conn = sqlite3.connect('northwind.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

# 1. List all employees with their first name, last name and title.
    def list_emp_names(self):
        query = '''
            SELECT FirstName, LastName, Title FROM Employees;
            '''
        for emp in self.cursor.execute(query):
            print('{} |---| {} |---| {}'.format(
                emp['FirstName'], emp['LastName'], emp['Title']))

# 2. List all employees from Seattle.
    def list_emp_from_Seattle(self):
        query = '''
            SELECT FirstName, LastName
            FROM Employees WHERE City='Seattle';
        '''
        for emp in self.cursor.execute(query):
            print('{} |---| {}'.format(emp['FirstName'], emp['LastName']))

# 3. List all employees from London.!!!!!!!
    def list_emp_from_London(self):
        query = '''
            SELECT FirstName, LastName
            FROM Employees WHERE City='London';
        '''
        for emp in self.cursor.execute(query):
            print('{} |---| {}'.format(emp['FirstName'], emp['LastName']))

# 4. List all employees that work in the Sales department.
    def list_emp_in_sales_dep(self):
        query = """
            Select * FROM employees where Title LIKE '%Sales%';
        """
        for emp in self.cursor.execute(query):
            print('{} |---| {} |---| {}'.format(
                emp['FirstName'], emp['LastName'], emp['Title']))

# 5. List all females employees that work in the Sales department.
    def list_all_female_from_sales(self):
        query = """
            Select * FROM employees
            WHERE Title LIKE '%Sales%'
            AND (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.');
        """
        for emp in self.cursor.execute(query):
            print('{} |---| {} |---| {} |---| {}'.format(
                emp['FirstName'], emp['LastName'], emp['Title'], emp['TitleOfCourtesy']))

# 6. List the 5 oldest employees.
    def list_5_oldest_emp(self):
        query = """
            SELECT * FROM employees
            ORDER BY BirthDate ASC LIMIT 5;
        """
        for emp in self.cursor.execute(query):
            print('{} |---| {} |---| {}'.format(
                emp['FirstName'], emp['LastName'], emp['BirthDate']))

# 7. List the first 5 hires of the company.
    def list_first_5_hires_in_comp(self):
        query = """
            SELECT * FROM employees
            ORDER BY HireDate ASC LIMIT 5;
        """
        for emp in self.cursor.execute(query):
            print('{} |---| {} |---| {}'.format(
                emp['FirstName'], emp['LastName'], emp['HireDate']))

# 8. List the employee who reports to no one (the boss)
    def list_emp_reports_to_noone(self):
        '''
            check for empty cell with null !!!
        '''
        query = """
            SELECT * FROM employees WHERE
            ReportsTo IS null;
        """
        for emp in self.cursor.execute(query):
            print('{} |---| {} |---| {}'.format(
                emp['FirstName'], emp['LastName'], emp['ReportsTo']))

# 9. List all employes by their first and last name, and the first and last name of the employees that they report to.
    def all_emp_and_who_they_report(self):
        '''
            LEFT JOIN ---> return all rows from the table when we get data
        '''
        query = """
            SELECT e1.FirstName, e1.LastName as name,
            SELECT e2.FirstName, e2.LastName as manager_name,
            FROM employees AS e1
            JOIN employees AS e2;
            ON e1.ReportsTo = e2.EmployeeID
        """

# 10. Count all female employees.
    def count_all_female_emp(self):
        query = """
             Select COUNT(EmployeeID) FROM employees AS emp_count
             WHERE (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.');
        """
        for i in self.cursor.execute(query):
            print(i['COUNT(*)'])

# 11. Count all male employees.
    def count_all_male_emp(self):
        query = """
            Select COUNT(EmployeeID) FROM employees AS emp_count
            WHERE (TitleOfCourtesy = 'Mr.' OR TitleOfCourtesy = 'Dr.');
        """
        for i in self.cursor.execute(query):
                    print(i['COUNT(*)'])

# 12. Count how many employees are there from the different cities. For example, there are 4 employees from London.
    def count_emp_from_diff_cities(self):
        query1 = """
            SELECT DISTINCT City
            FROM employees;
        """
        query2 = """
            SELECT ShipCity, COUNT(OrderID) AS order_count
            FROM Orders
            GROUP BY ShipCity
            ORDER BY  order_count DESC;
        """
        query3 = """
            SELECT City, COUNT(City)
            FROM employees
            GROUP BY City;
        """

# 13. List all OrderIDs and the employees (by first and last name) that have created them.
    def list_all_orderIDs_and_emp_who_create_it(self):
        query = """
            SELECT OrderID, FirstName, LastName
            FROM Orders JOIN Employees
            WHERE Orders.EmployeeID = Employees.EmployeeID;
        """
        for emp in self.cursor.execute(query):
            print('{} |---| {} |---| {}'.format(
                emp['OrderID'], emp['FirstName'], emp['LastName']))

# 14. List all OrderIDs and the shipper name that the order is going to be shipped via.
    def list_all_orderIDs_and_the_shipper(self):
        query = """
            Select OrderID, CompanyName FROM orders
            JOIN shippers ON orders.ShipVia = shippers.ShipperID;
        """
        for emp in self.cursor.execute(query):
            print('{} |---| {}'.format(
                emp['OrderID'], emp['CompanyName']))

# 15. List all contries and the total number of orders that are going to be shipped there.
    def list_all_packages_shiped_to_countries(self):
        pass

# 16. Find the employee that has served the most orders.
    def emp_with_most_orders(self):
        pass

# 17. Find the customer that has placed the most orders.
    def customer_with_most_orders(self):
        pass

# 18. List all orders, with the employee serving them and the customer, that has placed them.
    def all_orders_linked_emp_and_customer(self):
        query = """
            SELECT OrderID, CustomerID, FirstName, LastName FROM Orders JOIN Employees
        """
        for emp in self.cursor.execute(query):
            print('OrderId: {} |---|CustomerID: {} |---| Employee: {} {}'.format(
                emp['OrderID'], emp['CustomerID'], emp['FirstName'], emp['LastName']))

# 19. List for which customer, which shipper is going to deliver the order.
    def list_shipper_for_each_customer(self):
        pass

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
# q.count_all_male_emp()
# q.list_all_orderIDs_and_emp_who_create_it()
# q.list_all_orderIDs_and_the_shipper()
# q.all_orders_linked_emp_and_customer()
