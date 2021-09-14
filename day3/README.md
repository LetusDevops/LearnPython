## Learn Python with Let Us DevOps

### Day 3: Data format conversions, JSON <-> DICT, XML <-> DICT and regex in Python. 

#### Why JSON and XML to dict? 

Whenever you make a request to get any data you will get the data as JSON or XML or provide the data in any of these formats. So its important to understand how the coversion between these works.

Since you understood dictionaries in the last lesson. If you are able to convert the data in dictionary, you will be able to operate on it. 

### Task 1: Convert a dictionary object to JSON and then convert it back to dictionary. Do the same with XML. 

You can use json and xmltodict modules for accomplishing the above tasks. You can use the below object:
```
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

### Task 2: Read and understand what are Regular expressions and they evaluate. 
It is really important to understand how they evaluate else a bad regex can take down your systems. Read about backtracking in REGEX evaluation. 

### Task 3: Given below logs try to parse them and get unique IP from where the requests are coming. 
```
TLSv1.2 AES128-SHA 1.1.1.1 "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 2.2.2.2 "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 3.3.3.3 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 4.4.4.4 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1 AES128-SHA 5.5.5.5 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1.2 ECDHE-RSA-CHACHA20-POLY1305 6.6.6.6 "Mozilla/5.0 (Linux; U; Android 5.0.2; en-US; XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.2.1164 Mobile Safari/537.36"
TLSv1.2 AES128-SHA 1.1.1.1 "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 2.21.2.2 "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 3.31.3.3 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"
TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 2.4.4.4 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1 AES128-SHA 5.5.5.51 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
TLSv1.2 ECDHE-RSA-CHACHA20-POLY1305 6.6.6.6 "Mozilla/5.0 (Linux; U; Android 5.0.2; en-US; XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.2.1164 Mobile Safari/537.36"
```

Solve it with first string manipulation and then regex. 
You can read these article for help: 
* [Log Parsing using regex](https://www.learnsteps.com/log-parsing-in-python-using-regular-expressions/)
* [Log Parsing using String manipulation](https://www.learnsteps.com/log-parsing-in-python-read-how-you-can-do-it/)

This is a very important question in terms of DevOps interviews. You can get it at lot of interviews it Visa, Cred, Linkedin, etc.

### Online Problems that you can try solving: 
1. [Validate Roman Numerals](https://www.hackerrank.com/challenges/python-loops/problem)
2. [Validate Phone Numbers](https://www.hackerrank.com/challenges/validating-the-phone-number/problem)
3. [Find all and finditer](https://www.hackerrank.com/challenges/re-findall-re-finditer/problem)
4. [Other Problems](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-regex)

You can try solving as many as possible to get good hands-on. 


### This is it for Day 3. All the best!
