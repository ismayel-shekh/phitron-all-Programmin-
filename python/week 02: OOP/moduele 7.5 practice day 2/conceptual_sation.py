class Book:
    def __init__(self,id,name,quantity) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity
class User:
    def __init__(self,id,name,passoword) -> None:
        self.id = id
        self.name = name
        self.passoword = passoword
        self.borrowedBook =[]
        self.returnedBook =[]
class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.users =[]
        self.books = []
    def addbook(self,id,name,quantity): # add new book
        for book in self.books:
            if book.id == id:
                print(f"\n\t ---> !! book id {book.id} already exists")
                return
        book = Book(id,name,quantity)
        self.books.append(book)
        print(f"\n\t ---> {book.name} X {quantity} added succesfuly !")
    def adduser(self,id,name,password): #add a new user
        for user in self.users:
            if user.id == id:
                #they give -> book.id   i wright --> user.id
                print(f"\n\t ---> !! user id {user.id} already exists")
                return
        user = User(id,name,password)
        self.users.append(user)
        return user
    def borroewBook(self,user,token):
        for book in self.books:
            if book.id == token:
                if book in user.borrowedBook:
                    print("\n\t ---> already borrowed !")
                    return
                elif book.quantity == 0:
                    print("\n\t ---> no copy available !")
                    return
                else:
                    user.borrowedbooks.append(book)
                    book.quantity -= 1
                    print(f"\n\t ---> borrowed {book.name} succesfully !")
                    return
                print("\n\t ---> not found any book with id : {token}")
    def returnBook(self,user,token):
        for book in self.books:
            if book.id == token:
                if book in user.borrowedbook:
                    book.quantity += 1
                    user.returnedBook.append(book)
                    user.borrowedBook.remove(book)
                    print(f"\n\t ---> returned {book.name}succesfully !")
                    return
                else:
                    print(f"\n\t ---> !!! you are not reading {book.name} now")
                    