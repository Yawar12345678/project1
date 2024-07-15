def show_menu():
    options = ("kuty ka bacha", "alo ka paratha", "painchod")
    for i in range(0, len(options)):
        print(str(i) + ":" + options[i])
    
def show_database(db):

    for i in range(0, len(db)):
        print(str(i)+ ":" + db [i])
    
def add_item(db):
    item = input("enter the item:")
    db.append(item)
    
def change_item(db):
    item_number = input("enter the number of item to change:")
    item = input ("enter the item:")
    db [int(item_number)] = item
def delete_item(db):
    item_number = input ("enter the item to delete:")
    db.pop (int (item_number))
    pass




def main():
    db = ["apple", "orange", "guava"]
    show_database(db)
    show_menu()
    add_item(db)
    show_database(db)
    delete_item(db)

main()