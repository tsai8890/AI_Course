# NTU AI 2022 HW0

## Problem Description
```
    Capybara, one of the cutest animals in the world, needs to eat a lot of grass every day. 
You, a capybara guardian, have the sacred duty to herd capybaras. One day, Hashira, 
the most senior capybara guardian, gave you a map. When you read the map, you find that 
there are many little islands on the map. Each island is assigned with an integer, starting 
from 1 (there are no duplicate numbers), which is also the dangerous level of the island. 
You can also see curves between the islands on the map and those are the symbol of bridges.     
After you read the map, Hashira commanded you to take care of a herd of capybaras 
by guiding them to eat grass. They are initially taken to the island with a dangerous level 
1 by Hashira.
    You should obey the following rules made by Hashira.
    First, the capybaras are smart but lazy, if there is no grass on the next island, they 
won't go there no matter how you beg them. If they can't reach an island with grass 
by passing only one bridge, they sleep. That means you can't move them anymore. 
You should guide the capybaras to visit the islands as many as you can. The more they eat, 
    the cuter they will be.
    Second, the capybaras are like grass mowers, they will eat all the grass on the island.
You can't hurry them to the next island when they can still find some grass on the current 
island. 
    Third, when you want to guide the capybaras to the next island, you should always 
choose the safest one which is still full of grass. For example, if your current island is 
connected with three islands with dangerous levels 8, 9, and 5 respectively, assuming the 
level 5 island runs out of grass, you should choose the first one (the island with 
dangerous level 8) as the next island.
    Fourth, all the islands on the map are full of grass when you receive the map.
    Fifth, you can assume that the amounts of grass on all the islands are the same.
    "For the glory of capybara! Now, tell me about your plan." said Hashira. By knowing the 
previous information, can you figure out the best plan to fit Hashira's demand?
```       

## Input

* The first line contains two integers N, representing the number of islands, and M, which indicating the number of bridges.
* Each line of the following M lines contains two space-separated integers u and v, indicating that there is a bridge between u and v. (That is, the capybaras can go to u from v and go to v from u by passing the bridge.)
* $1\leq N \leq 30$
* $0\leq M \leq \frac{N(N-1)}{2}$
* $1\leq u, v \leq N$, and $u \neq v$

## Output
* The output should be a sequence of integer which indicate the order of islands visited by capybaras. Notice that the number of island also represents island's dangerous level. The sequence should include the initial point and seperated by a whitespace.
* Notice that you should guide the capybaras to eat grass as much as possible, and you also need to consider the safety of capybara.

## Hint
* If you have no idea about solving this problem, the depth-first search method may help you figure it out.
* You don't need to think about the time consuming problem. You only need to consider path.
---


### Sample Input 1
5 5
1 3
1 2
1 4
2 4
4 5



### Sample Output 1
1 2 4 5


---

### Sample Input 2
6 7
2 3
2 4
2 5
1 4
1 3
1 2
5 6

### Sample Output 2
1 2 3


---



### Submit Rule and Judge Method
* Your code should be written in Python 2.7 or Python 3.8, and should be in the same format as the following sample code.
```python=
class Solution:
    def __init__(self):
        pass
    #Feel free to define your own member function
    
    def solve(self):
        pass

if __name__ == '__main__':
    ans = Solution()
    ans.solve()
```
* Your code will be judged  by the following two commands. You can check your answer through these commands.
```
python2 r12345678_hw0.py < testdata.in
python3 r12345678_hw0.py < testdata.in
```
* If one of your output done by the above commands is correct, you will get the grade of this testcase.
* Your code should named as <student_ID>_hw0.py. Notice that the file name should be in lower case. For example, r12345678_hw0.py is correct, and it should not be R12345678_hw0.py. Please create a <student_ID>_hw0.zip to pack your code. 
```
Filename: r12345678_hw0.zip
			- r12345678_hw0.py
```

* You should not import the module which is not a build-in content in Python. 
* TA will import your code and check if the output is correct. The following code is

```python=
import sys
if __name__ == "__main__":
    student_id = sys.argv[1] #This will be passed by the driver process of TA.    
    student_file = __import__(student_id + "_hw0") #Import your code.
    ans_obj = student_file.Solution()
    ans_obj.solve() #The output to stdout will be received by the driver process.
```


### Additional Information
* HW0 is the only one assignment in this course that allowed to be complete with Python 2 or Python 3. The propose is to make it easier to the students who are still not familiar with coding. 
* As stated above, the other assignments could be done by Python 2 only, the details will be announced in the future.




### May the Capybaras Be with You.

![](https://i.imgur.com/TuQEMXA.jpg)

