# ----------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #5-1 Library Management System
#  * #11 Chia-Hui Amy Lin
# ----------------------------------------------------------------------------

#1 Class - Base for the object
class Person(object):
    ''' Basic info of a Person with unassigned status '''
    # Constructor
    def __init__(self, firstName, lastName, ID):
        self.firstName = firstName
        self.lastName = lastName
        self.ID = ID
        self.status = "None"

    #def outputInfo(self):
        #print(self.firstName, self.lastName, self.ID, self.status)

# --------------------------------------------------------------------------------------------------------
#2 Class - Specifically for Student, Inherit from Person
class Student(Person):
    ''' Student info '''
    num_checkout = 0

    # Constructor
    def __init__(self, firstName, lastName, ID):
        Person.__init__(self, firstName, lastName, ID)
        super().status = "Student"  # Super call status in Person to override the status
        Student.num_checkout += 1

    #def output(self):
        #print(self.firstName, self.lastName, self.ID, self.status, self.num_checkout)

# --------------------------------------------------------------------------------------------------------
#3 Class - Specifically for Member, Inherit from Person
class Member(Person):
    '''Member info'''
    num_checkout = 0  # Private Member to keep track of the check out total

    # Constructor
    def __init__(self, firstName, lastName, ID):
        Person.__init__(self, firstName, lastName, ID)
        super().status = "Member"  # Super call status in Person to override the status
        Member.num_checkout += 1


# --------------------------------------------------------------------------------------------------------
#4 Class - For Book Info
class Book(object):
    ''' A book details '''
    total_num_books = 0  # Private Member to keep track of the check out total

    # Constructor
    def __init__(self, ISBN, title, author, year, total_num_books):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.year = year
        self.total_num_books = total_num_books


# --------------------------------------------------------------------------------------------------------
#5 Class - Multiple inheritence for managing the library system
class Librarian(Person, Book):
    ''' A Staff to manage the Library system '''
    # A basic libraryInfo to keep the records of current check-out info
    libraryInfo = [{"Name": "Amy Lin", "ID": 11, "Status": "student", "Book Holding": [{"ISBN": 22454 , "title": "Grit", "author": "Duckworth, Angela", "year": 2015}], "Total Checkout": 1}]

    # Total number of records in the system
    totalNum = len(libraryInfo)

    # Constructor
    def __init__(self, firstName, lastName, ID, status, ISBN, title, author, year, totalNum):
        Person.__init__(self, firstName, lastName, ID)
        Book.__init__(self, ISBN, title, author, year, totalNum)
        self.status = status
        self.totalNum = totalNum

    # Function for check-in books
    def returnBook(self, returnID, returnISBN):
        ''' Return a book '''
        for idx in range(len(self.libraryInfo)):
            for secondidx in range(len(self.libraryInfo[idx]["Book Holding"])):
                if returnID == self.libraryInfo[idx]["ID"] and returnISBN == self.libraryInfo[idx]["Book Holding"][secondidx]["ISBN"]:
                    self.libraryInfo[idx]["Total Checkout"] -= 1
                    if len(self.libraryInfo[idx]["Book Holding"]) > 1:
                        self.libraryInfo[idx]["Book Holding"].pop(secondidx)
                    else:
                        self.libraryInfo.pop(idx)
                else:
                    print("No Match Found!")


    # Function for check-out books
    def checkOutBook(self, checkoutID, checkoutISBN):
        ''' Return a book '''
        for idx in range(len(self.libraryInfo)):
            for secondidx in range(len(self.libraryInfo[idx]["Book Holding"])):
                if checkoutID == self.libraryInfo[idx]["ID"] and checkoutISBN == self.libraryInfo[idx]["Book Holding"][secondidx]["ISBN"]:
                    self.libraryInfo[idx]["Total Checkout"] += 1
                    if len(self.libraryInfo[idx]["Book Holding"]) > 1:
                        self.libraryInfo[idx]["Book Holding"].append(secondidx)
                    else:
                        self.libraryInfo.append({"ID":checkoutID,"Book Holding": [{"ISBN": checkoutISBN}]})
                else:
                    print("No Match Found!")

# --------------------------------------------------------------------------------------------------------

'''
Library =
[
    {
        "Name" : Amy Lin,
        "ID" : 11,
        "Status" : student,
        "Book Holding" : [ { ISBN: , title: , author: , year:  } ],
        "Total Checkout" : 1
    }
]
'''


