from models.data_sources import users
from untiles.curud import read_friends




if __name__ == '__main__':
    while True:
        print("Welcome to the menu choose an option: ")
        print("1. Read a list of friends ")
        print("0. Exit ")
        menu_option = input("Choose an option:")
        if menu_option == "0":
            break
        if menu_option = "1":
            read_friends(users)
