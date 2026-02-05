
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print(f"The number of vowels in '{word}' is {count}.")
