# Creating arrays with numpy

import numpy as np

# Create a 1d array using a single list

my_array = np.array([3,6,9])

# print(my_array)

# Create an nd array using a list of lists

my2d_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(my2d_array)

print(my2d_array[3,])


# Inspecting an array

# Check the dimensions of an array using .ndim

print(my_array.ndim)

# See the shape of an array using .shape
# The left hand output is the number of rows and the right hand is the number of columns

print(my2d_array.shape)

# Count the number of elements in an array using .size

print(my_array.size)


# Check the data type of an array using .dtype

print(my_array.dtype)
print(my2d_array.dtype)


# Convert the type of an array using astype()

print(my2d_array.astype('float32'))


# Array comparisons

# Check if one array is equal to another

print(my_array == my2d_array)

# Check if one array is not equal to another

print(my_array != my2d_array)

# Check if one array is greater than another

print(my_array > my2d_array)

# Check if one array is greater or equal to another

print(my_array >= my2d_array)

# Check if one array is less than another

print(my_array < my2d_array)

# Check if one array is less than or equal to another

print(my_array <= my2d_array)


# Check how the elements in an array compare to a value

print(my_array > 5)




# Array aggregate function

# Carry out an array-wise sum using np.sum()

# Use the axis= argument, to make the calculation by axis

# axis =0 will sum the columns, axis= 1 will sum the rows 

print(np.sum(my2d_array))
print(np.sum(my2d_array,axis = 0))

# Locate the array-wise minimum value using np.min()
# Use the axis= argument, to make the calculation by axis

print(np.min(my2d_array))
print(np.min(my2d_array,axis = 0))

# Locate the array-wise maximum value using np.max()
# Use the axis= argument, to make the calculation by axis

print(np.max(my2d_array))
print(np.max(my2d_array,axis = 0))

# Calculate the mean using np.mean()
# Use the axis= argument, to make the calculation by axis

print(np.mean(my2d_array))
print(np.mean(my2d_array,axis = 0))

# Calculate the median using np.median()
# Use the axis= argument, to make the calculation by axis

print(np.median(my2d_array))
print(np.median(my2d_array,axis = 0))

# Calculate the standard deviation using np.std()
# Use the axis= argument, to make the calculation by axis

print(np.std(my2d_array))
print(np.std(my2d_array,axis = 0))



# Subsetting and slicing

# To subset an array we identify the index in square brackets []

print(my_array[0])

# In a 2 dimensional array we would use two indices, the row and the column [ , ]

print(my2d_array[0,1])

# To select a slice we would use a colon to separate the 'from' and 'to' indexes

# The first index is included, the second is excluded

print(my_array[0:2])

# In a 2 dimensional array, we would again use a comma between the row and column selections

print(my2d_array[0:2, 0:2])

# To select all the columns for a row, just use a colon after the comma

print(my2d_array[0, :])

# To select all the rows for a column, just use a colon before the comma

print(my2d_array[: ,0])


# Exercise 1

# a) If not already done import numpy as np to use in your answers

import numpy as np

# b) Use the information provided below to create two new arrays, a and b

list_a = [1, 3, 3, 2, 5, 2, 4,]
list_b = [[1, 2, 3, 4, 5,6,7],[1, 3, 3, 2, 5, 2, 4,]]

a = np.array(list_a)
b = np.array(list_b)
print(a)
print(b)


# c) a is a 1D array and b is a 2D array; use .ndim to confirm this

print(a.ndim)
print(b.ndim)

# d) Use .shape() to review the shape of each array

print(a.shape)
print(b.shape)

# e) Check the number of elements in each array using .size()

print(a.size)
print(b.size)

# f) Find out the .dtype of b, and then convert it to 'float32' using .astype()

print(b.dtype)

# g) Print the second element of array a

print(a[1])

# h) Print the bottom row of array b

print(b[-1,])

# or

print(b[1,])

# i) Print the second column of array b

print(b[:,1])

#### Optional extras ####


# j) What are the minimum and maximum values of array b?

print(np.min(b))
print(np.max(b))

# k) Calculate the: the mean, median and standard deviation accross the rows of array b

print(np.mean(b, axis = 1))

# l) Print the bottom row of b by 1.8 and then add 32, (this calculation converts celsius to farenheit)

print((b[1,] * 1.8)+32)