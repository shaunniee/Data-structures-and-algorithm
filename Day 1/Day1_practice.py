# Print statement
print("Hello World")

# Variables
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

age=20
price=19.95
print(age)
first_name="Shaun"
last_name="Dsouza"
is_online=True
is_legal=False

# Exercise
# Check in a patient named John smith.He is 20 years old and is a new patient.Write 2 variables to register the patient with name,age.
# Bonus:receive input from patient (use the input function)

# step 1:Recieve the patients name and store it in the variable
patient_name=input("What is your name:")

# Step 2:Greet the patient
# Use string concatenation for this step
# String concatenation means add strings together.
# Use the + character to add a variable to another variable
print("Hello" + patient_name + "!")
# Using the ‘%’ Operator for String Concatenation
# The ‘%’ operator allows you to embed variables in a string.
# result = 'My name is %s and I am %d years old.' % (name, age)
print("Hello %s"%(patient_name))
# String Concatenation Using the format() Method
# The format() method is a more modern way to format strings in Python. It’s more readable and versatile than the ‘%’ operator. 
# result = 'My name is {} and I am {} years old.'.format(name, age)
print("Hello {}".format(first_name))

# Step 3:ask for age and output the patient details
age=input("{} could you please tell us your age: ".format(patient_name))
print("Patient details: Name {} , Age {}".format(patient_name, age))


# Type conversion

birth_year=input("Enter your birth year: ")
# when u enter the birthyear it will be stored as string
# To convert it into integer we can use the int function : int()
# In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.

# There are two types of type conversion in Python.

# Implicit Conversion - automatic type conversion
# Explicit Conversion - manual type conversion

# In Implicit type conversion of data types in Python, the Python interpreter automatically converts one data type to another without any user involvement. For example when u add and integer and float it implicitly converts the result into float
a=10
b=12.3
print(a+b)

# In Explicit Type Conversion in Python, the data type is manually changed by the user as per their requirement. With explicit type conversion, there is a risk of data loss since we are forcing an expression to be changed in some specific data type.
# Since the input of the birthyear is in string we explicitly convert it into integer

birth_year_integer=int(birth_year)
print(2024 - birth_year_integer)

birth_year_float=float(birth_year)
# String and string functions
practice_string="Hi my name is shaun"
# upper() function converts string into upper case
print(practice_string.upper())

# .find() returns the matching index in that string
# index in python starts from 0
print(practice_string.find("s"))
# If none the string in find does not match anything it returns -1
# Python is case sensitive.So s and S are treated differently in this case
print(practice_string.find("s"))
# The above code returns 14 as s is present in the 14 index
print(practice_string.find("S"))
# The above code returns -1 as capital S is not present in the practice string

# .replace() function is used to replace a peice of string
print(practice_string.replace("shaun","Vivian"))
# The above code replaces shaun by vivian from the practice string
 
# To check is a peice of string or a word is present in a statent we can use the find funtion or the in function
# if the find function returns a  postive index means it is present in the string 
print(practice_string.find("Hi"))
# The above peice of code returns 0 indicating that it is present in the string
print("Hi" in practice_string)
# The above piece of code returns truth or false
# In this case it returns True 

# Arithemtic operators
# Here are the different types of arithmetic operators in Python:
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%)
# Exponentiation (**)
# Floor Division (//)
a=10
b=3
# Addition
print(a+b)

# Subtraction
print(a-b)

# Multiplication
print(a*b)

# Division
print(a/b)

# Modulus
print(a%b)

# Exponentiation
print(a**b)

# Floor division
print(a//b)



