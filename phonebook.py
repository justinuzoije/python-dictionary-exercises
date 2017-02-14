import pickle

phone_book = {}
userChoice = 0

def look_up_entry():
    targetName = raw_input("Name: ")
    if targetName in phone_book:
        print "Found entry for %s: %s" % (targetName, phone_book[targetName])
    else:
        print "Entry not found"

def set_entry():
    targetName = raw_input("Name: ")
    targetNumber = raw_input("Phone Number: ")
    phone_book[targetName] = targetNumber
    print "Entry stored for %s" % targetName

def delete_entry():
    targetName = raw_input("Name: ")
    del phone_book[targetName]
    print "Entry deleted"

def list_entry():
    for entry in phone_book:
        print "Found entry for %s: %s" % (entry, phone_book[entry])

def save_entry():
    #open the file in write mode (w)
    myfile = open('phonebook.pickle', 'w')
    #dump the contents of the phonebook_dict into myfile - the open file
    pickle.dump(phone_book, myfile)
    #close myfile
    myfile.close()
    print "Entries saved to phonebook.pickle"

def restore_entry():
    #The global statement lets the function know that it is talking about
    #the global phone_book, not a local variable version of it
    global phone_book
    #open the file in read mode (r)
    myfile = open('phonebook.pickle', 'r')
    #load the contents from teh file and store it in the phonebook_dict variable
    phone_book = pickle.load(myfile)
    print "Entries restored"

while userChoice != 7:
    userChoice = int(raw_input('''Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Save entries
    6. Restore saved entries
    7. Quit
    What do you want to do (1-7)?
    '''))

    #1 - Look up an entry
    if userChoice == 1:
        look_up_entry()

    #2 - Set an entry
    elif userChoice == 2:
        set_entry()

    #3 - Delete an entry
    elif userChoice == 3:
        delete_entry()

    #4 - List all entries
    elif userChoice == 4:
        list_entry()

    #5 - Save entries
    elif userChoice == 5:
        save_entry()

    #6 - Restore saved entries
    elif userChoice == 6:
        restore_entry()

    #7 - Quit
    elif userChoice == 7:
        print "Bye"
