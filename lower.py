def main():
    animals = ['Cat', 'dog', 'Bear']
    def lower(str):
        return str.lower()
    animals1 = map(lower, animals)
    print(list(animals1))
    animals = list(map(lower , animals))
    print(animals)
if __name__ == "__main__":
    main()