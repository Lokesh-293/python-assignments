num=int(input("enter number"))

sum = 0
length = len(str(num))
temp = num
while temp > 0:
    digits = temp % 10
    sum = sum + digits ** length
    temp = temp // 10
if sum == num :
    print("armstrong number")
else:
    print("not a armstrong number")        