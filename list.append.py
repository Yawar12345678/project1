
def main():
    print(list((x,y) for x in range (0, 4) for y in range (0, 4)))

    li = list()
    for x in range(0, 4):
        if x == 1:
            continue
    for y in range(0, 4):
        if y == 1:
            continue
    li.append((x,y))

    print(li)
if __name__ == "__main__":
    main()