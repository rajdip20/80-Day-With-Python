
# 1. Create a greeting for your program.
# 2. if the bill was ₹150.00, split between 5 pepple, with 12% tip. make it for 10,12,15 percent of tip.
# 3. Each person should pay (150.00/5)*1.12 = 33.6
# 4. Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? ₹"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))

bill_with_tip = percent/100 * bill + bill
bill_per_person = bill_with_tip/person
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ₹{final_amount}")
