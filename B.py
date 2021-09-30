sentnc = input("Enter a Word/sentence : ")
ls = []
ls = sentnc.split(" ")
print(ls)
cou = 0

for i in range(len(ls)):    
    if cou < len(ls[i]):
      cou = len(ls[i])
      apbt = ls[i]
print(f"String with maximun length is = {apbt}")