fruits = ["apple","bannana","peach"]
animals =["lion","cat","mouse"]

for i, item in enumerate(fruits):
    print(i, item)

print()

for fruit, animal in zip(fruits, animals):
    print(fruit,animal)