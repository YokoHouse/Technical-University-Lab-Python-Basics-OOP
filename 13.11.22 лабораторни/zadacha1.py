figure=int(input())

area=0

def fig1():
    global area
    a=int(input())
    area = a*a
    return area

def fig2():
    global area
    a=int(input())
    b=int(input())
    area= a*b
    return area

def fig3():
    global area
    a=int(input())
    b=int(input())
    area=(a*b)/2
    return area



if figure==1:
    fig1()
    print(area)
elif figure==2:
    fig2()
    print(area)
elif figure==3:
    fig3()
    print(area)

print(area)
