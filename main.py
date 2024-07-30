# Step 01
# Create a variable called number and assign it the value 5

number = 5

# Step 2
# Delete your number variable and its value. 
# Then, declare another variable called text and assign the string Hello World to this variable.

text = 'Hello World'

# Step 3
# Print your text variable to the screen by including the variable name between the opening and closing parentheses of the print() function.

print(text)

# Step 4
# Now, instead of printing text, print just the character at index 6

print(text[6])

# Step 5
# You can also access string characters starting from the end of the string. The last character has an index of -1, the second to last -2 and so on. 
# Now modify your existing print() call to print the last character in your string.

print(text[-1])

# Step 6
# Modify your existing print() call to print len(text).

print(len(text))

# Step 7
# Another useful built-in function is type(), which returns the data type of a variable. 
# Modify your print call to print the data type of text.

print(type(text))

# Step 8
# Now go to a new line and create another variable called shift and assign the value 3 to this variable.

text = 'Hello World'
print(type(text))
shift = 3

# Step 9
# And now print your new variable.

print(shift)
print (type(shift))

# Step 11

# Key aspects of variable naming in Python are:

#    Some words are reserved keywords (e.g. for, while, True). They have a special meaning in Python, so you cannot use them for variable names.
#    Variable names cannot start with a number, and they can only contain alpha-numeric characters or underscores.
#    Variable names are case sensitive, i.e. my_var is different to my_Var and MY_VAR.
#    Finally, it is a common convention to write variable names using snake_case, where each space is replaced by an underscore character and the words are written in lowercase letters.

# Remove both calls to print() and declare another variable called alphabet. Assign the string abcdefghijklmnopqrstuvwxyz to this variable.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Step 12 - Caesar cipher

# The first kind of cipher you are going to build is called a Caesar cipher. Specifically, you will take each letter in your message, find its position in the alphabet, take the letter located after 3 positions, and replace the original letter with the new letter.
# Start by finding the position of the first letter in the string. One way is to use the built-in find() function:
# a_string.find(char)
# Above, char is the character you want to locate, and a_string is the string you want to parse.
# At the end of your code, call find() on your alphabet string and pass text[0] to the function.

alphabet.find(text[0])

# Step 13

# Now assign the value returned by alphabet.find(text[0]) to a variable named index. Then, print its value.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)

# Step 14

# find() returns the index of the matching character inside the string. If the character is not found, it returns -1. As you can see, the first character in text, uppercase "H", is not found, since alphabet contains only lowercase letters.
# You can transform a string into its lowercase equivalent with the lower() function. Add another print() call to print text.lower() and see the output.

print(text.lower())

# Step 15

# Remove the last print() call. Then, instead of text[0], pass text[0].lower() to find() and see the output.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)

# Step 16

# As you can see from the output, "h" is at index 7 in the alphabet string. Now you need to find the letter at index 7 plus the value of shift. For that, you can use the addition operator, +, in the same way you would use it for a mathematical addition.
# Declare a variable named shifted and assign it the alphabet letter at index plus shift.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)

# Step 18 - Loop

# Repeating this process for each character in text can be tedious. Thankfully, you can simplify it using a loop. 
# A loop allows you to systematically go through a sequence of elements and execute actions on each one.
# In this case, you'll employ a for loop. Here's how you can iterate over text:

        #  for i in text:

# for is the keyword denoting the loop type. 
# i is a variable that sequentially takes the value of the elements in text. The statement ends with a colon, :.
# Remove everything after the alphabet line. Then write a for loop to iterate over text.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for i in text:

# Step 19

# The code to execute at each iteration — placed after the : — constitutes the body of the loop. This code must be indented. In Python, it is recommended to use 4 spaces per indentation level. This indented level is a code block.

    # for i in text:
    #     <code>

# Give your for loop a body by adding a call to print(i). Remember to indent the loop body.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:
    print(i)
    
# Step 22

# The iteration variable can have any valid name, but it's convenient to give it a meaningful name.
# Rename your i variable to char.

for char in text:
    print(char)

# Step 23

# Before printing the current character, declare a variable called index and assign the value returned by alphabet.find(char) to this variable.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    index = alphabet.find(char)
    print(char)

# Step 24

# An argument is an object or an expression passed to a function — between the parentheses — when it is called. 
# The print function can take multiple arguments, separated by a comma.
# Add a second argument to print(char) so that it prints the character and its index inside the alphabet.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    index = alphabet.find(char)
    print(char, index)

