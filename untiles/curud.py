def read_friends(users: list)->None:
    print("informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')

def add_user(lista: list) -> None:
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_postów = int(input("Podaj liczbe postów użytkownika: "))
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postów, }
    lista.append(new_user)

def search_user(users: list):
    imie = input("Podaj imie: ")
    for user in users:
        if user["name"] == imie:
            print(user)

def remove_user (users: list):
    imie = input("Podaj imie: ")
    for user in users:
        if user["name"] == imie:
            users.remove(user)

def update_user (users: list):
    imie = input("Wprowadż imie użytkowinika, którego dane chcesz zmienić: ")
    for user in users:
        if user["name"] == imie:
            user ["name"] = input("Podaj nowe imię: ")
            user ["surname"] = input("Podaj nowe nazwisko: ")
            user ["posts"] = int(input("Podaj liczbę postów: "))

