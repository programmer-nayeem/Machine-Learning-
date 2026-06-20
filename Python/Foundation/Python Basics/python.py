"""
==============================================================
 THE COMPLETE BEGINNER'S PYTHON TUTORIAL
==============================================================
A progressive, runnable guide covering:
1. Variables
2. Conditions
3. Loops
4. Functions
5. Object-Oriented Programming (OOP)
6. File Handling
7. Modules
8. Exception Handling

Each section has explanations as comments, runnable example
code, and exercises (with sample solutions) at the end.
Run this file with:  python python_tutorial.py
==============================================================
"""

import math
import random
from datetime import datetime


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ==============================================================
# 1. VARIABLES
# ==============================================================
def variables_demo():
    section("1. VARIABLES")

    # Variables store data. Python figures out the type automatically.
    name = "Alice"        # string (str)
    age = 30               # integer (int)
    height = 5.6           # float
    is_student = False     # boolean (bool)

    print(name, type(name))
    print(age, type(age))
    print(height, type(height))
    print(is_student, type(is_student))

    # Type conversion
    age_str = "25"
    age_int = int(age_str)
    price = str(19.99)
    print("Converted age:", age_int, type(age_int))
    print("Converted price:", price, type(price))

    # Multiple assignment
    x, y, z = 1, 2, 3
    print("x, y, z =", x, y, z)

    # --- Exercise 1 ---
    # 1. Create variables for your name, age, and favorite hobby.
    # 2. Print a sentence combining all three using an f-string.
    # 3. Convert "100" into an integer and add 50 to it.
    my_name = "Sam"
    my_age = 22
    hobby = "chess"
    print(f"My name is {my_name}, I am {my_age} years old, and I enjoy {hobby}.")
    number = int("100") + 50
    print("100 converted and +50 =", number)


# ==============================================================
# 2. CONDITIONS
# ==============================================================
def conditions_demo():
    section("2. CONDITIONS")

    temperature = 28
    if temperature > 30:
        print("It's hot outside!")
    elif temperature > 20:
        print("It's a pleasant day.")
    else:
        print("It's cold outside!")

    # Logical operators
    age = 25
    has_id = True
    if age >= 18 and has_id:
        print("Entry allowed")
    if age < 18 or not has_id:
        print("Entry denied")

    # --- Exercise 2 ---
    def check_sign(n):
        if n > 0:
            return "positive"
        elif n < 0:
            return "negative"
        else:
            return "zero"

    print("Sign of -5:", check_sign(-5))

    def age_group(a):
        if a < 13:
            return "child"
        elif a < 20:
            return "teenager"
        else:
            return "adult"

    print("Age group for 15:", age_group(15))

    num = 30
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by both 3 and 5")


# ==============================================================
# 3. LOOPS
# ==============================================================
def loops_demo():
    section("3. LOOPS")

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
        print("range step:", i)

    count = 0
    while count < 5:
        print("while count:", count)
        count += 1

    # break and continue
    for number in range(10):
        if number == 5:
            break
        print("before break:", number)

    for number in range(10):
        if number % 2 == 0:
            continue
        print("odd number:", number)

    # --- Exercise 3 ---
    print("Even numbers 1-50:")
    for n in range(1, 51):
        if n % 2 == 0:
            print(n, end=" ")
    print()

    print("Multiplication table 1-5:")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i*j:3}", end=" ")
        print()


# ==============================================================
# 4. FUNCTIONS
# ==============================================================
def is_even(number):
    return number % 2 == 0


def calculate_area(length, width):
    return length * width


def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0


def describe_pet(name, animal_type="dog"):
    print(f"{name} is a {animal_type}.")


def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


def functions_demo():
    section("4. FUNCTIONS")

    def greet(name="friend"):
        print(f"Hello, {name}!")

    greet()
    greet("Maria")

    result = calculate_area(5, 3)
    print("Area:", result)

    describe_pet(name="Rex")
    describe_pet(name="Whiskers", animal_type="cat")

    print("Sum via *args:", sum([1, 2, 3, 4]))
    show_info(name="Alice", age=30)

    # --- Exercise 4 ---
    print("Is 7 even?", is_even(7))
    print("Average of 4,8,15,16,23,42:", average(4, 8, 15, 16, 23, 42))


# ==============================================================
# 5. OBJECT-ORIENTED PROGRAMMING (OOP)
# ==============================================================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Cat(Animal):
    def speak(self):  # overrides parent method
        print(f"{self.name} says Meow!")


class Bird(Animal):
    pass  # inherits speak() unchanged


