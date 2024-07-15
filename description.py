def add_description(**description):
    for prop in description:
        print (prop, ":", description[prop])
        print()
def main():
    add_description(height= 180, age = 25, eyes = "brown")
    add_description(age = 45, race = "white", eyes = "blue")
main()


