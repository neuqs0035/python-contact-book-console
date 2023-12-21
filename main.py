print("\n\t\tWelcome\tContact Book") # title

def addcontact(name : str,number : int): # function to add contacts to contacts.csv
    
    file = open("contacts.csv","r") # creating file object to read existing contact details

    all_contacts_data = file.readlines() # read all contacts details 

    for i in all_contacts_data: # iterate through each contact ( each person contact )
        contact_detail = i.split(",") # split the name and contact number and other details to list to access individual

        if contact_detail[0] == name: # check if the name is already exists or not
            print("\nName Already Exists , Choose Different Name") # message 
            print("\nExisting Contact Details :-") 
            print("Name : " + contact_detail[0] + "    Number : " + contact_detail[1]) # printing the contact details of the same name matched
            return # return , function call ended ( no further execution of function )
        
        
        elif contact_detail[1] == number: # check if the number is already exists or not

            print("\nNumber Already Exists , Check The Number And Try Again")
            print("Name : " + contact_detail[0] + "    Number : " + contact_detail[1]) # printing the contact details of the same number matched
            return # return , function call ended ( no further execution of function )
        
        else:
            pass

# main code starts

while True: # starting of main menu

    print("\nMain Menu\n") # main menu title

    print("1 ) Add Contacts") # option for add contact
    print("0 ) Quit") # option to quit app / program

    input_choice = int(input("_ : "))

    if( input_choice == 1): # if input choice from user is 1 ( to add contact )

        print("\nADD CONTACT") # title for add contact

        new_contact_name = input("\nEnter Name Of Contact : ") # input the name for new contact
        new_contact_number = input("Enter Number ( With Country Code) eg . +91xxxxxxxxxx : ") # input the number for new contact

        addcontact(new_contact_name,new_contact_number)
