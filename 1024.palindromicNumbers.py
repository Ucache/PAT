(init, maxstep) = (x for x in raw_input().split())

def p(init,maxstep):
    for i in range(int(maxstep)):
        if init == init[::-1]:
            print init
            print i
            return 0
        else:
            init = str(int(init)+int(init[::-1]))

    print init
    print maxstep

p(init,maxstep)
