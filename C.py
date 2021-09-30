str1 = input("Enter a word/sentence : ")
str2 = "" # an empty string

for i in str1:
    str2 = i + str2
if str1 == str2:
    print(f"{str2} is equal to {str1}/nHence the string is Palindrome :)")
else:
    print(f"{str2} is not equal to {str1}\nThe string is not a Plaindrome :(")
