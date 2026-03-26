VOWELS = ("a", "e", "i", "o", "u")

text = input("Input: ")

no_vowels = [char for char in text if char.lower() not in VOWELS]

print("".join(no_vowels))
