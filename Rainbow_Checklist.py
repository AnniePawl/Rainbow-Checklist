# Imports
import sys
# from termcolor import colored
from os import system, name


# Create empty list object to put in memory
rainbow_checklist = []

#CRUD (Create, Read, Update, Destroy) Functions
def create(item):
    rainbow_checklist.append(item)

def read(index):
    return rainbow_checklist[index]

def update(index, item):
    rainbow_checklist[index] = item

def destroy(index):
    rainbow_checklist.pop(index)

# List all items functions- loops over all, prints all
def list_all_items():
    index = 0
    for list_item in rainbow_checklist:
        print("{} {}".format(index, list_item.title()))
        index += 1

# Check Items Off, and Uncheck
def mark_completed(index):
    rainbow_checklist[index] = '√' + rainbow_checklist[index]
    return rainbow_checklist[index]
def uncheck(index):
    rainbow_checklist[int(index)] = rainbow_checklist[int(index)].replace("√", "")
    return rainbow_checklist[index]

# User Input Function, displays prompt and waits for input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# Clear terminal between user selection for readability
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

# Select Operation (Create, Read one item, View all items)
def select(function_code):
    if function_code.upper() == "C":
        input_item = user_input("Add an item to your list:")
        create(input_item)
        print ("\x1b[6;30;42m" + "You've successfully added an item!")
        list_all_items()

    elif function_code.upper() == "R":
        item_index = user_input("Enter index of item you'd like to view: ")
        print(read(int(item_index)))

    elif function_code.upper() == "V":
        list_all_items()

    elif function_code.upper() == "U":
        num_index = int(user_input("Enter index of item you want to update: "))
        item_index = user_input("Enter replacement item:")
        update(num_index, item_index)

    elif function_code.upper() == "M":
        item_index = user_input("Enter index of item you'd like to check off: ")
        mark_completed(int(item_index))
        list_all_items()

    elif function_code.upper() == "UM":
        item_index = user_input("Enter index of item you want to uncheck: ")
        uncheck(int(item_index))
        list_all_items()

    elif function_code.upper() == "D":
        index = int(user_input('Enter index of item you want to destroy:'))
        destroy(index)

    # Stops Infinite Loop
    elif function_code.upper() == "Q":
        return False
    # Catch All
    else:
        print("Whoops, Try Again!")
    return True


# TESTS
def test():
    create('grimy key card')
    create('wiggly pinecone')
    create('childish sugar packet')
    create('baby dragon')

    # print(read(0))
    # print(read(1))
    # print(read(2))

    # update(1,'saucy succulent')
    # destroy(1)
    #
    # # Test Check Mark Feature
    # create('Jello Shots')
    # mark_completed(1)
    # print(read(1))
    #
    # select('C')
    # list_all_items()
    # select('R')
    # list_all_items()
    # select('V')
    # select('Q')
    # select('U')
    #
    # user_value = user_input('Please Enter a Value:')
    # print(user_value)

test()

# Condition starts True, but changes to False during runtime
# Uncomment running = True when done debugging
running = True
while running:
    selection = user_input(
        "Welcome to Rainbow Checklist!\nPress 'C' to add an item to your list.\nPress 'R' to read one particular item from your list.\nPress 'V' to view all list items.\nPress 'U' to update your list.\nPress 'M' to check an item off your list.\nPress 'UM' if you want to uncheck an item from the list. \nPress 'D' to delete an item from your list.\nPress 'Q' to quit!")
    clear()
    running = select(selection)

# Stretch Challenges
# √Add a function that unchecks checked items
# √Display colored text in the terminal
# √Clear terminal output between user selections
