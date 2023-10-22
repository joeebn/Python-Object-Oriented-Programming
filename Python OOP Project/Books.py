#This import allows for random IDs to be created for the ID of the books, as per the requirements
import uuid


#The first class here  is the books class that contains the variables set out in the requirements.
#The books class is where the details of the books will be saved. 
class Books():
    ID = ''
    title = ''
    author = ''
    year = ''
    publisher = ''
    number_of_copies = ''
    publication_date = ''


    #The constructor is here do make objects of the class. The values are passed in as parameters and the
    #values are set to the corresponding class variable.
    def __init__(self, ID, title, author, year, publisher, copies_available, publication_date):
        self.ID = ID
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.numer_of_copies = copies_available
        self.publication_date = publication_date


    #The setters are and allow for the program to set the values of objects on the class for entry and modification.
    #The values are passed in as parameters and allow for that varaible within the object to be set
    def set_title(self, title):
        self.title = title

    def set_author(self,author):
        self.author = author

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_number_of_copies(self, copies_available):
        self.number_of_copies = copies_available

    def set_publication(self, publication):
        self.publication_date = publication


    #Here are the getters for the class. These allow for the variables to be returned.
    def get_ID(self):
        return self.ID

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_number_of_copies(self):
        return self.number_of_copies

    def get_publication(self):
        return self.publication_date


          
#This is the second class that is instantiated from the books class
#This class is where the list of all books availible will be stored.
#The objects that are created are then stored in a list called booklist.
#This then allows for the list to be read and modified in various ways depending
#on the users' requirements.
#When object of this class are created, so is a list for the values to be stored in. 
class BookList(Books):
    booklist= []#Here is the list to store the values of the books. 

    #The constructor to create the objects also contains the empty list ready for values to be added.
    def __init__(self):
        booklist = []


    #This method adds the boks to the list using the .append() function, with the book itself passed
    #in as a parameter.
    #The try and except error checking is in place to catch any unforseen errors. 
    def add_books(self, book):
        try:
            self.booklist.append(book)
        except:
            print("Not Able to Add Book")


    #This method searches through the books to find a particular title and return the values.
    #The user passes in the title of the book, and the author and year are returned.
    #This method utilises a flagging system to see if the book is found.
    #If the book is found then found becomes true, otherwise the user is told that no
    #book exists. The methid also loops through all entries to find the book and
    #compares the parameter with the value stored.
    #The try and except method is in place to catch any errors. 
    def search_books(self,title):
        try:
            found = False
            for book in self.booklist:
               if book.get_title() == title:
                   print ("Book Found")
                   print (book.title)
                   print (book.author)
                   print (book.year)
                   found = True

            if found == False:
                print("No Book Found")
        except:
            print("Unable to find book")
           

    #This is the remove book method.
    #This, very similar to the previous method loops through and uses a flagging system in the same way
    #However, upon finiding the right entry in this method, the books is then delete from the list using the
    #.remove() feature.
    #The try and except validation is in place to catch any errors. 
    def remove_book(self, title):
        try:
            found = False
            for book in self.booklist:
                if book.get_title() == title:
                    self.booklist.remove(book)
                    print ("Book removed")
                    found = True
                
            if found == False:
                print("No Book Found")
        except:
            print("Unable to remove book")
                
    
          
    #Here is the number of books method. This method counts the number of books in the list.
    #The initial value of the books is set to 0 and incremented as the number of books is looped through
    #After the loop, the final number of books is returned to the user.
    #The try and except method is here to catch any errors, allowing the program to continue without crashing.
    def num_of_books(self):
        try:
            num_of_books = 0
            for i in self.booklist:
                num_of_books += 1

            return num_of_books
        except:
            print("Unable to count the books")


#Here is some hard coded entries for testing purposes.
book1 = Books(uuid.uuid1(), "The Hobbit", "JRR Tolkien", 1954, "Allen and Unwin", 100, "01/01/1954")
book2 = Books(uuid.uuid1(), "Brave New World", "Aldous Huxley", 1931, "	Chatto & Windus", 20, "02/02/1932")
book3 = Books(uuid.uuid1(), "1984", "George Orwell", 1949, "Secker & Warburg", 10, "01/01/1949")



#Here, the objects of the books created above are added to the booklist (bl1) object, which is used throughout the running of the program
bl1=BookList()
bl1.add_books(book1)
bl1.add_books(book2)
bl1.add_books(book3)



