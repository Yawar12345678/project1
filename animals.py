def main():
    animals = ("cat","dog","snake")
    number_of_animals =len(animals)
    print(number_of_animals)
    print(animals[0])
    print(animals[1])
    print(animals[2])
    for animal in animals:
        print(animal)
    for i in range(0, len(animals)):
        print(animals[i])
main()