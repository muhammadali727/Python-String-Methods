text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

if text1.lower() in text2.lower():
    print(True)
else:
    print(False)