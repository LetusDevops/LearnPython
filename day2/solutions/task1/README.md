## Task 1: WAP to create a function which returns the sum of all the element  provided to it as an arguement. The arguement list will be dynamic.

Topics:
- *args
- function
- list

The *args  i.e. *<variable_name/function>. treats every element seperately
only if arguments provided without key assignment

The argument passed to the *args are converted to tuple

It adds default space in the arguments pass to it.
```
>>>string  = input("Enter string : ")
Enter string : 12 34 56
>>>
>>>print("Printing string  as it is: ", string)
Printing string  as it is:  12 34 56
>>>
>>>print("Printing string using *args :", *string)
Printing string using *args : 1 2   3 4   5 6
```

# Resources that helped to understand better:
(PyGotham 2014 *args **kwargs talk)[https://youtu.be/bm-ZwhNzZkw]

(Difference between args and kwargs)[https://stackoverflow.com/questions/18753627/difference-bewteen-args-and-args-in-python]