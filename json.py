from json import dump, load
def main():
    numbers = {1, 2, 4, 5, 6}
    text = "hello how are you"
    lookup = {
        "jan",
        "feb",
        "mar"
              }
    to_save = {
        "values": numbers,
        "greetings" : text,
        "months" : lookup
    }
    filename = "data.bin"
    with open(filename, 'wb') as file:
        dump(to_save, file)
        
    with open(filename, 'rb') as file:
        loaded = load(file)
    print(loaded)
if __name__ == "__main__":
    main()