## Learn Python with Let Us DevOps

### Day 4: The mighty REQUESTS module. 

We will start today with a small thought to keep you motivated :P. Motivation is a burst of energy that can help you start anything but you need some discipline to keep doing it for longer time. You get results with long term effort. Not with one day work. Same will happen with this python learning exercise. :)


Moving on, we have talked before that lot of automation on devops side is done with help of APIs. If you have not read about APIs before I recommend you going through this article: 

[What are apis?](https://www.learnsteps.com/what-are-apis-and-how-to-build-api/)

Requests module is a way to make these API calls. You can use this to call any endpoint. For example
```buildoutcfg
import requests
data = requests.get("https://google.com")
print(data.text)
```
Here it will print the google.com website data as text. But when we call apis we get JSON mostly as data. 



Now in our day 2 and day 3 we understood about dictionaries json and xml. If you have not you can go through this video.  
[Youtube video on dictionaries](https://www.youtube.com/watch?v=mKmX25HFUmQ&list=PLhqPDa2HoaAZN9pG0cUugTmgAddRtF3zK&index=8&ab_channel=LetUsDevOps)

So our tasks today revolves around making API calls and parsing the API data. 

### Task 1:  Read and understand different ways to make api calls. Read about below mentioned things and try them out. 
1. methods: GET POST PUT DELETE
2. Headers
3. Status COde
4. HTTP vs HTTPS

### Task 2: GET all the repo information from any github account and present it in sorted manner on basic of stars.

You can use these apis. [GITHUB API RESOURCES](https://docs.github.com/en/rest/overview/resources-in-the-rest-api)

### Task 3: Create a tool to parse the news feed and print them. You can choose any rss feed. These feeds are in XML and you need to print them as String. 
You can use learnsteps feed: [Feed](https://www.learnsteps.com/feed/)

**Extended tasks:** Host it on heorku. This will also act as a small project if you extend more feature. To host it on heroku you have create an app for it. You can try out flask. If you want are very curious, otherwise we will talk about flask also in comming days. 

These tasks may take some time, so we will post the next day content after a GAP of 3 days. Try to complete all the exercises. 

#### Important Note: Practice makes a man perfect. Keep practicing these problems. If you skip them, there is a good chance you can end up even after going through all the days. 


Also as mentioned in previous days, contributions are welcome, here is a small guide on how you can contribute to any open source project. 

[How to contribute in Open Source](https://www.learnsteps.com/how-to-contribute-in-open-source-and-creating-the-right-merge-request/)
### This is it for Day 4. All the best!
 
