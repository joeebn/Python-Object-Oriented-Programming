#The imports for the system. This allows this file to access other parts of the system and other
#imports such as datetime and the UUID for creating ID's
import uuid
from datetime import datetime
from Books import Books, BookList, bl1
from Users import User, UserList, ul1
from Loans import Loans, l1

#Welcome message when the application starts.
#This displays a welcome message and then runs to the main menu
def welcome():
    print("------------Welcome to the Library----------")
    main_menu()


#The main menue function allows to user to select a section of the system. The options can be seen below
#The system will taje to user to the correct section depending on their option.
#If the user selects an invalid option, the fucntion will recall itself, making it recursive.
def main_menu():
    print("Please Select an Option 1-4 \n")
    option = input("1:User section | 2:Books Section | 3:Loans | 4:Close the Program\n")

    if option == "1":
        user()
    elif option == "2":
        books()
    elif option == "3":
        loans()
    elif option =="4":
        quit()
    else:
        print("Please Select a Valid Option")
        main_menu()


#In the user seciton, again the user has a choice between the various sections of the library
def user():
    print("Please Select an Option 1-5")

    option = input("""
1:Add User|  2:Remove User|3:Count Number of Users|
4:Check User Details| 5:Main Menu \n
""")

    #The while loop is used to rerun the code if an invalid option is made
    #The loop is broken if a valid option is selected by changing the state of i
    i = 1
    while 1==1:
        
        if option == "1":
            add_user()
            i=2
        elif option == "2":
            remove_user()
            i=2
        elif option == "3":
            count_users()
            i=2
        elif option == "4":
            check_user_details()
            i=2
        elif option == "5":
            main_menu()
            i=2
        else:
            print("Please Select a Valid Option")
            user()

#This function is in place to add a user to the list of user.
#This is done by using the method from the user code.
def add_user():
    print("Please Enter User Details")
    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        username = input("Username (between 3 and 10 characters): ")
        if username == "" or username==" " or len(username)<3 or len(username)>=10: #Presence check and range check in place on the username
            print("Please Enter a valid username")
        else:
            i=2
            
    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        firstname = input("Firstname: ")
        if firstname.strip().isdigit(): #This checks that no numbers are inputted for the firstname
            print ("Please enter a valid firstname")
        elif firstname == "" or firstname ==" ": #A presence check is in place on the fristname variable
            print ("Please enter a valid firstname")
        else:
            i=2


    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        surname = input("Surname: ")
        if surname.strip().isdigit():#This checks that no numbers are inputted in this section
            print ("Please enter a valid surname")
        elif surname == "" or surname ==" ":#A presence check is in place on this variable
            print ("Please enter a valid surname")
        else:
            i=2
            
    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        try: #The try method will run the code indended, however is the user does not enter a number than
            #a value error occurs, therefore this is to stop that from happening
            house_number = int(input("House Number: "))
            
            if house_number == "" or house_number ==" ": #Presence check on the house number
                print("Please enter a value")
            else:
                i=2
        except ValueError:
            print("Please enter a numerical value")

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        street_name = input("Street Name: ")
        if street_name == "" or street_name ==" ":#Presence check on the street name
            print ("Please enter a valid Street Name")
        else:
            i=2
   
    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        postcode = input("Postcode: ")
        if len(postcode)<6 or len(postcode)>8 or postcode == "" or postcode ==" ":#A range check and presence check on the postcode
            #Postcodes should be between 6 and 8 characters.
            print ("Please enter a valid postcode")
        else:
            i=2


    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        email_add = input("Email: ")
        if len(email_add)<4 or len(email_add)>30 or email_add == "" or email_add ==" ":#Another range check on the email variable
                                                                                        #Also, a prsence check
            print ("Please enter a valid Email Address")
        else:
            i=2
        

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        try: #This is used because the date must be entered in the correct way, failing to do soe will run an error.
            #The except code will catch these errors. 
            dob_entry = str(input("Date of Birth (DD/MM/YYYY): ")) #User must enter in the correct format DD/MM/YYYY
            dob = datetime.strptime(dob_entry,"%d/%m/%Y")#This uses the datetiime feature to ensure the format is DD/MM/YYYY
            i=2
        except:
            print("Please Enter date in the correct format")
            
        
        
    #This creates an instance in the user details just entered by creating an instance on the User class
    add = User(username, firstname, surname, house_number, street_name, postcode, email_add, dob)
    #The add_user method from the class is then used to add the user to the list.
    ul1.add_user(add)

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #This section of code asks if the user wants to add another user, go back to user menu, or the main menu
    #Depending on their answer, the user will be taken to the correct place.
    i =1
    while i==1:
    
        print("Would you like to add another user? Y or N")
        option = input()
        if option.lower()=="y":#The .lower() takes the users input and converts to lowercase
            add_user()
            i=2
        elif option.lower()=='n':
            x=1
            while x==1:
                decision = input("Do you want another service for the user? Y or N \n")
                if decision.lower() == "y":
                    user()
                    x=2
                    i=2
                elif decision.lower() == "n":
                    main_menu()
                    x=2
                    i=2
                else:
                    print ("Please enter a valid option")
        else:
            print("Please select a valid option")
            

