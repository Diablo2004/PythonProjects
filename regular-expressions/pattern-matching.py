# re.match() - Matches from the beginning of the string

import re

pattern = r"Python" # Using raw strings (r"...") tells Python to ignore escape sequences, making regex patterns cleaner and avoiding errors.
text1 = "Python is great!"
text2 = "I love Python!"

print(re.match(pattern, text1))
print(re.match(pattern, text2))

print("------")

pattern = r"^Hello"  # Matches 'Hello' at the start of a string
text1 = "Hello, Python!"
text2 = "Hi, Hello!"

print(bool(re.match(pattern, text1)))
print(bool(re.match(pattern, text2)))

print("---------")

# Validating a phone number

pattern = r"^\+91-\d{10}$"  # +91- followed by exactly 10 digits
text1 = "+91-9876543210"
text2 = "9876543210"

print(bool(re.match(pattern, text1)))
print(bool(re.match(pattern, text2)))

# ^ → Start of string
# \+91- → Matches "+91-" literally
# \d{10} → Ensures exactly 10 digits
# $ → End of string

print("--------")

pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
password1 = "Secure@123"
password2 = "weakpass"

print(bool(re.match(pattern, password1)))
print(bool(re.match(pattern, password2)))

# (?=.*[A-Z]) → At least one uppercase letter
# (?=.*\d) → At least one digit
# (?=.*[@$!%*?&]) → At least one special character
# [A-Za-z\d@$!%*?&]{8,} → Length of at least 8 characters

print("---------")

# re.search() - Searches the entire string for a match

pattern = r"Python"
text1 = "Python is great!"
text2 = "I love Python!"

print(re.search(pattern, text1))
print(re.search(pattern, text2))

print("--------")

pattern = r"Python!$"  # Matches 'Python!' at the end of a string
text3 = "I love Python!"
text4 = "Python is great!"

print(bool(re.search(pattern, text3)))
print(bool(re.search(pattern, text4)))

print("--------")

pattern = r"Python"
text = "I love Python programming."

# re.match() checks only at the beginning
print(re.match(pattern, text))

# re.search() checks anywhere in the text
print(re.search(pattern, text))



