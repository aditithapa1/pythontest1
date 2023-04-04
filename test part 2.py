# Define global variables for the three primary colors
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

# Ask user for input
color1 = input("Enter the first primary color: ").lower()
color2 = input("Enter the second primary color: ").lower()

# Check for invalid color1 input
if color1 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color1")

# Check for invalid color2 input
elif color2 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color2")

# Check for same color inputs
elif color1 == color2:
    print("Error: The two colors you entered are same")

# All inputs are valid, perform color mixing
else:
    if color1 == RED:
        if color2 == BLUE:
            print("PURPLE")
        elif color2 == YELLOW:
            print("ORANGE")
    elif color1 == BLUE:
        if color2 == RED:
            print("PURPLE")
        elif color2 == YELLOW:
            print("GREEN")
    elif color1 == YELLOW:
        if color2 == RED:
            print("ORANGE")
        elif color2 == BLUE:
            print("GREEN")

 
     
