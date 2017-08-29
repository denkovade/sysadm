
# This program is part of my learning pythong 
# This program says hello and asks for my name.
# I'm using Python 2.7.12 (default, Nov 19 2016, 06:48:10)

print('Hello world!')
#print('What is your name?') # ask for their name
myName = raw_input('What is your name? ')
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
#print('What is your age?') # ask for their age
myAge = raw_input('What is your age? ')
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
