
'''
Write a program that works out whether if a given year is a leap year. 
A normal year has 365 days, leap years have 366, with an extra day in February. 
The reason why we have leap years is really fascinating,
'''

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if(year % 4 == 0 or year % 400 == 0):
    print("Leap year.")
else:
    print("Not leap year.")
