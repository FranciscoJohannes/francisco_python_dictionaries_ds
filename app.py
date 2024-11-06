from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="Hello, World!")

# class for product dictionary
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# List of product dictionaries
products = [
    {"name": "Laptop", "price": 750},
    {"name": "Desk Chair", "price": 100},
    {"name": "Smartwatch", "price": 200},
    {"name": "Notebook", "price": 5},
    {"name": "Running Shoes", "price": 80}
]

# class for employee dictionary
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

# List of employee dictionaries
employees = [
    {"name": "John Doe","department": "Sales"},
    {"name": "Jane Smith","department": "Human Resources"},
    {"name": "Mark Johnson","department": "IT"},
    {"name": "Lisa Wong", "department": "Marketing"},
    {"name": "Paul McDonald","department": "Finance"}
]

# class for book dictionary
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# List of book dictionaries
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"title": " A Brief History of Time", "author": "Stephen Hawking"}
]

# class for university dictionary
class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location

# List of university dictionaries
universities = [
    {"name": "University of the Philippines", "location": "Quezon City"},
    {"name": "Ateneo de Manila University", "location": "Quezon City"},
    {"name": "De La Salle University", "location": "Manila"},
    {"name": "University of Santo Tomas", "location": "Manila"},
    {"name": "Polytechnic University of the Philippines", "location": "Manila"}
]

# class for restaurant dictionary
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

# List of restaurant dictionaries
restaurants = [
    {"name": "Vikings Luxury Buffet", "cuisine_type": "Buffet"},
    {"name": "Antonio's Restaurant", "cuisine_type": "Fine Dining"},
    {"name": "Mesa Filipino Moderne", "cuisine_type": "Filipino"},
    {"name": "Manam Comfort Filipino", "cuisine_type": "Filipino"},
    {"name": "Ramen Nagi", "cuisine_type": "Japanese"}
]

if __name__ == '__main__':
    app.run(debug=True)