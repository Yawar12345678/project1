def greetings():
    print ("Welcome, no unauthorized users! :")
PASSWORD = "KUTA"
def get_password ():
    password = input ("Enter your password:")
    if password == PASSWORD:
        print ("Acess Granted") 
    else:
        print ("Acesss Denied")
def main():
    greetings()
    get_password()
main()