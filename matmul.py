import numpy as np
def main():
    num1 = np.array([5, 10, 3, 6]). reshape(2,2)
    num2 = np.array([25, 1, 3, 0.5]). reshape(2,2)
    print(num1)
    print(num2)
    num3 = np.matmul(num1, num2)
    print(num3)
if __name__ == "__main__":
    main()