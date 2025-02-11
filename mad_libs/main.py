
# Welcome message
print("Welcome to Mad Libs! Let's create a fun story.")
print("Please enter the following words when prompted:\n")

# Collect user inputs
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb (base form, e.g., 'run'): ")
animal = input("Enter an animal: ")
exclamation = input("Enter an exclamation (e.g., 'Wow', 'Oh no'): ").capitalize()
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb (base form): ")
adverb = input("Enter an adverb (e.g., 'happily', 'quickly'): ")

# Story template
story = f"""
One {adjective1} morning, a {noun1} decided to {verb1} to the park. 
On the way, it encountered a {animal} wearing a {adjective2} hat. 
"{exclamation}!" shouted the {animal}. "You're {verb1}ing all wrong!"

The {noun1} replied, "I'm just trying to {verb2} like usual!" 
Suddenly, they both heard a loud {noun2} noise from above. 
They looked up and saw a {adverb} dancing cloud!

They spent the rest of the day {verb2}ing together, 
proving that even a {noun1} and {animal} can be friends.
"""

# Display the completed story
print("\nYour Mad Lib Story:\n")
print(story)