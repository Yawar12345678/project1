def main():
    numbers1 = [x for x in range(10)]

    print(numbers1)

    numbers2 = [x for x in numbers1 if x > 4]
    print(numbers2)

    print (5 % 3 == 0)

    numbers3 = [x for x in numbers1 if x % 4 == 0 ]
    print(numbers3)

main()