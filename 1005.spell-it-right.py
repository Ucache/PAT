import sys
sum = 0
dic = ["zero","one","two","three","four",
        "five","six","seven","eight","nine"]
result = []
lineint = int(sys.stdin.readline())
if lineint ==0:
    print "zero"
while lineint > 0:
    sum = sum + lineint%10
    lineint = lineint/10;
while sum>0:
    result.append(dic[sum%10])
    sum = sum / 10
for s in reversed(result):
    print s,

