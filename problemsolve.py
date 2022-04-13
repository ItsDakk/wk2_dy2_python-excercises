# Think like a Programmer (book resource)
# Dive into algorithms (book resource)

# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints -(rules placed on you by the question)
    # Determine a Logical way to solve the problem - (build out your mental flow-chart)
        # Write each step out English - (don't write any code until you explain it in english)
        # Write each code step-by-step
        # Write each step out in Python-esse 
    # Invoke and Test Your Function

  # ex
    # given an integer age 
    # Write a function to return a string based on the age (line19)
    # if that age is old enough to smoke(18) return "Can Smoke, Can't Drink"
    # if that age is not old enough to smoke return "Can't do anything"
    # If that age is old enough to drink "Can Party"

def what_can_i_buy(age):
    """Takes an integer and returns a string that says what that age can do"""
    # Check the age and if it is in a certain range return it's respective string
    # If they are 21 and over return "Can Party"
    if age >= 21:
        return "Can Party"
    # If they are under 18 return "Can't do anything"
    elif age < 18:
        return "Can't Do Anything"
    # If they are between 18(inclusive) & 21(exclusive) then return "Can Some, Can't Drink" 
    elif 18<=age<21:
        return "Can Smoke - Can't Drink"
    
print(what_can_i_buy(19))
print(what_can_i_buy(18))
print(what_can_i_buy(17))

print(what_can_i_buy(23))

