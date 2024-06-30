from journal.converters import convert
from journal.parsers import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")
if result < 1:
    print("kid is too smaall")
else:
    print("kid can use the slide.")
