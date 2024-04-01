# 1. The Calculator App
# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

def addition(x,y):
    return x+ y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y != 0:
        return x/y 
    else:
        return "Error: Division by zero."

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
opertation=input("Enter the operation (+, -, *. /): ")

if opertation == "+":
    result = addition(x,y)
elif opertation == "-":
    resul= subtraction(x,y)
elif opertation =="*":
    result= multiplication  (x,y)
elif opertation== "/":
    result = division(x,y)
else:
    print("Invalid operation")

print("Result", result)



# 2. The Shopping List Maker
# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

def add_item(shopping_list):
    while True:
        items = input("What item would you like to add to the list? (type 'quit' to stop): ")
        if items.lower()== 'done':
            break
        shopping_list.append(items)
    return shopping_list

def remove_item(shopping_list):
    item_to_remove = input("What item would you like to remove from list?: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
    else:
        print("Item not found in the list.")

def print_list(shopping_list):
    if not shopping_list:
        print("Your list is currently empty. ")
    else:
        print("Shopping list:")
        for item in shopping_list:
            print("- ", item)





# 3. The Grade Analyzer
# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
            
def average_grade(grades):
    total_sum = 0
    for grade in grades:
        total_sum += grade
    average = total_sum/len(grades)
    return average

def grade_calculator(grades):
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade
    
def grade_categorizer(grades):
    letter_grade=[]
    for grade in grades:
        if grade >= 90:
            letter_grade.append("A")
        elif grade >= 80:
            letter_grade.append("B")
        elif grade >= 70:
            letter_grade.append("C")
        elif grade >=60:
            letter_grade.append("D")
        elif grade >= 50:
            letter_grade.append("F")
    return letter_grade
