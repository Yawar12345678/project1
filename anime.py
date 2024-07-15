animals = ("dog","cat","mouse")
animals2 = ("lion", "bear", "girrafe")

fruits1 = ("apple", "pear")
fruit2 = ("cherry", "kiwi")

animals += animals2
print(id(animals))
print(animals)

fruits1 += fruit2

print (id(fruits1))


print (fruits1)