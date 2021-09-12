# Solution of day1 task3

# Generating even and odd numbers with for loop
print('Generating Odd and Even numbers exerice with For loop!')
even=[]
odd=[]
for i in range(1,11):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print("The even numbers are: ", even)
print("The odd numbers are: ", odd)

# Generating even and odd numbers with while loop
print('Generating Odd and Even numbers exerice with while loop!')
even=[]
odd=[]
i = 1
while i <= 11:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
    i += 1

print("The even numbers are: ", even)
print("The odd numbers are: ", odd)

# Fizz Buzz Exercice
print('Welcome to Fizz Buzz exerice!')
for i in range(1,101):
    if i % 3 ==0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
    else:
        print(i)

