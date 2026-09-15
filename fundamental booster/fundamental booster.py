print("Welcome to the Interactive Personal Data Collector!")

print("\nPlease enter your personal information:")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favorite_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print("Name:", name, "(Type:", type(name), ", Memory Address:", id(name), ")")
print("Age:", age, "(Type:", type(age), ", Memory Address:", id(age), ")")
print("Height:", height, "(Type:", type(height), ", Memory Address:", id(height), ")")
print("Favourite Number:", favorite_number,
      "(Type:", type(favorite_number), ", Memory Address:", id(favorite_number), ")")

birth_year = 2026-age

print("\nYour birth year is approximately:",
      birth_year, "(based on your age of", age, ")")


print("\nThank you for using the Personal Data Collector. Goodbye!")