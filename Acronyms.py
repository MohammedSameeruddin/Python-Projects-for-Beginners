your_input = str(input("Enter a Phrase: "))
split_text = your_input.split()
a = " "
for i in split_text:
    a = a+str(i[0]).upper()
print(a)
