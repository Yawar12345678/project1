def main():
    li = [chr(x) for x in range (65, 69)]
    print(li)
    for x in li:
        print(x)
    print(list((chr(x)for x in range (65, 69))))
if __name__ == "__main__":
    main()