def main():
    animals = ['Bear', 'Cat', 'Lion', 'Fox']
    def order (item):
        return len(item)
    animals1 = sorted(animals, reverse=True, key=lambda item: len (item))

    print(animals1)
    animals.sort(reverse=True, key=lambda item: len(item))
    print(animals)
if __name__ == "__main__":
    main()