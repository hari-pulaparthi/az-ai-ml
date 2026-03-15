# Python OOP Program: Library Book Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f'You have borrowed "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'You have successfully returned "{self.title}".')
        else:
            print(f'"{self.title}" was not borrowed.')
    
    def display_info(self):
        status = "Avilable" if self.available else "Not Available"
        print(f'Title: {self.title}, Author: {self.author}, Status: {status}')

def display_books(library):
    print("\n Library Catalog:")
    for idx, book in enumerate(library):
        print(f'{idx + 1}. ', end="")
        book.display_info()

# Main Program 
if __name__ == "__main__":
    # Create a library with some books
    library = [
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("The Great Gatsby", "F. Scott Fitzgerald")
    ]

    while True:
        print("\nLibrary Menu:")         
        print("1. View Books")         
        print("2. Borrow Book")         
        print("3. Return Book")         
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_books(library)

        elif choice == '2':
            display_books(library)
            try:
                book_number = int(input("Enter the number of the book to borrow: "))
                if 1 <= book_number <= len(library):
                    library[book_number - 1].borrow_book()
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Please enter a valid number.") 

        elif choice == '3':
            display_books(library)
            try:
                book_number = int(input("Enter the number of the book to return: "))
                if 1 <= book_number <= len(library):
                    library[book_number - 1].return_book()
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':             
            print("Exiting Library System. Goodbye!")             
            break         
        
        else:             
            print("Invalid choice. Please try again.") 