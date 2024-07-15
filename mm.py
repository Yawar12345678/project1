def main():
    numbers1 = {1, 2, 3, 4, 5, 6}
    numbers2 = {9, 8, 7, 6,}

    print(numbers1.union(numbers2))
    print(numbers1.intersection(numbers2))
    print("Difference")
    print(numbers2.difference(numbers1))
    print(numbers1.difference(numbers1))
main()