#The imports from the other files to allow acces to the classes.
from Users import User, UserList
from Books import Books, BookList


#The class here is instantiated from the UserList class.
#This is because the data in the loans needs access to the
#userlist to assign users with the books.
#As objects of the class are created, the loanlist list is
#created. This will then allow the various other methods
#within this class to perform all the operations listed in the requirements.
class Loans(UserList):
    loanlist = []

    #This constructor creates a list when the object is setup. 
    def __init__(self):
        loanlist=[]
        
    #Here is the method to borrow a book. The values of the user and book are passed in
    #Similar to other methods, a flag to see if both the book and user is found is used here
    #The method will loop through the books and compare the title of the book with the one
    #passed into the function. If the book is found the the same applies to the user using
    #nested loops. If both are found then the book is added to the list.
    #The try and except technique is used here to validate the method.
    def borrow_book(self, firstname, surname, title):
        try:
            user_found = False
            book_found = False
            for i in BookList.booklist:
                if title == i.title:
                    book_found = True
                    for x in UserList.userlist:
                        if firstname == x.firstname and surname == x.surname:
                            record = [x.firstname, x.surname,title, "\n"]
                            self.loanlist.append(record)
                            user_found=True
                            print("Borrow Added")
                     
            if user_found == False:
                print("Not able to add to list")
            elif book_found == False:
                print("Not able to add to list")
        except:
            print("Unable to process book borrow")



    #Here is the method to return a book from the list.
    #As a user may have many books on loan, the method
    #needs the users details and the book title.
    #Same as before, a flag to see if the record has been found is used.
    #within the for loop, the method compares the names to each value(i)
    #in the list. If found the book is removed using the .remove() function.
    #Otherwise there is nothing to remove.
    #The try and except technique is used to catch ay errors.
    def return_book(self, firstname, surname, book):
        try:
            found = False
            for i in self.loanlist:
                if i[0] == firstname and i[1]==surname and i[2]==book:
                    self.loanlist.remove(i)
                    found = True
                    print("Book Returned")
            if found == False:
                print("No Record Found")
        except:
            print("Unable to return book")
            


    #Here is the count_borrows method.
    #The method will count the number of books on loan by a particular person.
    #The firstname and surname are needed to be passed into the method to ensure
    #the correct user is added.
    #The value of amount is set to 0 at the start of the method. This will then
    #be incremented as more borrows are found.
    #The loop will run through the loanlist list and will compare the parameters
    #with their counterparts in the list.
    #If found the found varaible becomes true and the final value of
    #amount is returned to the user.
    #If nothing is found then and message of such will appear to the user.
    #The try and except methods are in place to catch any errors. 
    def count_borrows(self, firstname, surname):
        try:
            amount = 0
            found = False
            for i in self.loanlist:
                if i[0] == firstname and i[1] == surname:
                    amount +=1
                    found = True
                    print(amount)

            if found == False:
                print("No Books on Loan")
        except:
            print("Unable to count the books")
       

    #The final method of the class is the overdue books method.
    #This method finds all the overdue books.
    #As per the requirements the users' username, firstname and surname
    #are returned for each loan.
    #The loop in this method loops through the loanlist and then the userlist,
    #hence why the loans class is instantiated from the userlist class,
    #this creating a nested loop
    #As the loop runs, the values of the two lists are compared to find the values required.
    def overdue_books(self):
        try:
            for i in self.loanlist:
                for x in self.userlist:
                    if x.firstname == i[0] and x.surname == i[1]:
                        print ("User",x.username, "(",x.firstname, x.surname,")","has the book", i[2])
        except:
            print("Unable to find books")
                        
              

#The object l1 is created for the program and is used throughout the program. 
l1 = Loans()