#The function to remove a user. The user is asked to enter the name of the user
#The method from the user class is then called.
def remove_user():
    name = input("Please enter the Firstname of the user to remove")
    ul1.remove_user(name)

  #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
  #This section of code asks if the user wants to remove another user, go back to user menu, or the main menu
  #Depending on their answer, the user will be taken to the correct place
    i=1
    while i==1:
    
        print("Would you like to remove another user? Y or N")
        option = input()
        if option.lower()=="y":
            remove_user()
            i=2
        elif option.lower()=='n':
            x=1
            while x==1:
                decision = input("Do you want another service for the user? Y or N \n")
                if decision.lower() == "y":
                    user()
                    x=2
                    i=2
                elif decision.lower() == "n":
                    main_menu()
                    x=2
                    i=2
                else:
                    print ("Please enter a valid option")
        else:
            print("Please select a valid option")


#Here is the method to count the number of users.
#If the user selects this section the the count_users method from the class
#will run. 
def count_users():

    amount_of_users = (ul1.count_users())
    print("There are currently", amount_of_users, " users in the library")

     #This section of code asks if the user wants to go back to user menu, or the main menu
    #Depending on their answer, the user will be taken to the correct place
    i=1
    while i==1:
    
        print("Would you like to return to the user menu? Y or N")
        option = input()
        if option.lower()=="y":
            user()
            i=2
        elif option.lower()=='n':
            i=2
            main_menu()
            
        else:
            print("Please select a valid option") 


#This is the check user details function.
#The user enters the username of the user they wish to find.
#The show details method from the User class will then run. 
def check_user_details():
    print("Please enter a username")
    username = input()
    ul1.show_details(username)


  #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
  #This section of code asks if the user wants to find another users' details, go back to user menu, or the main menu
  #Depending on their answer, the user will be taken to the correct place
    i=1
    while i==1:
    
        print("Would you like to find another user? Y or N")
        option = input()
        if option.lower()=="y":
            check_user_details()
            i=2
        elif option.lower()=='n':
            x=1
            while x==1:
                decision = input("Do you want another service for the user? Y or N \n")
                if decision.lower() == "y":
                    user()
                    x=2
                    i=2
                elif decision.lower() == "n":
                    main_menu()
                    x=2
                    i=2
                else:
                    print ("Please enter a valid option")



#This is the books main menu. It will utilise the Books and BookList classes.
#Users are intially given a menu to chose where to navigate to. 
def books():
    print("Please Select an Option 1-5")

    option = input("""
1:Add Book|  2:Remove Book|3:Find a Book|
4:Amount of Books| 5:Main Menu \n
""")

  #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
  #This section of code asks if the user what part of the books system they wish to travel to. 
    i=1
    while i==1:
        
        if option == "1":
            add_book()
            i=2
        elif option == "2":
            remove_book()
            i=2
        elif option == "3":
            find_book()
            i=2
        elif option == "4":
            amount_of_books()
            i=2
        elif option == "5":
            main_menu()
            i=2
        else:
            print("Please Select a Valid Option")
            books()
    
