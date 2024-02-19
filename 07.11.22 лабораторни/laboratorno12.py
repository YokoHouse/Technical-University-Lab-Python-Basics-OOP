k=(1,3,5) #кортеж от 3 елемента
S=[1,3,5]
tup=tuple([1,3,5])
tup1=tuple('python')
tup2=tuple()
print(k[0])
print(k[1:2])

for S in k:
    print(S, end='')

k.count(3)
k.index(5)
len(k)

i=k+(2,4)

print(S in k)
print(k*3)