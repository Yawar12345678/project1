import numpy as np
def main():
    num = np.arange(12)
    print(num)
    num *= 3
    print(num)
    print(num + 4)
    print(num / 4)
    print(num ** 5)
    print(np.sin(num))
    print(np.max(num))
    print(np.mean(num))
    print(np.std(num))
if __name__ == "__main__":
    main()