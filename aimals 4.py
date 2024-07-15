animals = ["dog", "cat", "mouse"]
"""
animals1 = animals

del animals1[1]

print(animals)
print(animals1)
"""
"""
animals3 = animals.copy()
del animals3 [1]
print (animals3)
print (animals)
"""
animals4 = [animal.upper() for animal in animals]
print(animals4)

length = [len(text) for text in animals]
print (length)

numbers1 = [2, 4, 6, 7, 11]
numbers2 = [x*x for x in numbers1 ]
print (numbers2)