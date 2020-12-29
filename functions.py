# Functions

# A function is a piece of reusable code that solves a task.  You can ‘call’ a function instead of writing the code yourself.  

# Python offers a lot of built-in functions to make life easier and we've have already seen a number of them including: 

# print() 
# round() 
# type()

# Another way of thinking about a function is a ‘machine’ that takes an input and produces an output.


# Functions help()

# To find out more about a function we can ask for information using the help() function.  

# To get help on the max() function, for example, we would use:

help(max)

# max(iterable, *[, default=obj, key=func]) -> value
# max(arg1, arg2, *args, *[, key=func]) -> value
# With a single iterable argument, return its biggest item. 
# The default keyword-only argument specifies an object to return
# if the provided iterable is empty.
# With two or more arguments, return the largest argument.

# In the documentation if there is more than one argument they are separated by commas.  

# Those arguments that have been assigned a default value are optional and if there is no default value in place
# the information is 'required'.

# For example, sorted() has multiple arguments:

help(sorted)

# sorted(iterable, key=None, reverse=False)
# Here we see that sorted() takes three arguments: iterable, key and reverse:
# iterable is what we are sorting, and IS required
# key=None means that if you don't specify the key argument, it will be None. 
# (key can be used to customise the order).
# reverse=False means that if you don't specify the reverse argument, it will be False.


# Exercise 1

# Two lists are provided below:

lista = [17, 20, 20, 45, 56, 204, 54]
listb = [19, 24, 54, 64, 13, 657, 424]

# a) Use the max() function on lista. What is returned?

# b) The documentation says that max() can take two arguments. Pass both lista and listb into max() what is returned? 
# (View help(max to help!))

# c) Print the result of listb using the sorted() function, then add the optional argument to show the sorted output in reverse
print(sorted(lista, reverse = True))
#### Optional extras ####

# d) View the help documentation for print(). Currently everytime you combine numbers or booleans (e.g. print(2,3)),
# a space will be inserted between each argument. Work out how to alter this to a comma. Then alter this to a colon.

help(print)
print(2,3, sep = ';')
# Creating your own function

# Functions can be built-in as we have seen but we can also create our own.

# Once created a function can be used anywhere in that script.  

# The structure of a function is show below, note the colon on the first line and the indent on the second:

def hello_function():
	print("Hello! How are you doing?")

hello_function() #This is 'calling' the function. Note We are no longer inside the function, because we have left the indented section. 

# Here, the def key word creates the function

# The brackets allow us to add arguments if we wish - in the above example we haven't added any.

# The colon lets python know that any subsequent indented information is part of what the function should do. 

# To leave the function, we stop indenting our code.

#We can execute the function, by ‘calling’ it (bottom line above)


# Why create functions?

# In the example above we printed a simple line of text but what if we have common tasks that need to be repeated?  

# If we had just added a print statement: print(‘Hello! How are you doing?’)

# this could have been copy/pasted multiple times into the script…

# ...However, what if I needed to change the contents?  I would need change it multiple times.  

# By using my function, I can change it once 

# and it it will be reflected throughout the code wherever it is called.  

# For example if I change the greeting from ‘Hello’ to ‘Hi’ , it would be as simple as:

def hello_function():
	print("Hi! How are you doing?")

hello_function() #Calling the function


# The difference between 'printing' and 'returning' a value

# We could chose to ‘return’ our value instead of printing it. We would not see the output, but we would be able to 

# 'chain' methods to it.  

# For example, below we return a string and we could chain string methods such as: .upper and .lower to the value ‘returned’:

def hello_function():
	return("Hello! How are you doing?")

print(hello_function().upper()) #Calling the function

# In this example, we would no longer see an output when we call our function, 
# unless we print out the function call as per the bottom line in the example above. 


# Passing an argument to a function

# We can add arguments to our function in the parenthesis (curved brackets).

# Here the parameter is a ‘greeting’, this will allow the user to specify the ‘greeting’ when the function is called:
def hello_function(greeting):
    return (greeting)

print(hello_function('Tadaa!'))

# Note, now if we called the function and didn't specifiy the greeting argument we would get an error. 

# Therefore, our argument is known as a required argument.


# Multiple arguments

# We can also create a function with multiple arguments (some of which are required and some that are optional). 

# For example the function below has one required argument and one optional:

def hello(greeting, name='Rich'):
    return (greeting + " " + name)

print(hello('Hi'))

# In the example above we have specified a second parameter ‘name’.  