class BankAccount:
    """Demonstrates encapsulation with a 'private' attribute."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # double underscore -> name-mangled / "private"

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade.")


def oop_demo():
    section("5. OBJECT-ORIENTED PROGRAMMING (OOP)")

    cat = Cat("Whiskers")
    bird = Bird("Tweety")
    cat.speak()
    bird.speak()

    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(30)
    print("Final balance:", account.get_balance())

    # --- Exercise 5 ---
    my_car = Car("Toyota", "Corolla", 2022)
    my_car.display_info()

    student = Student("Sam", 88)
    print("Student grade:", student.get_grade())
    student.set_grade(95)
    print("Updated grade:", student.get_grade())


# ==============================================================
# 6. FILE HANDLING
# ==============================================================
def file_handling_demo():
    section("6. FILE HANDLING")

    # Writing to a file
    with open("notes.txt", "w") as file:
        file.write("Hello, this is line one.\n")
        file.write("This is line two.\n")

    # Appending to a file
    with open("notes.txt", "a") as file:
        file.write("This line is added later.\n")

    # Reading line by line
    print("Contents of notes.txt:")
    with open("notes.txt", "r") as file:
        for line in file:
            print(line.strip())

    # --- Exercise 6 ---
    with open("diary.txt", "w") as file:
        file.write("Today I learned Python.\n")
        file.write("It was a productive day.\n")
        file.write("Tomorrow I'll practice more.\n")

    with open("diary.txt", "r") as file:
        lines = file.readlines()
        print(f"diary.txt has {len(lines)} lines.")

    with open("diary.txt", "a") as file:
        file.write(f"New entry added at {datetime.now()}.\n")


# ==============================================================
# 7. MODULES
# ==============================================================
def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(length, width):
    return length * width


def modules_demo():
    section("7. MODULES")

    print("Square root of 16:", math.sqrt(16))
    print("Value of pi:", math.pi)
    print("Random number 1-10:", random.randint(1, 10))
    print("Current datetime:", datetime.now())

    # --- Exercise 7 ---
    print("Circle area (r=3):", round(circle_area(3), 2))
    print("Rectangle area (4x5):", rectangle_area(4, 5))

    print("Rolling a die 10 times:")
    rolls = [random.randint(1, 6) for _ in range(10)]
    print(rolls)


# ==============================================================
# 8. EXCEPTION HANDLING
# ==============================================================
class InsufficientFundsError(Exception):
    """Custom exception for bank account withdrawals."""
    pass


class NegativeNumberError(Exception):
    """Custom exception for invalid square root input."""
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money in account.")
    return balance - amount


def safe_sqrt(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


def exception_handling_demo():
    section("8. EXCEPTION HANDLING")

    # Basic try/except/else/finally
    try:
        number = int("42")
    except ValueError:
        print("Conversion failed.")
    else:
        print(f"Conversion succeeded: {number}")
    finally:
        print("Finished the conversion attempt.")

    # Catching specific exceptions
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("You can't divide by zero.")

    # Raising and catching a custom exception
    try:
        withdraw(100, 150)
    except InsufficientFundsError as e:
        print(f"Transaction failed: {e}")

    # --- Exercise 8 ---
    try:
        print(safe_sqrt(25))
        print(safe_sqrt(-9))
    except NegativeNumberError as e:
        print(f"Error: {e}")

    try:
        with open("does_not_exist.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("Custom message: That file could not be found.")


# ==============================================================
# MINI PROJECT: CONTACT BOOK
# Combines variables, conditions, loops, functions, OOP,
# file handling, and exception handling all in one place.
# ==============================================================
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append(Contact(name, phone))

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, phone = line.strip().split(",")
                    self.add_contact(name, phone)
        except FileNotFoundError:
            print("No saved contacts found yet.")


def mini_project_demo():
    section("MINI PROJECT: CONTACT BOOK")

    book = ContactBook()
    book.add_contact("Alice", "123-456-7890")
    book.add_contact("Bob", "987-654-3210")
    book.save_to_file("contacts.txt")

    new_book = ContactBook()
    new_book.load_from_file("contacts.txt")
    for contact in new_book.contacts:
        print(contact)


# ==============================================================
# RUN ALL DEMOS
# ==============================================================
if __name__ == "__main__":
    variables_demo()
    conditions_demo()
    loops_demo()
    functions_demo()
    oop_demo()
    file_handling_demo()
    modules_demo()
    exception_handling_demo()
    mini_project_demo()

    print("\n" + "=" * 60)
    print("Tutorial complete! Explore each function above,")
    print("modify the code, and try the exercises on your own.")
    print("=" * 60)