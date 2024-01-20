# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# Pseudocode 

# Creating a variable to start the loop from 0 
previous_num = 0 

# Creating loop 
for i in range(10): 

# Showing the result 
    print("Current Number", i, "Previous number", previous_num, "Sum", previous_num + i) 
    previous_num = i 
