from getpass import getpass

import utils
from utils import print_menu, print_error, print_success
import service


def login():
    username = input("username: ")
    password = getpass("password: ")
    response = service.login_user(username, password)
    utils.print_response(response)

def register():
    pass


def logout():
    pass


def create_todo():
    pass


def update_todo():
    pass


def delete_todo():
    pass


def todo_list():
    pass


def block_user():
    pass


def unblock_user():
    pass


def block_admin():
    pass


def unblock_admin():
    pass

# divide menu according role
#login_menu()
#user_menu()
#admin_menu()
def menu():
    print_menu("=> login")
    print_menu("=> register")
    print_menu("=> logout")
    print_menu("=> create_todo")
    print_menu("=> update_todo")
    print_menu("=> delete_todo")
    print_menu("=> todo_list")
    print_menu("=> block_user")
    print_menu("=> unblock_user")
    print_menu("=> block_admin")
    print_menu("=> unblock_admin")
    print_menu("=> quit")
    choice = input("> ?: ")
    match choice:
        case "login":
            login()
        case "register":
            register()
        case "logout":
            logout()
        case "create_todo":
            create_todo()
        case "update_todo":
            update_todo()
        case "delete_todo":
            delete_todo()
        case "block_user":
            block_user()
        case "unblock_user":
            unblock_user()
        case "block_admin":
            block_admin()
        case "unblock_admin":
            unblock_admin()
        case "quit":
            exit(0)
        case _:
            print_error("Wrong choice")



if __name__ == '__main__':
    menu()