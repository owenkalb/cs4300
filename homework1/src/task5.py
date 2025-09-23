# Create a list of your favorite books, including book titles and authors. 
booklist = [
    ("Red Rising", "Pierce Brown"),
    ("Vicious", "V. E. Schwab"),
    ("Ender's Game", "Orson Scott Card"),
    ("The Way of Kings", "Brandon Sanderson"),
    ("The Terminal List", "Jack Carr")
]
# Create a dictionary that represents a basic student database, 
# including student names and their corresponding student IDs
studentlist = {
    "John": "101",
    "Joe": "102",
    "Jill": "103",
    "Jason": "104"
}

def first_three_books():
    return booklist[:3]

def get_student_info(name):
    return studentlist.get(name)
