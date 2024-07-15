def main():
    animals = ["dog", "horse", "donkey"]
    animals.insert(1,  "snail")

    print(animals)

    more_animals = ["cat", "goat", ]
    animals.extend (more_animals)
    print(animals)
main()