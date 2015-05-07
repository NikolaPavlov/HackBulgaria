from company_maker import CompanyMaker


class ConsoleOutputHandler:

    def __init__(self):
        self.cm = CompanyMaker()

    def create_initial_database(self):
        self.cm.add_employee('Ivan Ivanov', 5000, 10000, 'Software Developer')
        self.cm.add_employee('Rado Rado', 500, 0, 'Technical support intern')
        self.cm.add_employee('Ivo Ivo', 10000, 100000, 'CEO')
        self.cm.add_employee('Petar Petrov', 3000, 1000, 'Marketing manager')
        self.cm.add_employee('Maria Georgieva', 8000, 10000, 'COO')

    def list_employees(self):
        all_employees = self.cm.list_employees()
        for employee in all_employees:
            print('{} - {}'.format(employee['name'], employee['position']))

    def monthly_spendings(self):
        print(self.cm.monthly_spendings())

    def yearly_spendings(self):
        print(self.cm.yearly_spendings())

    def add_employee(self):
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        self.cm.add_employee(name, monthly_salary, yearly_bonus, position)

    def delete_employee(self):
        id_for_deletion = input('id for deletion>')
        self.cm.delete_employee(id_for_deletion)

    def update_employee(self):
        emp_id = input('id>')
        emp_name = input('name>')
        emp_monthly_salary = input('monthly_salary>')
        emp_yearly_bonus = input('yearly_bonus>')
        emp_position = input('position>')
        self.cm.update_employee(emp_id,
            emp_name,
            emp_monthly_salary,
            emp_yearly_bonus,
            emp_position)




# coh = ConsoleOutputHandler()
# # coh.create_initial_database()
# coh.list_employees()
# coh.monthly_spendings()
# coh.yearly_spendings()
# coh.delete_employee()

