text = input("Enter the text: ")
word = input("Enter the ending word: ")

if text.endswith(word):
    print(True)
else:
    print(False)