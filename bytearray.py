def main():
    data = bytearray([12, 34, 56, 255])
    print(list(data))
    data = bytearray("hello bro", 'utf8')
    print(list(data))
if __name__ == "__main__":
    main()
