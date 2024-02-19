n = int(input())

d=dict()
l=[]

for i in range(1, n+1):
    l.append(i)

for x in range(1, n+1):
    d[x]= l.pop(len(l)-1)

print(d)
