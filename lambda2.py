def main():
    try:
        file = open("lambda.py")
        lines = file.readlines()
        for line in lines:
             print(line)
    finally:
        file.close()
if __name__ == "__main__":
    main()