# Personal Information Manager
# Created by [Priya Kumari]
# Internship Task 1 - Python Basics Project

# Welcome message
print("=" * 50)
print("        PERSONAL INFORMATION MANAGER")
print("=" * 50)
print()

# -------------------------------
# Store Static Information
# -------------------------------

name = "Your Name"          # String: stores your full name
age = 20                    # Integer: stores your age in years
city = "Your City"          # String: stores your city
hobby = "Your Hobby"        # String: stores your hobby

# -------------------------------
# Get User Input
# -------------------------------

print("Please tell me about yourself:")
print("-" * 40)

# Ask for favorite food with validation
favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ").strip()

# Ask for favorite color with validation
favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ").strip()

# Optional: Format user input nicely
favorite_food = favorite_food.title()
favorite_color = favorite_color.title()

# -------------------------------
# Calculations
# -------------------------------

age_in_months = age * 12  # Convert age from years to months

# -------------------------------
# Display Information
# -------------------------------

print()
print("=" * 50)
print("              YOUR INFORMATION")
print("=" * 50)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print("-" * 50)
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye message
print("=" * 50)
print("Thank you for using the Personal Information Manager!")
print("Goodbye! 👋")
print("=" * 50)