#The add books function is used to gather details of a book to add to the library, very similar to the add user functino above.
def add_book():
    
    print("Please Enter Book Details")



    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i ==1:
        title = input("Please enter title")
        if title == "" or title==" ":#A presence check on the title of the book
            print("Please Enter a valid Title")
        else:
            i=2

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        author = input("Please enter an Author")
        if author == "" or author==" ":#Presence check on the author of the book
            print("Please Enter a valid Author")
        else:
            i=2

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        try:#Try and except methoid in place as non-entry of an interger will return a value error. 
            year = int(input("Please enter a year"))
            if year == "" or year==" ":#Presence check on the year variable
                print("Please enter a valid year")
            else:
                i=2
        except ValueError:
            print("Please Enter a year eg. 2022")



    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i ==1:
        publisher = input("Please enter a publisher")
        if publisher == "" or publisher==" ":#presence check on the publisher to ensure a valie is entered
            print("Please Enter a valid publisher")
        else:
            i=2

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        try:#Try and except methoid in place as non-entry of an interger will return a value error. 
            number_of_copies = int(input("Please enter number of copies"))
            if number_of_copies=="" or number_of_copies == " ":#Presence check to ensure data is entered.
                print("Please Enter a number")
            else:
                i=2
        except ValueError:
            print("Please Enter a valid number")

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    i=1
    while i==1:
        try:#This is used because the date must be entered in the correct way, failing to do soe will run an error.
            #The except code will catch these errors. 
            publisher_date_entry = str(input("Date of Publication (DD/MM/YYYY): "))#Asking the user to enter the date in a DD/MM/YYYY format
            publisher_date = datetime.strptime(publisher_date_entry,"%d/%m/%Y")#This validates the date to ensure it is in the correct format.
            i=2
        except:
            print("Please Enter date in the correct format")
  
    

    #This takes the values entered by the user and creates and instance of the Books class
    add = Books(uuid.uuid1(), title, author, year, publisher, number_of_copies, publisher_date)
    #This add the instance of the book class to the list of books using the add_books method
    bl1.add_books(add)


    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #This asks the user if they want to add another books, return to book menu, or the main menu
    #Depending on the users answer they will be navigate to the correct section.
    i =1
    while i==1:
    
        print("Would you like to add another book? Y or N")
        option = input()
        if option.lower()=="y":
            add_book()
            i=2
        elif option.lower()=='n':
            x=1
            while x==1:
                decision = input("Do you want another service for the books? Y or N \n")
                if decision.lower() == "y":
                    books()
                    x=2
                    i=2
                elif decision.lower() == "n":
                    main_menu()
                    x=2
                    i=2
                else:
                    print ("Please enter a valid option")
        else:
            print("Please select a valid option")


#Function to remove a book from the library
#The user is asked to enter the title of the book.
#The method remove_book will then be called from the BookList Class
def remove_book():
    title = input("Please enter a book to be removed")
    bl1.remove_book(title)

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #This asks the user if they want to add another books, return to book menu, or the main menu
    #Depending on the users answer they will be navigate to the correct section.
    i=1
    while i==1:
    
        print("Would you like to remove another book? Y or N")
        option = input()
        if option.lower()=="y":
            remove_book()
            i=2
        elif option.lower()=='n':
            x=1
            while x==1:
                decision = input("Do you want another service from the books? Y or N \n")
                if decision.lower() == "y":
                    books()
                    x=2
                    i=2
                elif decision.lower() == "n":
                    main_menu()
                    x=2
                    i=2
                else:
                    print ("Please enter a valid option")
        else:
            print("Please select a valid option")



#This function is used to find a book
#The user enters the title of the book
#The method is then called from the BookList class. 
def find_book():
    title = input("Please enter the title of the book")
    bl1.search_books(title)

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #This asks the user if they want to add another books, return to book menu, or the main menu
    #Depending on the users answer they will be navigate to the correct section.
    i=1
    while i==1:
    
        print("Would you like to find another book? Y or N")
        option = input()
        if option.lower()=="y":
            find_book()
            i=2
        elif option.lower()=='n':
            x=1
            while x==1:
                decision = input("Do you want another service from the books? Y or N \n")
                if decision.lower() == "y":
                    books()
                    x=2
                    i=2
                elif decision.lower() == "n":
                    main_menu()
                    x=2
                    i=2
                else:
                    print ("Please enter a valid option")


