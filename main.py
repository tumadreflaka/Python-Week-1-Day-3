#####################Bell Ringer#######################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it

computer_brand = "Dell"
intel_chip = "i5"
windows_os = "Windows 10"

print(f"This is a {computer_brand} computer. It has an {intel_chip} chip and it runs {windows_os}.")

# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.

print("Christopher Escobar")
print("Friday, August 25th")
print("Spiderman ATSV")

# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."

print("My name is Christopher Escobar\nI am 16 years old")

name = "Chris"
age = 16
print(f"In 20 years, {name} will be {age + 20} years old.")

###########################end bell ringer##################################











###########################String Practice##################################
# Syntax is the way we write down
# print("Hello World")
# Name = "John"
# In other languages, this is different
# In Javascript for example, you define 
# Variables with let or const or var
# In Python you just give your variables a 
# Name and then define it with a value

word = "Python is cool and stuff OOGA BOOGA"
print(word)
print(word[5])
print(word[8])
print(word[10])
print(word[-1])
print(word[-2])
print(word[-3])

# STRING SLICING
print(word[10:14])
print(word[19:24])
print(word[0:6])
print(word[7:9])
print(word[-1:-6])
print(word[-1:-6])
print(word[ :0])
print(len(word))
# print(len(xxx)) ---> # of words

print(word[:13])
print(word[13:])
print(word.find("is"))
# Finds the index of a substring
print(word.upper())
print(word.capitalize())
# This capitalizes the first word
cool = word[10:14]
print(cool.capitalize())
print(word.replace("Python", "javascript"))
print(word.replace("cool", "ugly"))

######################## CHALLENGE ##########################

blue_beetle_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
print(len(blue_beetle_summary))
print(blue_beetle_summary.upper())
print(blue_beetle_summary.lower())
print(blue_beetle_summary.replace("Blue" , "Red"))
print(blue_beetle_summary.find("Beetle"))
print(blue_beetle_summary[334:340])
print(blue_beetle_summary[::-1])

##################### END CHALLENGE ##########################

# String Practice #1: try this in repl.it
# Define a string containing your full name.
# Print the first 3 letters of your name using string slicing.
# Convert your name to uppercase and print the result.
# Use string formatting to print "My name is [Your Name]."

# String Practice #2
# Write Python code that prints the following, by calling the print function just once:
# Line 1
# Line 2
# Line 3

# String Practice #3
# Write Python code that prints the following:
# A	B	C
# D	E	F
# G	H	I

# String Practice #3
# Write Python code that prints the following:
# Backslash (\)
# Forward Slash (/)

##########################input practice#############################################
# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.


###########################time for a real challenge!!!!##################################
# last slide