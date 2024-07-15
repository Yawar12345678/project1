import matplotlib.pyplot as plt 
import numpy as np
def main():
    print(plt.style.available)
    plt.style.use('classic')
    x = np.linspace(0, 30, 100)
    y = x**2
    plt.figure(figsize=(16,9))
    plt.grid(True)
    plt.title("y=x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, y)
    plt.show()
if __name__ == "__main__":
    main()
