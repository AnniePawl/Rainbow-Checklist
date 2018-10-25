# Create empty list object to put in memory
# Code will run within object and passs in value to add
# Can be written at checklist = [] OR ...
# checklist = list()

checklist = []

#CRUD (Create, Read, Update, Destroy) Functions
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

# Loops over all items, prints everything in list
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#   Checklist Item
def mark_completed(index):
    checklist[index] = '√' + checklist[index]
    return checklist[index]


# User Input Function
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    # print("User input: {}".format(user_input))
    return user_input

# Updates value in checklist with new value
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Add an Item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        #Item_index must exist or program will crash.
        print(read(int(item_index)))

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "U":
        num_index = int(user_input("Index Number?"))
        item_index = user_input("Enter index item:")
        update(num_index), item_index)

    elif function_code == 'D':
        index = int(user_input('Index Number?'))
        destroy(index)

    # Check off item
    elif function_code == "M":
        item_index = int(user_input("Select item to check off:"))
        mark_completed(item_index)

    # Uncheck Item
    # elif function_code == "UC":
    #     item_index = int(user_input("Select item to uncheck:"))
    #     un_mark(item_index)

    # Stops Infinite Loop
    elif function_code == "Q":
        return False
    # Catch all
    else:
        print("Unknown Option")

    return True

#Test CRUD Functions
def test():
    create('grimy key card')
    create('baby dragon')
    create('wiggly pinecone')
    create('childish sugar packet ')

    update(2, 'saucy succulent')
    # destroy(1)

    # print(read(0))
    # print(read(1))
    # print(read(2))
    # print(read(3))


    # Test Check Mark Feature
    # create('Jello Shots')
    # mark_completed(1)
    # print(read(1))

    # select('C')
    # list_all_items()
    # select('R')
    # list_all_items()

    # user_value = user_input('Please Enter a Value:')
    # print(user_value)

    # list_all_items()
test()

#Condition starts True, but changes to False during runtime
# Uncomment running = True when done debugging
# running = True
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, U to update the list, M to check off list item and Q to quit")
    running = select(selection)
