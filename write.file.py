def main():
    with open("tempt.txt", 'w') as file:
        file.write("Hello\n")
        file.write("to\n")
    with open("tempt.txt", 'a') as file:
        file.write("you\n")
    print("finished")
if __name__ == "__mian__":
    main()