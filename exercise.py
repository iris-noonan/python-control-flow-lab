# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    vowels = ["a", "e", "i", "o", "u"]
    print(f'Please enter a letter.')
    letter = input().lower()
    is_vowel = letter in vowels
    is_alpha = letter.isalpha()
    if is_alpha != True:
        print("The letter " + letter + " is not in the alphabet.")
        return
    if is_vowel:
        print("The letter " + letter + " is a vowel.")
    else:
        print("The letter " + letter + " is a consonant.")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    print(f'Please enter your age: ')
    age = input()
    age_number = int(age)
    if age_number < 0:
        print("Your age is negative")
        return
    can_vote = True if age_number >= 18 else False
    if can_vote:
        print("You can vote")
    else:
        print("You can not vote")
# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    print(f'Input a dog\'s age: ')
    age = input()
    age_number = int(age)
    if age_number < 0:
        print("Your age is negative")
        return
    if age_number <= 2:
      dogs_age = age_number * 10
    else:
      older_years = age_number - 2
      dogs_age = 20 + (older_years * 7)
    print("The dog's age in dog years is " + str(dogs_age))

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    print('Is the weather cold (yes/no)')
    cold = input()
    if cold == "yes":
      is_cold = True
    elif cold == "no":
      is_cold = False
    print('Is it raining (yes/no)')
    rain = input()
    if rain == "yes":
      is_rain = True
    elif rain == "no":
      is_rain = False
    if (is_cold and is_rain):
      print("Wear a waterproof coat.")
    elif (is_cold and not is_rain):
      print("Wear a warm coat.")
    elif (not is_cold and is_rain):
      print("Carry an umbrella.")
    elif (not is_cold and not is_rain):
      print("Wear light clothing.")

# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Nov", "Dec"]
    print("Enter the month of the year (Jan - Dec):")
    month = input()
    is_a_month = month in months
    if is_a_month != True:
        print(month + " is not a valid month.")
        return
    print("Enter the month of the year (Jan - Dec):")
    day = input()
    day_is_numeric = day.isnumeric()
    if day_is_numeric != True:
        print(day + " is not a numeral.")
        return
    day = int(day)
    day_calendar_day = day > 0 and day <= 31
    day = str(day)
    if day_calendar_day != True:
        print(day + " is not a valid day of a month.")
        return
    day = int(day)
    if (month == "Dec" and day >= 21):
      season = "Winter"
    elif (month == "Jan"):
      season = "Winter"
    elif (month == "Feb"):
      season = "Winter"
    elif (month == "Mar" and day <= 19):
      season = "Winter"
    elif (month == "Mar" and day >= 20):
      season = "Spring"
    elif (month == "Apr"):
      season = "Spring"
    elif (month == "May"):
      season = "Spring"
    elif (month == "Jun" and day <= 20):
      season = "Spring"
    elif (month == "Jun" and day >= 21):
      season = "Summer"
    elif (month == "Jul"):
      season = "Summer"
    elif (month == "Aug"):
      season = "Summer"
    elif (month == "Sep" and day <= 20):
      season = "Summer"
    elif (month == "Sep" and day >= 21):
      season = "Fall"
    elif (month == "Oct"):
      season = "Fall"
    elif (month == "Nov"):
      season = "Fall"
    elif (month == "Dec" and day <= 20):
      season = "Fall"
    day = str(day)
    print(month + " " + day + " is in " + season + ".")

# Call the function
determine_season()
