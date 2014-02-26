n = int(raw_input())
male=[]
female=[]
for i in range(n):
    (name,g,ids,grade) = (x for x in raw_input().split())
    grade = int(grade)
    if g =='M':
        male.append([grade,name,ids])
    else:
        female.append([grade,name,ids])
male.sort()
female.sort()
if len(male)>0 and len(female)>0:
    print female[len(female)-1][1],female[len(female)-1][2]
    print male[0][1],male[0][2]
    print female[len(female)-1][0] -male[0][0] 
else:
    if len(female) != 0:
        print female[len(female)-1][1],female[len(female)-1][2]
    else:
        print "Absent"
    if len(male) != 0:
        print male[0][1],male[0][2]
    else:
        print "Absent"
    print "NA"
        

