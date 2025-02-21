
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