# By saying name = 'Rich' we have told the function that if the ‘name’ is not specified

# when the function is called, it should still run but use default the value

# If a ‘name’ is specified when the function is called, then the default will be ignored.

# Note: If you intend to make any of the arguments a key word/optional argument, place these after the

# required positional arguments as shown above


# Exercise 2

# a) Create and test a new function: 'my_savings'. Initially it won't have any arguments. When you call it should print "My savings are:"

def my_savings(expenditure, income = 2500):
	print("my savings are", income - expenditure)

my_savings(1000) 

# b) Amend a) to add a required argument called income, then:

	# Call the function without the argument to check the error

	# Pass in 3000 when calling the function and check that the function works correctly

# c) Amend the print out from the function so that it now prints the amount after "My savings are:"

# d) Amend your function: Create a new required argument called expenses. Then change your income argument to have a 
# default value of 2000. Adjust the output to show income - expenses

#### Optional extras ####

# e) Create a new function that will take any number and double it

# f) Amend e) to take any number and raise it to the power of 2

# g) Amend f) to take any number and raise it to the power of any number the user passes in

# h) Amend g) so that the default power is 2 but this can still be altered



# Positional and named arguments

# When calling a function it possible pass the arguments both by their 'position' or their 'name'.
# The simple function below adds two arguments a and b

def my_sum(a,b):
	total= a+b
	print(total)
	return total

my_sum(3,5) #calling the function using 'positional' arguments

my_sum(b=3, a=5) #calling the function using 'named/key word' arguments


# Global versus local variables


# When using variables within a program / function it is important to keep the scope of the variable in mind. 

# A variable’s scope refers to the particular places it is accessible within the code of a given program. 

# A global variable is declared outside the function and it's scope is the entire program

# A local variable is declared inside a function and it's scope is the function in which it is declared

# Example 1

# In this example, num1, num2, and num3 are all global variables

# Variable a, b and c are all local variables

# Running a print from inside the function will work as expected

# Running a print from outside of the function will fail

num1 = 0
num2 = num1+6

def my_function():
	c=1 
	b=2
	a=b+c
	print("This is 'a' and it has been printed from inside the function\n",a)

num3 = num1 * num2

my_function() 

# When we 'call' the function 'a' prints normally as the function output

# print(a) #will error variable 'a' is not recognised outside the function


# Example 2

# In this example the print inside function2() will do nothing as d is not local to function2()

# If we attempt to print d outside of function1() a NameError will be received
x=0

def function1():
	d=1
	print(d)

def function2():
	e=2
	print(d) 

function1() # This is calling function(1)

# function2() #This is calling function2().  It will fail because function2() does not have a variable called 'd'.

# print(d) #NameError. 'd' is not recognised outside of the function.


# Example 3

# In this example we can see that global f is separate to local f

# When we run function1() nothing is printed (no print statement)

# When Python reaches the print statement at the end, global f is printed

# Global f is NOT affected by calling function1()

f = 0 # global f

def function1():

	f = 7 #local f

function1() #Calling function1()

print(f) #This prints out global f value 0, and not local f value 7 as it is outside the function


#Example 4

#In this example, we can see a global variable being declared global within a function

#In this instance, the function will modify the global variable when it is called

#When we call the function, the print following the call returns 7

g=0 #global g

def function1():
	global g
	g=7 #local g

function1() #calling the function
print(function1()) 
print(g) 


# Example 5

# Accessing a global variable is different to modifying a global variable

# When Python can't access a local variable a it automatically checks to see if there is a global one instead

# With no local h, the print would be 5

# If there was a local variable h within the function, Python would take this as first choice

# e.g. if a local h=7 has been added, global h would be ignored and the print would be 9

h=3

def function1():
	#h = 7 #This local variable would be taken as first choice
	i=h+2
	return(i)

print(function1())


# Exercise 3

# a) Create a new function called greeting that will store a text variable of "Hi 'name'" where the name is an argument of the function

# b) Adjust a) so that the text variable is saved as a global variable. Test this by trying upper() or lower() on the variable
# outside of the function

# c) Create a new function that sums together two number arguments. Store the output as a global variable and test this using round()
# outside of your function

#### Optional extras ####

# d) Create a variable called savings with a value of 0

# e) Create a function called add_savings that will update savings by whatever number is passed into the function and store it as new_savings. 
# Test that this works correctly by printing savings checking if the value has updated

# f) Create a varible called my_list which is a blank list

# g) Create a function called add_element which will append a new item to my_list. Hint - try the .append method















