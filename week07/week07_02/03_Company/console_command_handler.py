from console_output_handler import ConsoleOutputHandler


def main():
    coh = ConsoleOutputHandler()
    coh.create_initial_database()

    current_command = ''
    while current_command != 'exit':
        current_command = input('command>')
        if current_command == 'list':
            coh.list_employees()
        elif current_command == 'monthly_spendings':
            coh.monthly_spendings()
        elif current_command == 'yearly_spendings':
            coh.yearly_spendings()
        elif current_command == 'add':
            coh.add_employee()
        elif current_command == 'delete_employee':
            coh.delete_employee()
        elif current_command == 'update_employee':
            coh.update_employee()

if __name__ == '__main__':
    main()
