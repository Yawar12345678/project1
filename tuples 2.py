def main():
    animals = ("goat", "cat", "bear")
    (a1, a2, a3) = animals
    print(a1)
    print(a2)
    print(a3)
    fruits = ("apple", "orange", "pear", "guava")
    (f1, f2, *morefruits) = fruits
    print(f1)
    print(f2)
    print(*morefruits)
    print(type(morefruits))

main()