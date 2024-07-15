

def main():
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    days[0:3]= []
    print(days)

    days.remove("saturday")
    print(days)

    item = days.pop(2)
    print(days)
    print(item)
    del days[1]

    print(days)
    return 

main()