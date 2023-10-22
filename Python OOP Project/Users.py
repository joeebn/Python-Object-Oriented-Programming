#Code to create the class with the class variables set out in the requirements
class User():
    username = ''
    firstname = ''
    surname = ''
    house_num = ''
    street_name = ''
    postcode = ''
    email_add = ''
    dob = ''
    
    #The initialising constructor for the objects of this class. The class variables are set in this section.
    #The variables are passed into the function 
    def __init__(self, username, firstname, surname, house_num, street_name, postcode, email_add, dob):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_num = house_num
        self.street_name = street_name
        self.postcode = postcode
        self.email_add = email_add
        self.dob = dob

    #Here are the getters of this class that return the corresponding value.
    #Below are the getters for username, firstname, surname, house number, street name, postcode, email and DoB. 
    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_num(self):
        return self.house_num

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email_add(self):
        return self.email_add

    def get_dob(self):
        return self.dob

    
    #Here are the setters of the class. The setters allow for the variables to be set, or modified, when they are passed
    #into the method. Here are the setters for the firstname, surname, email address and DoB. 
    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_surname(self, surname):
        self.surname = surname

    def set_email_add(self, email_add):
        self.email_add = email_add

    def set_dob(self, dob):
        self.dob = dob


#The second class in this file is the UserList class. This is iherited from the User class.
#This class is in place to add users to the list callled userlist. This list is used to store the user in the library
#This class also allows for some of the requirements, such as removing users, counting amount of users and showing
#specific details.
class UserList(User):
    userlist = [] #This is the list created as the intances of this class are created. 

    #The constructor here creates the userlist for the data to be added, removed and read from as per the users requests.
    def __init__(self):
        userlist=[] 

    #This method adds the user to the list that was created earlier. The users themselves are created in the user class
    #and are then appended to the list from here.
    #Within here to validate the entry is a try and except method which will run the method as intented, however,
    #if an issue arrises, then the except methods will catch the error, allow the program not to crash. 
    def add_user(self, user):
        try:
            self.userlist.append(user)
        except:
            print("Unable to add user")


    
    #This method removes a user from the userslist. Using the .remove() function, the specific instance of the UserList
    #can be removed form the class. The method also includes a flag, the found variable, which is used to
    #see if a user is present in the list, otherwise no user will be found.
    #This class also counts the amount of users that match the criteria. As this method has the firstname of the
    #passed in as a parameter, there may be multiples within the list. If that is the case the program will tell the
    #user that there are more than one persons' with that name in the system.
    #This feature is acheived through setting the amount to 0 at the start of the loop and incrementing by 1 if multiples
    #are found. Like before, the try and except is used here to catch any unforseen errors.     
    def remove_user(self, firstname):
        try:
            amount = 0
            found = False
            for user in self.userlist:
                if user.get_firstname() == firstname:
                    amount += 1
                    self.userlist.remove(user)
                    print ("User removed")
                    found = True
            
                if amount >=2:
                    print("There are more than 1 users with that firstname")
            if found == False:
                print("No User with that name")
        except:
            print("No record found")


    #This method will count the number of users in the list. This list checks if the list is empty,
    #if it is then the method will return 0 as this is set at the begining of the method.
    #If values are present then the method will loop through the list and increment 1 to the user_count
    #for every pass in the loop. Then the program can return the exact number of users.
    #The try and expect error hadnling is in place to catch any unforseen errors. 
    def count_users(self):
        try:
            user_count = 0
            if self.userlist == []:
                return user_count
            else:
                for i in self.userlist:
                    user_count += 1

            return user_count
        except:
            print("Unable to count users")

            
    #This method will show the information for the user when the username is passed in.
    #The achieve this, a flag is in place through the found variable, which is set to false and will
    #change to true if the user if found. At the end of the loop if found is still false then no user has
    #been found and will return as such.
    #Within the loop, a comparision is made between the username passed into the method and the username stored
    #in the list. The try and except method is in place to catch any errors. 
    def show_details(self, username):
        try:
            found = False
            for user in self.userlist:
               if username == user.username:
                   print ("User Found")
                   print (user.username)
                   print (user.firstname)
                   print (user.surname)
                   found = True
            if found == False:
                print("No User Found")
        except:
            print("Unable to find user")


#Example instances of the User class added in for testing.            
user1 = User("JB123","Joe", "Brown", 3, "New Street", "AA1 1AA" , "jb@gmail.com", "01/01/2000")
user2 = User("JA123","Joe", "Jones", 5, "Old Street", "BB1 1BB" , "jj@gmail.com", "02/02/2000")

#Set up of the ul1 instance of the UserList class, which is used in the main system.            
ul1 = UserList()

#Here the two users are added using the add_user method
ul1.add_user(user1)
ul1.add_user(user2)





                
