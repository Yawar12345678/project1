def main():
    animals = ("dog", "cat", "fox", "tiger")
    number_animals = len(animals)
    print(number_animals)
    for animal in animals:
        print(animal)
    for i in range (0, len(animals)):
        print(animals[i])
main()