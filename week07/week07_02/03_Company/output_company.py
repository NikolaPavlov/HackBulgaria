import sqlite3
from company_maker import CompanyMaker

cm = CompanyMaker()
db = CompanyMaker.db()

def add_employee(db):
    db.add_employee('gogo', 100, 1111, 'drinker')
    db.add_employee('coco', 1010, 1111, 'drinker2')

# def list_employees(self.db_conn):
#     employees = CompanyMaker.list_employees()
#     for employee in employees:
#         print('{} - {}'.format(employee['name'], employee['position']))

# cm = CompanyMaker()
# cm.list_employees()
