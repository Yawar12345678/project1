def main():
    with open("lambda.py") as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end="")
if __name__ == "__main__":
    main()