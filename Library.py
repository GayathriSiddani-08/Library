from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity
        self.borrowed_by = {}  # Dictionary to track borrowers and due dates

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Genre: {self.genre}, Quantity: {self.quantity})"

    def borrow_book(self, borrower_id, due_date):
        if self.quantity > 0:
            self.borrowed_by[borrower_id] = due_date
            self.quantity -= 1
            print(f"Book borrowed: {self.title}, due on {due_date}")
        else:
            print(f"No copies of {self.title} available for borrowing.")

    def return_book(self, borrower_id):
        if borrower_id in self.borrowed_by:
            self.quantity += 1
            del self.borrowed_by[borrower_id]
            print(f"Book returned: {self.title}")
        else:
            print(f"This book was not borrowed by borrower ID {borrower_id}")

class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id

    def __str__(self):
        return f"{self.name} (ID: {self.membership_id}, Contact: {self.contact_details})"

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def update_book(self, isbn, title=None, author=None, genre=None, quantity=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if genre:
                    book.genre = genre
                if quantity is not None:
                    book.quantity = quantity
                print(f"Updated book: {book}")
                return
        print(f"Book with ISBN {isbn} not found.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed book: {book}")
                return
        print(f"Book with ISBN {isbn} not found.")

    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower
        print(f"Added borrower: {borrower}")

    def update_borrower(self, membership_id, name=None, contact_details=None):
        if membership_id in self.borrowers:
            borrower = self.borrowers[membership_id]
            if name:
                borrower.name = name
            if contact_details:
                borrower.contact_details = contact_details
            print(f"Updated borrower: {borrower}")
        else:
            print(f"Borrower with membership ID {membership_id} not found.")

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            removed_borrower = self.borrowers.pop(membership_id)
            print(f"Removed borrower: {removed_borrower}")
        else:
            print(f"Borrower with membership ID {membership_id} not found.")
            
    def borrow_book(self, isbn, membership_id, days_to_borrow=14):
        if membership_id not in self.borrowers:
            print(f"Borrower with membership ID {membership_id} not found.")
            return
        for book in self.books:
            if book.isbn == isbn:
                due_date = datetime.now() + timedelta(days=days_to_borrow)
                book.borrow_book(membership_id, due_date)
                return
        print(f"Book with ISBN {isbn} not found.")
    
    def return_book(self, isbn, membership_id):
        for book in self.books:
            if book.isbn == isbn:
                book.return_book(membership_id)
                return
        print(f"Book with ISBN {isbn} not found.")

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append(book)
        return results

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)

    def display_borrowers(self):
        if not self.borrowers:
            print("No borrowers in the library.")
        for borrower in self.borrowers.values():
            print(borrower)

# Example Usage
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890", "Fiction", 5)
    book2 = Book("1984", "George Orwell", "1234567891", "Dystopian", 3)

    library.add_book(book1)
    library.add_book(book2)

    # Add borrowers
    borrower1 = Borrower("Alice Johnson", "alice@example.com", "B001")
    borrower2 = Borrower("Bob Smith", "bob@example.com", "B002")

    library.add_borrower(borrower1)
    library.add_borrower(borrower2)

    # Display books and borrowers
    library.display_books()
    library.display_borrowers()

    # Borrow a book
    library.borrow_book("1234567890", "B001", 7)
    library.borrow_book("1234567890", "B002", 14)

    # Return a book
    library.return_book("1234567890", "B001")

    # Update a book
    library.update_book("1234567891", quantity=5)

    # Update a borrower
    library.update_borrower("B002", contact_details="bob.smith@example.com")

    # Search for books
    search_results = library.search_books(author="George Orwell")
    for book in search_results:
        print(f"Search result: {book}")

    # Remove a book
    library.remove_book("1234567891")

    # Remove a borrower
    library.remove_borrower("B001")

    # Display books and borrowers again
    library.display_books()
    library.display_borrowers()