import re

pattern = r"([a-zA-Z]+) (\d+)"

text = "I have 3 cats and 2 dogs."

match = re.search(pattern, text)

if match:
    print(f"Match found: {match.group()}")
else:
    print("No match found.")