#This function will find the number of books in the list
#The method from the BookList class is then called.
#This returns the amount of books that are presence in the library
def amount_of_books():
    amount_of_books = bl1.num_of_books()
    print("There are currently", amount_of_books,"books in the library")

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #This asks the user if they want to eturn to book menu, or the main menu
    #Depending on the users answer they will be navigate to the correct section.
    i=1
    while i==1:
    
        print("Would you like to return to the books menu? Y or N")
        option = input()
        if option.lower()=="y":
            books()
            i=2
            
        elif option.lower()=='n':
            main_menu()
            i=2
                
        else:
            print("Please select a valid option") 



#The loans main menu here will call from the Loans Class
#First the user is given a menu to to perform various tasks. 
def loans():
    print("Please Select an Option 1-5")

    option = input("""
1:Borrow Book|  2:Return Book| 3:Number of Books a User is Borrowing|
4:Overdue Books| 5:Main Menu \n
""")

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #This section of code asks if the user what part of the books system they wish to travel to. 
    i = 1
    while 1==1:
        
        if option == "1":
            borrow_book()
            i=2
        elif option == "2":
            return_book()
            i=2
        elif option == "3":
            loan_books()
            i=2
        elif option == "4":
            overdue_books()
            i=2
        elif option == "5":
            main_menu()
            i=2
        else:
            print("Please Select a Valid Option")


#The borrow book function will ask the user to enter the firstname, surname and title of the book
#The borrow_book method will then be called and will add the borrow to the list
def borrow_book():
    print("Please enter the following details: firstname, surname and book title:")
    firstname = input("Firstname: ")
    surname = input("Surname: ")
    title = input("Title: ")

    #Here the method is called to add these values to the list
    l1.borrow_book(firstname, surname, title)

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #The options will then ask is the user wishes to add another borrow, return to the loans menu, or the main menu
    i=1
    while i==1:
        option = input("Please Select - 1: Borrow Another Book| 2: Return to Loans Menu| 3: Return to Main Menu")

        if option == "1":
            borrow_book()
        elif option == "2":
            loans()
        elif option == "3":
            main_menu()
        else:
            print("Please Select an Valid Option")
       
#This function takes the firstname, surname and title of the book to return the book.
def return_book():
    print("Please enter the following details: firstname, surname and book title:")
    firstname = input("Firstname: ")
    surname = input("Surname: ")
    title = input("Title: ")

    #This method is called to remove the data given from the list. 
    l1.return_book(firstname, surname, title)

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #The options will then ask is the user wishes to add another borrow, return to the loans menu, or the main menu
    i=1
    while i==1:
        option = input("Please Select - 1: Return Another Book| 2: Return to Loans Menu| 3: Return to Main Menu")

        if option == "1":
            return_book()
        elif option == "2":
            loans()
        elif option == "3":
            main_menu()
        else:
            print("Please Select an Valid Option")

#This function will count the number of books a person has on loan.
#The user enters the firstname and surname 
def loan_books():
    print("Please enter the following details: Firstname and Surname: ")
    firstname = input("Firstname: ")
    surname = input("Surname: ")

    #This method is called form the Loans Class. 
    l1.count_borrows(firstname, surname)


    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #The options will then ask is the user wishes to add another borrow, return to the loans menu, or the main menu
    i=1
    while i==1:
        option = input("Please Select - 1: Find another User| 2: Return to Loans Menu| 3: Return to Main Menu")

        if option == "1":
            loan_books()
        elif option == "2":
            loans()
        elif option == "3":
            main_menu()
        else:
            print("Please Select an Valid Option")


#This function check the amount of books overdue in the library
def overdue_books():
    #This method is called from the Loans class
    l1.overdue_books()

    #A while loop to loop if an invalid answer is made. If an input in valid, then the loop will break
    #The options will then ask is the user wishes to add another borrow, return to the loans menu, or the main menu
    i=1
    while i==1:
        option = input("Please Select - 1: Return to Loans Menu| 2: Return to Main Menu")

        if option == "1":
            loans()
        elif option == "2":
            main_menu()
        else:
            print("Please Select an Valid Option")

#This runs the first function as the program starts. 
welcome()
