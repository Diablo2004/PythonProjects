
import re

# \d - Matches any digit (0-9)

pattern = r"\d+"  # Matches one or more digits
text = "My age is 25 and my house number is 1024."

matches = re.findall(pattern, text)
print(matches)  # Output: ['25', '1024']

print("---------")

pattern = r"\d+"  # Matches one or more digits
text = "Phone: 9876543210, Age: 25"

matches = re.findall(pattern, text)
print(matches)

print("---------")

# \w - Matches any alphanumeric character (A-Z, a-z, 0-9, _)

pattern = r"\w+"  # Matches words (letters, numbers, underscore)
text = "Hello, World_123!"

matches = re.findall(pattern, text)
print(matches)

print("------")

pattern = r"\w+"  # Matches words (letters, numbers, underscore)
text = "Hello, World_123!"

matches = re.findall(pattern, text)
print(matches)

print("------------")

# ^ - Matches the beginning of a string

pattern = r"^Hello"  # String must start with "Hello"
text1 = "Hello there!"
text2 = "Say Hello!"

print(bool(re.match(pattern, text1)))
print(bool(re.match(pattern, text2)))

print("----------")

# $ - Matches the end of a string

pattern = r"end$"  # String must end with "end"
text1 = "This is the end"
text2 = "End of the story."

print(bool(re.search(pattern, text1)))
print(bool(re.search(pattern, text2)))

# Checking for phone numbers in a given text

pattern = r"\b\d{3}-\d{3}-\d{4}\b"  # Matches phone numbers like 123-456-7890

text1 = "Call me at 123-456-7890."
text2 = "No phone number provided."

matches1 = re.findall(pattern, text1)
matches2 = re.findall(pattern, text2)

print(matches1)  # Output: ['123-456-7890']
print(matches2)  # Output: [] (empty list, since no phone number is found)

# Handling the case where no match is found
if not matches2:
    print("No phone numbers found in the text2.")

print("------------")


