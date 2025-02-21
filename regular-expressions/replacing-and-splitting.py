import re

# re.sub() - Replaces all occurrences of a pattern

pattern = r"\d+"  # Matches digits
text = "I have 3 cats and 5 dogs."

new_text = re.sub(pattern, "X", text)
print(new_text)

print("---------")

#  Mask Credit Card Numbers (Keep Only Last 4 Digits)

pattern = r"\d{12}(\d{4})"  # Captures last 4 digits
text = "My card number is 1234567812345678."

masked_text = re.sub(pattern, "************\\1", text)
print(masked_text)

# \d{12} → Matches the first 12 digits
# (\d{4}) → Captures the last 4 digits
# re.sub() replaces first 12 digits with "************" but keeps the last 4

print("---------------")

# Remove extra spaces between texts

pattern = r"\s+"
text = "This   is   a    test   string."

clean_text = re.sub(pattern, " ", text)
print(clean_text)  # Output: "This is a test string."

print("-------------")

# Remove all vowels from a string

text = "Hello, this is a test string."
pattern = r"[aeiouAEIOU]"

result = re.sub(pattern, "", text)
print(result)

print("--------")

# re.split() - Splits the string based on a pattern

pattern = r"\s+"  # Splits by one or more spaces
text = "Python   is   fun!"

words = re.split(pattern, text)
print(words)

print("--------")

# Split by comma or semicolon

pattern = r",|;"
text = "apple,banana;cherry,grape;orange"

words = re.split(pattern, text)
print(words)

print("------------")

# Split a sentence at punctuation

pattern = r"[.!?]"
text = "Hello! How are you? I am fine. Thank you."

sentences = re.split(pattern, text)
print(sentences)  # Output: ['Hello', ' How are you', ' I am fine', ' Thank you', '']

