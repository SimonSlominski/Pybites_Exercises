
def add_room():
    name = input("\nWhat name would you like to give the room?")
    name = scrub(name)
    with access_db() as cursor:
        cursor.execute("CREATE TABLE '" + name.lower() + "' """"
        Item TEXT, Value REAL)
        """)
        print(f"\nA room with name {name} has been added to the db.")

def scrub(table_name):
    # remove special characters. Keep only letters and digits
    return ''.join(char for char in table_name if char.isalnum())
