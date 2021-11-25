known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

while True:
    print('Hi, my name is Travis')
    name = input('What is your name? ').strip().capitalize()
    if name in known_users:
        print(f'Hello, {name}')
        remove = input("Would you like to be removed from the system? (y/n) ".lower())
        if remove == "y":
            known_users.remove(name)

    else:
        print('Name not recognized')


