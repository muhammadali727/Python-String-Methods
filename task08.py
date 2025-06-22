text = input("enter text: ")
word = input("enter the starting word: ")
if text.startswith(word):
    print(True)
else:
    print(False)