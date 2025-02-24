# re.match() - Matches from the beginning of the string

import re

pattern = r"Python" # Using raw strings (r"...") tells Python to ignore escape sequences, making regex patterns cleaner and avoiding errors.
text1 = "Python is great!"
text2 = "I love Python!"

print(re.match(pattern, text1))
print(re.match(pattern, text2))

print("------")

# Matches later in the string but doesnt find a match

pattern = r"Python"
text1 = "Python is great!"  # 'Python' is at the beginning
text2 = "I love Python!"  # 'Python' is not at the beginning

print(re.match(pattern, text1))
print(re.match(pattern, text2))  # Output: None (No match because 'Python' isn't at the start)

print("----------")

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

# Edge cases

valid_number = "+91-9876543210"
missing_country_code = "9876543210"
extra_digit = "+91-98765432101"
wrong_separator = "+91 9876543210"
short_number = "+91-98765"
non_numeric = "+91-98765abcd0"

print(bool(re.match(pattern, valid_number)))         # True (Valid format)
print(bool(re.match(pattern, missing_country_code))) # False (Missing country code)
print(bool(re.match(pattern, extra_digit)))          # False (11 digits instead of 10)
print(bool(re.match(pattern, wrong_separator)))      # False (Space instead of '-')
print(bool(re.match(pattern, short_number)))         # False (Less than 10 digits)
print(bool(re.match(pattern, non_numeric)))         # False (Contains non-numeric characters)

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

print("----------------")

# Extract YouTube Video IDs from URLs

pattern = r"(?<=v=)[\w-]+"
urls = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://youtu.be/dQw4w9WgXcQ"]

for url in urls:
    match = re.search(pattern, url)
    if match:
        print(match.group())  # Output: dQw4w9WgXcQ

# (?<=v=) → Looks for v= (positive lookbehind)
# [\w-]+ → Matches the YouTube ID

print("--------")

pattern = r"Python"
text = "I love Python programming."

# re.match() checks only at the beginning
print(re.match(pattern, text))

# re.search() checks anywhere in the text
print(re.search(pattern, text))



