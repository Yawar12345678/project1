class person():
    def __init__(self, name):
        self._name = name
        
        print(f"{name} created")
        print(id(self))
        pass
    def eat(self):
        print ("im eating")
    def talk(self):
        print("hello")
def main():
    person1 = person("zara") 
    person2 = person("zoe")
    print(person1._name)
    print(person2.__qualname__)

    person1.eat()
    person2.talk() 

    print(id(person1))
    print(id(person2))

    person1.age = 50
    person2.age = 40
main()