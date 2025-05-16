import json
import os
from datetime import datetime

class LibraryManager:
    def __init__(self):
        self.library = []
        self.filename = "library_data.json"
        self.load_library()

    def load_library(self):
        """Load library data from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.library = json.load(file)
                print("\nLibrary loaded successfully!")
        except Exception as e:
            print(f"\nError loading library: {e}")
            self.library = []

    def save_library(self):
        """Save library data to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.library, file, indent=4)
            print("\nLibrary saved successfully!")
        except Exception as e:
            print(f"\nError saving library: {e}")

    def add_book(self):
        """Add a new book to the library"""
        print("\n=== Add New Book ===")
        
        # Get book details with validation
        book = {
            'title': input("Enter title: ").strip(),
            'author': input("Enter author: ").strip(),
            'year': self._get_valid_year(),
            'genre': input("Enter genre: ").strip(),
            'read': self._get_read_status(),
            'date_added': datetime.now().strftime("%Y-%m-%d")
        }
        
        self.library.append(book)
        self.save_library()
        print("\nBook added successfully!")

    def _get_valid_year(self):
        """Get and validate publication year"""
        while True:
            try:
                year = int(input("Enter publication year: "))
                current_year = datetime.now().year
                if 1000 <= year <= current_year:
                    return year
                print(f"Please enter a valid year between 1000 and {current_year}")
            except ValueError:
                print("Please enter a valid number")

    def _get_read_status(self):
        """Get and validate read status"""
        while True:
            status = input("Has the book been read? (y/n): ").lower()
            if status in ['y', 'n']:
                return status == 'y'
            print("Please enter 'y' or 'n'")

    def remove_book(self):
        """Remove a book from the library"""
        if not self.library:
            print("\nLibrary is empty!")
            return

        print("\n=== Remove Book ===")
        title = input("Enter the title of the book to remove: ").strip().lower()
        
        initial_count = len(self.library)
        self.library = [book for book in self.library if book['title'].lower() != title]
        
        if len(self.library) < initial_count:
            self.save_library()
            print("Book removed successfully!")
        else:
            print("Book not found!")

    def search_books(self):
        """Search for books by title or author"""
        if not self.library:
            print("\nLibrary is empty!")
            return

        while True:
            print("\n=== Search Books ===")
            print("1. Search by title")
            print("2. Search by author")
            
            choice = input("Enter your choice (1/2): ").strip()
            
            # Improved input validation
            if choice == '1' or choice == '2':
                break
            else:
                print("Invalid choice! Please enter 1 or 2.")
        
        search_term = input("Enter search term: ").lower().strip()
        found_books = []
        
        for book in self.library:
            if (choice == '1' and search_term in book['title'].lower()) or \
               (choice == '2' and search_term in book['author'].lower()):
                found_books.append(book)
        
        if found_books:
            print("\nFound Books:")
            self._display_books(found_books)
        else:
            print("No books found!")

    def display_all_books(self):
        """Display all books in the library"""
        if not self.library:
            print("\nLibrary is empty!")
            return

        print("\n=== All Books ===")
        self._display_books(self.library)

    def _display_books(self, books):
        """Helper method to display books"""
        for book in books:
            print("\n-------------------")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read: {'Yes' if book['read'] else 'No'}")
            print(f"Date Added: {book['date_added']}")

    def display_statistics(self):
        """Display library statistics"""
        if not self.library:
            print("\nLibrary is empty!")
            return

        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book['read'])
        read_percentage = (read_books / total_books) * 100

        print("\n=== Library Statistics ===")
        print(f"Total books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Percentage read: {read_percentage:.1f}%")

def main():
    library = LibraryManager()
    
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.remove_book()
        elif choice == '3':
            library.search_books()
        elif choice == '4':
            library.display_all_books()
        elif choice == '5':
            library.display_statistics()
        elif choice == '6':
            library.save_library()
            print("\nThank you for using Personal Library Manager!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main() 