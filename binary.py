def printb(value):
    print(f"{ 255 & value : 08b}")
def main():
    pass
if __name__ == "__main__":
    num1 = 0b00001000
    printb(num1)
    printb(num1 >> 1)
    printb(num1 >> 3)
    num1 >>= 2
    printb(num1)
    print(10 >> 1)
    num1 = 0b01001000 
    printb(num1)
    print(10 << 3)

    


    main()