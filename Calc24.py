def get24(*tuples):
    keynum = list(range(0,4))
    black = list()
    for a in keynum:
        black.append(a)
        for b in keynum:
            if(black.count(b)):
                continue
            black.append(b)
            for c in keynum:
                if(black.count(c)):
                    continue
                black.append(c)
                for d in keynum:
                    if(black.count(d)):
                        continue
                    is24(tuples[a],tuples[b],tuples[c],tuples[d])
                black.remove(c)
            black.remove(b)
        black.remove(a)

def is24(a,b,c,d):
    tools = ['+','-','*','/','--','//']
    temp = 0
    for u1 in tools:
        temp1 = easycalc(a,b,u1)
        for u2 in tools:
            temp2 = easycalc(temp1,c,u2)
            for u3 in tools:
                temp3 = easycalc(temp2,d,u3)
                if(temp3 == 24):
                    print(a,u1,b,u2,c,u3,d,'=',temp3)


def easycalc(a,b,flag):
    if(flag == "+"):
        return a + b
    elif(flag == '-'):
        return a - b
    elif(flag == '*'):
        return a * b
    elif(flag == '/'):
        if(b == 0):
            return 9999
        return a / b
    elif(flag == '//'):
        if(a == 0):
            return 9999
        return b / a
    elif(flag == '--'):
        return b - a

get24(5,-5,10,2)