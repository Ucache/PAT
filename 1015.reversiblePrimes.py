import math
def isprime(a):
    if a ==2:
        return False
    if a==3:
        return True
    for i in range(2,a):
        if a%i ==0:
            return False
    return True
def trans(a,radix):
    total =[]
    sum =0
    while a:
        total.append(a%radix)
        a = a /radix
    for i in range(len(total)):
        sum = sum + total[i]*pow(radix,i)


lists = [int(x) for x in raw_input().split()]
while len(lists) == 2:
    if isprime(lists[0]) and isprime(trans(lists[0],lists[1])):
        print "Yes"
    else:
        print "No"
    lists = [int(x) for x in raw_input().split()]
