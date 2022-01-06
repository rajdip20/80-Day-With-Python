'''
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
Thus, the first even number would be 2 and the last one is 100:
i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
'''

#Write your code below this row 👇

add = 0

for i in range(2, 101):
    if(i % 2 == 0):
        add = add + i
print(add)
