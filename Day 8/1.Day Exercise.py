# Simple Function
# def greet():
#     print("Hello Rajdip")
#     print("How do you do Deba?")
#     print("Isn't the weather nice today?")

# greet()

# Function that allows for input
# 'name' is the parameter.
# 'Deba' is the argument.

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Deba")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Calling greet_with() with Positional Arguments
# greet_with("Debodip", "Nowhere")

# vs.
# greet_with("Nowhere", "Debodip")


# Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Rajdip")
