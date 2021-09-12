"""
----------------------------------------------------------------------------------
Task 1: WAP to create a function which returns the sum of all the element 
provided to it as an arguement. The arguement list will be dynamic.
----------------------------------------------------------------------------------
The *args  i.e. *<variable_name/function>. treats every element seperaterly
only if arguments provided without key assignment
"""
def calculate_sum(*args):
    print("Type of *args : ", type(args))
    sum = 0
    print("Given Elements: ", args)
#All arguments passed to function are converted into tuple by default.
    for passed_number in args:
        sum += int(passed_number)
    return(sum)

numbers = (map(int,input("Enter the of numbers: ").split()))
print("Sum of elements : ", calculate_sum(*numbers))
string  = input("Enter string : ")

print("Printing string  as it is: ", string)

#It is printing string with space after every character
print("Printing string using *args :", *string)

"""
=================================================
Output: 
Enter the of numbers: 1 2 3 4 5 6 7 8 9 10           
Type of *args :  <class 'tuple'>
Given Elements:  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Sum of elements :  55
Enter string : 12 34 56
Printing string  as it is:  12 34 56
Printing string using *args : 1 2   3 4   5 6
=================================================
"""