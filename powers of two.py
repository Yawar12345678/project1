def powers_of_twos(n):
    powers = 1
    for _ in range (0, 4):
        powers *= 2
        yield powers
def main():
    for x in powers_of_twos(8):
        print(x)
if __name__ == "__main__":
    main()