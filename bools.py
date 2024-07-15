import numpy as np
def main():
    values1 = np.array([1, 2, 3, 4])
    bools = np.array([True, False, True, False])
    print(values1[bools])
if __name__ == "__main__":
    main()