import pandas as pd

Inventary = {}
Record = {}
userData = {"2022a1r118@mietjammu.in": "dhruv@hp18", "2022a1r116@mietjammu.in": "smarth@23"}

class Book:
    def __init__(self):
        self.book_id = 0
        self.title = ""
        self.total_qty = 0 
        self.available_qty = 0

    def Add_book(self):
        try:
            self.book_id = int(input("Enter the book id : "))
            self.title = input("Enter the Book name: ")
            self.total_qty = int(input("Enter the the Qty: "))
            self.available_qty = int(input("Enter the available qty: "))
            Inventary[self.book_id] = [self.title, self.total_qty, self.available_qty]
            print("Book added successfully!\n")
        except:
            print("Invalid Input")
       
    def remove_book(self):
        try:
            self.book_id = int(input("Enter the book id you want to remove: "))
            if self.book_id in Inventary:
                Inventary.pop(self.book_id)
                print(f"Book with id {self.book_id} is Removed.")
            else:
                print("Book not found")
        except:
            print("Invalid Input")
        
    def update_book(self):
        try:
            self.book_id = int(input("Enter the book id you want to update: "))
            if self.book_id in Inventary:
                print("Enter a negative number if you want to decrease the qty")
                qty_update = int(input("Enter the quantity you want to add: "))
                Inventary[self.book_id][1] += qty_update
                Inventary[self.book_id][2] += qty_update
                print("Qty Updated")
            else:
                print("Book not found!")
        except:
            print("Invalid Input")
       
    def print_book(self):
        if Inventary:
            df = pd.DataFrame.from_dict(Inventary, orient='index', columns=['Title', 'Total Qty', 'Available Qty'])
            print(df.to_string(index=False))
        else:
            print("No stock available.")

class Record:
    def __init__(self):
        self.Name = ""
        self.Rollno = 0
        self.book_id = 0
        self.Book_name = ""
        self.status = ""
        self.condition = ""

    def Rent_book(self):
        try:
            self.Name = input("Enter your name: ")
            self.Rollno = input("Enter your Roll.no: ")
            self.book_id = int(input("Enter the book id you want to rent: "))
            if self.book_id in Inventary and Inventary[self.book_id][2] > 0:
                self.Book_name = Inventary[self.book_id][0]
                self.status = "Rent"
                self.condition = "Good"
                Record[self.Rollno] = [self.Name, self.book_id, self.Book_name, self.status, self.condition]
                Inventary[self.book_id][2] -= 1
                print("Book rented successfully!")
            else:
                print("Item not available or invalid Book ID.")
        except:
            print("Book not Rented successfully!")

    def Return_book(self):
        try:
            self.Rollno = int(input("Enter your Roll no : "))
            self.condition = input("Enter the returned condition (Good/Damaged): ")

            if self.Rollno in Record:
                if self.condition == 'Good':
                    Record[self.Rollno][3] = "Returned"
                    print("Student Name: ", Record[self.Rollno][0])
                    print("Student Rollno: ", self.Rollno)
                    print("Book Id: ", Record[self.Rollno][1])
                    print("Book Name: ", Record[self.Rollno][2])
                    print("Status: ", Record[self.Rollno][3])
                    Record[self.Rollno][4] = self.condition
                    Inventary[Record[self.Rollno][1]][2] += 1
                else:
                    print("Book condition is not good, so you have to pay a fine")
            else:
                print("Record not found for the given Roll.no.")
        except:
            print("Invalid Input")

    def print_Record(self):
        if Record:
            df = pd.DataFrame.from_dict(Record, orient='index', columns=["StudentName", "Book id", "BookName", "STATUS", "CONDITION"])
            print(df.to_string(index=True))
        else:
            print("No records available.")

def Management_system():
    temp = Book()
    while True:
        print("--------------MENU---------------")
        print("1. Add book ")
        print("2. Remove book ")
        print("3. Update book ")
        print("4. Print Inventory ")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            temp.Add_book()
        elif choice == 2:
            temp.remove_book()
        elif choice == 3:
            temp.update_book()
        elif choice == 4:
            temp.print_book()
        elif choice == 5:
            break
        else:
            print("Invalid Input!")

def main():
    temp = Book() 
    rec = Record()
    while True:
        print("--------------Welcome to Library Inventory Management System---------------")
        print("1. Management system ")
        print("2. Rent Book ")
        print("3. Return Book ")
        print("4. Print Record ")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Management_system()
        elif choice == 2:
            rec.Rent_book()
        elif choice == 3:
            rec.Return_book()
        elif choice == 4:
            rec.print_Record()
        elif choice == 5:
            break
        else:
            print("Invalid Input!")

def UserVerification():
    while(True):
        try:
            userId = input("Enter your id: ")
            userPassword = input("Enter password: ")
            if userId in userData and userData[userId] == userPassword:
                print("Login Successfully")
                main()
            else:
                print("Incorrect password or ID!")
        except:
            print(f"{userId} not found")
        
    

if __name__ == "__main__":
    UserVerification()
