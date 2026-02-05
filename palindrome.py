

text = input("Enter a word or phrase: ")

cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")
