import matplotlib.pyplot as plt
import numpy as np
def main():
    x = np.random.randn(10000)
    n, bins, patches = plt.hist(x, bins=20, edgecolor = 'white')
    print(n, bins, patches)
    plt.show()
if __name__ == "__main__":
    main()