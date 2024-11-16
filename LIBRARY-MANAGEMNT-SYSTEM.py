import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = {"Python Programming": 3, "Data Science Handbook": 2, "AI Basics": 4}
        self.borrowed_books = {}

    def add_book(self, book_name, count):
        if book_name in self.books:
            self.books[book_name] += count
        else:
            self.books[book_name] = count

    def borrow_book(self, book_name, user):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            self.borrowed_books.setdefault(user, []).append(book_name)
            return True
        return False

    def return_book(self, book_name, user):
        if user in self.borrowed_books and book_name in self.borrowed_books[user]:
            self.borrowed_books[user].remove(book_name)
            self.books[book_name] += 1
            return True
        return False

library = Library()

def display_books():
    books = "\n".join([f"{book}: {count}" for book, count in library.books.items()])
    messagebox.showinfo("Available Books", books)

def add_book():
    book_name = book_name_var.get()
    count = count_var.get()
    if book_name and count.isdigit():
        library.add_book(book_name, int(count))
        messagebox.showinfo("Success", f"Added {count} copies of '{book_name}'.")
    else:
        messagebox.showerror("Error", "Invalid input.")

def borrow_book():
    book_name = book_name_var.get()
    user = user_var.get()
    if book_name and user:
        if library.borrow_book(book_name, user):
            messagebox.showinfo("Success", f"'{book_name}' borrowed by {user}.")
        else:
            messagebox.showerror("Error", f"'{book_name}' is unavailable.")
    else:
        messagebox.showerror("Error", "Please provide valid inputs.")

def return_book():
    book_name = book_name_var.get()
    user = user_var.get()
    if book_name and user:
        if library.return_book(book_name, user):
            messagebox.showinfo("Success", f"'{book_name}' returned by {user}.")
        else:
            messagebox.showerror("Error", f"'{book_name}' was not borrowed by {user}.")
    else:
        messagebox.showerror("Error", "Please provide valid inputs.")

# Tkinter GUI
root = tk.Tk()
root.title("Library Management System")

book_name_var = tk.StringVar()
user_var = tk.StringVar()
count_var = tk.StringVar()

tk.Label(root, text="Book Name:").pack()
tk.Entry(root, textvariable=book_name_var).pack()

tk.Label(root, text="User Name:").pack()
tk.Entry(root, textvariable=user_var).pack()

tk.Label(root, text="Count (for Adding Books):").pack()
tk.Entry(root, textvariable=count_var).pack()

tk.Button(root, text="Display Books", command=display_books).pack()
tk.Button(root, text="Add Book", command=add_book).pack()
tk.Button(root, text="Borrow Book", command=borrow_book).pack()
tk.Button(root, text="Return Book", command=return_book).pack()

root.mainloop()
