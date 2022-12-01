class Library:
    def __init__(self,bookList):
        self.books = bookList
    
    def displayBooks(self):
        print("Available books are:")
        for book in self.books:
            print(book)

    def lendBook(self,reqBook):
        if reqBook in self.books:
            self.reqBook = reqBook
            self.books.remove(self.reqBook)
        else:
            print("The requested book is not available")

    def addBook(self,retBook):
        self.books.append(self.retBook)

class Customer:
    def borrowBook(self):
        self.reqBook = input()
        return self.reqBook
    def returnBook(self):
        self.retBook = input()
        return self.retBook

lib = Library(['book1','book2','book3'])
cst = Customer()
while(True):
    print("Enter 1 for displaying book list")
    print("Enter 2 for borrowing a book")
    print("Enter 3 for returning a book")
    print("Enter 4 to quit the programme")

    number = int(input())

    if number==1:
        lib.displayBooks()
    elif number==2:
        reqBook = cst.borrowBook()
        lib.lendBook(reqBook)
    elif number==3:
        retBook = cst.returnBook()
        lib.addBook(retBook)
    elif number==4:
        quit()
