print("This program generates username from the file 'superheroes.txt'")
print()
print(f"{'Name':20} Username")
# open the file
with open("superheroes.txt") as heroes_file:
    # for each line in the file
    for hero in heroes_file:
        hero = hero.strip() # removing the newline character

        # split the name into first name and last name
        firstname, lastname = hero.split()

        # generate the username
        username = (firstname[0] + lastname).lower()

        print(f"{hero:20} {username}") # print the current line



