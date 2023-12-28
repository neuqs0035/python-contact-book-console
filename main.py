print("\n\t\tWelcome\tContact Book") # title

def addcontact(name : str,number : str,contact_type : str): # function to add contacts to contacts.csv
   
    file = open("contacts.csv","r") # creating file object to read existing contact details

    all_contacts_data = file.readlines() # read all contacts details 

    file.close() # close file object to release memory

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
     
    # if number and names are not already exists then after for loop add new contact
    file = open("contacts.csv","a") # create a file object to append data to file contacts.csv
   
    new_contact_detail = name + "," + number + "," + contact_type + "\n" # create a complete string for csv file 

    file.write(new_contact_detail) # append data to file
    
    file.close() # close the file object to release momory

    print("\nContact Details Added Successfully") # after successfully adding new contact details to file displays message
    return # return to called

def remove_contact(name_or_number : str): # function to remove contact based on either number or name

    file = open("contacts.csv","+r") # file object to read and write on contacts.csv

    existing_contact_details = file.readlines() # store all rows in the form of list , readed from file using above file object
    file.close()
    if(len(existing_contact_details) == 0): # if the list is empty , meaning file is empty
        print("\nContact Not Found , You Can Add New Contact Using Option 1") # display message that contact not found
        return # return to where function is called
    
    else: # if list is not empty , meaning file is not empty

        modified_contact_details = [] # new list to store the contact details where the matched contact is removed

        is_contact_match_found = False

        for contact in existing_contact_details: # iterate through each contact to find the match give in arguement of function to remove it
            contact_detail_list = contact.split(",") # split the csv data into list , to access individual column

            if name_or_number == contact_detail_list[0]: # if the name matched from file 

                is_contact_match_found = True # set this boolean variable to true if the number matched from file data

                print("\nContact Found , Name : " + contact_detail_list[0] + "  Number : " + contact_detail_list[1]) # display founded contact to user
                confirm = input("Do You Wanna Delete This Contact Then Enter 'yes' OR Enter Any Other Value : ") # ask user if he/she wanna delete this contact or not

                if(confirm.lower() == "yes"): # if user inputs yes , means he/she wanna delete this contact
                    continue # skips the next codes for this iteration , to avoid the current contact details to append on modified list
                else: # if user inputs other than yes , means he/she dont wanna delete this contact 
                    print("\nContact Remove Operation Cancled") # just displays message that remove operation canceled
                
            elif name_or_number == contact_detail_list[1]: # if the number matched from file data

                is_contact_match_found = True # set this boolean variable to true if the number matched from file data
                
                print("\nContact Found , Name : " + contact_detail_list[0] + "  Number : " + contact_detail_list[1]) # display founded contact to user
                confirm = input("Do You Wanna Delete This Contact Then Enter 'yes' OR Enter Any Other Value : ") # ask user if he/she wanna delete this contact or not

                if(confirm.lower() == "yes"):  # if user inputs yes , means he/she wanna delete this contact
                    continue # skips the next codes for this iteration , to avoid the current contact details to append on modified list

                else: # if user inputs other than yes , means he/she dont wanna delete this contact 
                    print("\nContact Remove Operation Cancled") # just displays message that remove operation canceled

            modified_contact_details.append(contact) # append the current contact details , every iteration
        
        file = open("contacts.csv","w") # create a file object with write mode
    
        file.writelines(modified_contact_details) # write all modified contact ( removed the request contact if found ) to contacts.csv
        file.close() # close the file object to release memory

        if(is_contact_match_found): # check if contact found or not
            print("\nContact Removed Successfully") # display message if contact found , and removed successfully
        else:
            print("\nContact Not Found , You Can Add New Contact Using Option 1") # display message that contact not found

# main code starts

while True: # starting of main menu

    print("\nMain Menu\n") # main menu title

    print("1 ) Add Contacts") # option for add contact
    print("2 ) Remove Contacts") # option for removing contact
    print("3 ) Search Contacts") # option for searching contact
    print("0 ) Quit") # option to quit app / program

    input_choice = int(input("\n_ : "))

    if( input_choice == 1): # if input choice from user is 1 ( to add contact )

        print("\nADD CONTACT") # title for add contact

        new_contact_name = input("\nEnter Name Of Contact : ") # input the name for new contact
        new_contact_number = input("Enter Number ( With Country Code) eg . +91xxx : ") # input the number for new contact

        while True: # loop till the user enter correct input for add contact as favourite or not 

            is_add_to_fav = input("Wanna Add This Contact As Favourite Or Not ? ( Y / n ) : ") # input from user if he/she want to add this contact to favourites or not

            contact_type = "" # empty string variable to store contact type either favourite or normal

            if is_add_to_fav.lower() == "y": # if user enter y , means yes he/she wants to add this contact as favourites
                contact_type = "favourite" # set the variable value to favourite
                break # break the loop 

            elif is_add_to_fav.lower() == "n": # if user enter n , means no he/she dont want to add this contact as favourite
                contact_type = "normal" # as user enters no than the contact type value set to 'normal'
                break # break the loop

            else: # if user enters other than y or n 
                print("Please Enter Either 'y' or 'n'") # displays message for user to warn him for enter the valid input

        addcontact(new_contact_name,new_contact_number,"normal") # calls the function which adds the new contact to file

    elif input_choice == 2: # if input choice from user is 1 ( to remove contact )

        number_or_name = input("\nEnter Either Number Of Contact Or Name : ")

        remove_contact(number_or_name) # function called to remove contact 

    elif input_choice == 3: 

        number_or_name = input_choice("\nEnter Either Number Or Name Of Contact You Want To Search : ")

        search_contact(number_or_name) # function called to search contact

    elif input_choice == 0: # if input choice from user is 0 ( to exit program )

        print("\nProgram Exited -\n") # display message
        break # break from main while loop to exit main menu
