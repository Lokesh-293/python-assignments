for num in range(100,200):
    digits = 0
    power = 0
    temp = num
    while temp>0:
     digits +=1
     temp //=10
    temp = num
    while temp >0:
        digit = temp % 10
        power += digit ** digits
        temp //= 10
    if power == num:
        print(num)