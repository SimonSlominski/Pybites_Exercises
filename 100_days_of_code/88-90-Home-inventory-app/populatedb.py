import sqlite3


def enter_details():
    while True:
        info = []
        room = input('Enter room name: ')
        inventory = input('Enter the item name: ')
        owner = input('Enter the owner: ')
        for i in (room, inventory, owner):
            info.append(i)

        with sqlite3.connect("addressbook.db") as connection:
            c = connection.cursor()
            c.execute("INSERT INTO Details VALUES(?, ?, ?)", info)
            print('Data inserted to database.\n')

        stop = input("Hit Q to to quit.\n")
        if stop.upper() == 'Q':
            break
        else:
            continue


if __name__ == "__main__":
    enter_details()
