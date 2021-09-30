string1 = input("Enter a Word : ")
chara = input("Enter a letter : ")

count = 0

for i in range(len(string1)):
  if chara == string1[i]:
    count += 1
print(f"\'{chara}\' appears {count} time/s")