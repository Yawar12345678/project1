from collections import defaultdict
people = defaultdict(int)
people.update({"bob":45, "yawar":25})
print(people)
print(people["bob"])
print(people["yawar"])