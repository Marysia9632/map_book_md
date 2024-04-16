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