# Solution for day1 task1

# Simple iteration over a loop
list = [1,2,3,4,5,6,7,8,9]
print("Print the list with simple iteration:")
for i in list: 
     print(i, end=" ")

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
print(" ")
print("Printing range(5) loop:")
for x in range(5):
    print(x, end=" ")

print(" ")
print("Printing range(2,6) loop:")
for x in range(2,6):
    print(x, end=" ")

print(" ")
print("Printing range(0,10,2) loop:")
for x in range(0,10,2):
    print(x, end=" ")