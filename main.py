print("\n\t\tWelcome\tContact Book") # title

def addcontact(name : str,number : int): # function to add contacts to contacts.csv
    
    pass




# main code starts

while True: # starting of main menu

    print("Main Menu\n") # main menu title

    print("1 ) Add Contacts") # option for add contact
    print("0 ) Quit") # option to quit app / program

    input_choice = int(input("_ : "))

    if( input_choice == 1): # if input choice from user is 1 ( to add contact )

        print("\nADD CONTACT") # title for add contact

        new_contact_name = input("\nEnter Name Of Contact : ") # input the name for new contact
        new_contact_number = input("Enter Number ( With Country Code) eg . +91xxxxxxxxxx : ") # input the number for new contact

        addcontact(new_contact_name,new_contact_number)







    
