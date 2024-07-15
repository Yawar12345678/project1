def greet(name):
    print ("Hello" + name)
def create_greeting (name):
    return "Hi" + name
def create_simple_greeting (name):
    return "Hi kuty"
def main():
    name = "Yawar"
    greet (name)
    greeting = create_greeting(name)
    print(greeting)
    simplegreeting = create_simple_greeting(name)
    print (simplegreeting)
main()