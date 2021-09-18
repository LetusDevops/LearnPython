# Solution for task1 day1

# Initializing a string
course = "Learn python with LetUsDevOps"
print("length of string course: ", len(course))  # length of course
print("first char: ", course[0], "last char :", course[-1])  # length of course
# substring so OP but python allocate new memory
print("substring a string: ", course[0:3])
print("Checking if a string starts with a specific first letter: ", course.startswith("p"))

# formating strings
first = "Hamdi"
last = "Nait Limam"
full = f"{first} {last}"
print("Concating string with formated string: ", full)

# Initializing an integer
count = 5
x = y = 1
x, y = 2, 1
print("typeOf count is :", type(count))  # typeOf()
print(f"sum of two integers :{x+y}\nsubsctraction of two integers: {x-y}\nmultiplication of two integers: {x*y}")

# Initializing an Array
# Arrays are used to store multiple values in one single variable containing homogeneous elements i.e. belonging to the same data type.
t = [3, 1, 2, 3]
print("Printing the array: ", t)
print("length of the array is :", len(t))
print("Printing ID of the array t before: ", id(t))
t.append(4)  # pushing another value into the array
t.sort()
print("Printing ID of the array t after: ", id(t))
print("Printing the array after the changes: ", t)