def main():
    months = {
        "jan" : "january",
        "feb"  : "febuarary",
        "mar" : "march"
   }
    days = months.get("Jan")
    print(days)
    print(type(days))

    days = months.get("january", "jan")
    print(days)

    days = months.get("faburary", "feb")

    print(months)

    
main()