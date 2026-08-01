n1 = int(input("Enter The Value Of N1 : "))
rev = 0
temp = n1
while n1 > 0:
    rem = n1 % 10
    rev = rev * 10 + rem
    n1 = n1 // 10
if temp == rev:
    print(f"{temp} Is Palindrom Number") 
else:
    print(f"{temp} Is Not Palindrom Number")