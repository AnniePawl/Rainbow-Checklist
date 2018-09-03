
checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

def create(item):
    checklist.append('Blue')

def read(index):
    item = checklist[index]
    return item

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)


#TestFunction
create("purple sox")
create("red cloak")

print(read(0))
print(read(1))

update(0, "purple socks")
destroy(1)

print(read(0))
print(read(1))

for list_item in checklist:

def list_all_items():
    for list_item in checklist:
        print(list_item)

        def list_all_items():
    index = 0

for list_item in checklist:
    print(index + list_item)
        ndex += 1

    #Do something

# print("User Stories-- Frame user stories in a loose template. Approach propblem from the perspective of the user")
#
# print("CRUD- 4 fundamental operations for software to be complete: create, read, update, destroy")
#
#
# #Python Syntax
#  print ("This is a print statment")
#  print ("We are supplying blocks of text")
#  print ("Text in python is called a string- a series of letters, numbers, or symbols connected in order")
#  print ("We can combine" +"multiple strings")
#
#  print ("Error Handling---")
#  #  "<ul></ul>     <ul></ul>
#  </import>     <ul></ul>
#  </import> <ul></ul>
#  </im>d quotes will cause a SyntaxError')
#
#  # No quotes will cause a NameError
#
# print ("Variables are things that are subject to change")
#
# greeting_message = ("Welcome!")
# todays_date = ("09/01/18")
# print (todays_date)
#
# #Arithmetic Examples
#
# product = 20 * 3
# print (product)
#
# remainder = 1398 % 12
# print (remainder)
#
# print("Hello World")

#
# def my_fun_function(says_this):
#     print(says_this)





# todays_date = ("06.02.18")
# print(todays_date)
#
# def create(item):
#     checklist.append(item)
#
# def read(index):
# item = checklist[index]
# return item
#
# #Updating Variables
#
# money_in_wallet = 100
# sandwich_price = 10
# sales_tax = .5 * sandwich_price
#
# sandwich_price += sales_tax
# money_in_wallet -=sandwich_price
