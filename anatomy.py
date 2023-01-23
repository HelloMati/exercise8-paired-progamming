# import a package/ library
import sys

# declare a variable that is the number of items in the list called argv
arguments = len(sys.argv)

# conditional statement, if the variable called arguments contains more than 1 item run the built-in function to print the string
if arguments > 1:
    print("Too many arguments")
else:
    # if the argument count is greater than 1 then print the string 'hello' with the variable called location
    location = 'World'
    print("Hello", location)

# run the print function to print the string plus the first argument in the list which is located using the position index at 0
print('Goodbye from ' + sys.argv[0])
