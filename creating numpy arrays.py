import numpy as np
def main():
    print(np.zeros(6, dtype=int))
    values = np.zeros([2, 3])
    print(values)
    print(values.ndim)
    print()
    print(np.zeros([2, 3]))
    print(np.arange(2, 7 ,0.5))
    print(np.linspace(2, 4, 6))
    print(np.random.rand(7))
if __name__ == "__main__":
    main()