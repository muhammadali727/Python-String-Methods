text = input("Enter the text: ")
length = int(input("Enter the total length: "))
fill = input("Enter fill character: ")

print(text.ljust(length, fill))