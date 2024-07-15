import itertools as it
def main():
    items = it.product(range(-1, 2), range(-1, 2))

    for x,  y in items:
        print(x, y)
if __name__ == "__main__":
    main()
