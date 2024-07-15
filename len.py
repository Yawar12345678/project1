def main():
    fruits = ("apple", "mango", "peach")
    print(fruits)
    number_of_fruits = len(fruits)

    print(number_of_fruits)

    print(fruits[0])
    print(fruits[1])
    
    for fruit in fruits:
        print(fruit)

    for i in range(0, len(fruits)):
        print(fruits[i])

main()