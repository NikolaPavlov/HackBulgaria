import sql_manager
import getpass
from settings import *


def main_menu():
    sql_manager.create_clients_table()
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass('Enter your password:')
            email = input("Enter your email:")
            print(sql_manager.register(username, password, email))

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass('Enter your password:')

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'reset-password':
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            sql_manager.send_reset_email(username, email)

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("reset-password - for reset the pass via email")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass('Enter your password:')
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("reset-password - for sending new pass via email")

        elif command == 'exit':
            break


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
