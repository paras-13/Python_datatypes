# Program to make the first letter of each word in the sentence capita using ASCII value.
# Code -->
Str = input("Enter a string")
lst = Str.split(" ")
Str = ""
for i in lst:
    alpha,remain= i[0],i[1:]
    Ascii = ord(alpha)
    if Ascii > 90:
        alpha = chr(Ascii-32)
        remain = alpha+remain+" "
        Str+=remain
    else:
        Str+= i+" "
print(Str)
