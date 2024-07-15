import os 
def main():
    for (root, dirs, files) in os.walk('op.py
                                       '):
         for file in files:
              print(os.path.join(root, file))
if __name__ == "__main__":
     main()