# from replit import clear
# from art import logo

# print(logo)

# players = {}
# name = input("What is your name?: ")
# players[name] = int(input("What's your Bid?: $"))
# is_ok = True

# while is_ok:
#     condition = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#     if condition == "yes":
#         clear()
#         name = input("What is your name?: ")
#         players[name] = int(input("What's your Bid?: $"))
#     elif condition == "no":
#         clear()
#         max_bider = max(players, key=players.get)
#         max_number = players[max_bider]
#         print(f"The winner is {max_bider} with a bid of ${max_number}.")
#         is_ok = False

#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####OR#####

from replit import clear
from art import logo

print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
