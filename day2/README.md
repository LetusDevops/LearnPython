## Learn Python with Let Us DevOps

### Day 2: Functions, thier usage and Dictionaries.

After day 1, I am assuming you are aware of basic loops and data structures in python. Today we are going to talk about functions.

Below are few reason why you want to create a function: 
1. Reusable code
2. Seperating the concern. What I mean here is you want to make your code such that you can seperate out different functionalities of program and convert them as functions. 


In python creating a function is very simple: 

```buildoutcfg

def function_name(arguement1, arguement2):
    // do something with arguement 1 and arguement 2 and return
    return something
```

It is really simple to create and use functions. 
There is another concept with arguements that is very interesting and powerful to use. 
#### *args and **kargs

Read about args and kargs. 

### Task 1: WAP to create a function which returns the sum of all the element provided to it as an arguement. The arguement list will be dynamic.
Focus on understanding how you can use **args. This is very powerful when you design a system. 

### Task 2: WAP to create a function in which the arguements are users and their marks and return three value. User with maximum mark, Average_marks, Users below failing marks. Below is sample of output.
```buildoutcfg
("Raul": 99),("avg_marks","55"),["Hidan", "Goku", "Timon", "Sasuke", "Saitama"]
```
Focus on understanding how you can use *kargs and their similarities with dictionaries. 

## Dictionaries

Dictionaries are super powerful in python and very easy to use. These are nothing but key value pair. Dictionaries can be nested and can hold any data type. Look at the example below

```buildoutcfg
a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "frieds": [
            {
                "name": "Naruto",
                "friend_points": 28,
                "enemies": ["Saitama"] 
            },
            {
                "name": "Boruto",
                "friend_points": 18,
                "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "Alex",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Soniya",
            "friend_points": 128,
            "enemies": ["Saitama"] 
            }
        ]
    },
    {
        "name": "King",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"] 
            }
        ]
    }
    
]
```

So you can see a dict can have dict as value of key, data types as integers or strings. 

## TASK 3: WAP to traverse the above given dictionary and print every information about the user. 
The motive of this tasks to help you understand what dictionary is and how to traverse them if you are given. 
### **Now you ask why?** 

So most of the times you make any API call which are core tasks of devops automation you get the data as these dictionaries so having understanding of these will be very handy. 

Online Problems to attempt:
1. [Default Dict](https://www.hackerrank.com/challenges/defaultdict-tutorial/problem)
2. [Write a Function](https://www.hackerrank.com/challenges/write-a-function/problem) This is a medium question so its ok if you are not able to solve it. 

###Thats it for day 2.
### ALL THE BEST!