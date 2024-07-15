def number_range():
    for i in range(0, 5):
        yield (i)
def main():
    for i in range(5):
        print(i)
if __name__ == "__main__":
    main()