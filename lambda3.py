def main():
    guesses = set("aeiou")
    word = "fatass"
    result = map(lambda x: ' _ 'if x not in guesses else x, word)
    print(list(result))



if __name__ == "__main__":
    main()