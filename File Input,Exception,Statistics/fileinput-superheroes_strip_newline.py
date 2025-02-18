
print("This program displays the contents of the file 'superheroes.txt'")

# open the file
with open("superheroes.txt") as heroes_file:
    # for each line in the file
    for hero in heroes_file:
        hero = hero.strip()
        print(hero) # print the current line



