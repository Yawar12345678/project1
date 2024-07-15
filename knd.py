def create_lookup(people, ages):
    lookup = dict()
    for i in range (0, len(people)):
        name = people[i]
        age = ages[i]
        lookup[name] = age
    return lookup
def user_loop (lookup):
    while True:
        user_input = input("Enter aa name , or 'quit' >")
        if user_input == "quit":
            break
        elif not user_input in lookup:
            print("unknown person.")
            continue
          
        age = lookup[user_input]
        print(user_input + "is" +str(age) +"years old")





def main():    
    people = ["yawar", "bakhtawar", "yahya"]
    age = [25, 21, 18]
    lookup = create_lookup(people, age)
    print(lookup)

main()