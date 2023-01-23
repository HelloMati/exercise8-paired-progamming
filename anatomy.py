import sys

arguments = len(sys.argv)

if arguments > 1:
    print("Too many arguments")
else:
    location = 'World'
    print("Hello", location)

print('Goodbye from ' + sys.argv[0])
