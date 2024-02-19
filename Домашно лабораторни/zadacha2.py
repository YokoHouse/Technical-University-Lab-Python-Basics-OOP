n = int(input('Enter lenght of list:'))
l=[]
l1=[]
sumOfNumbers = 0
pos=1
for x in range(n):
    num = int(input('Input number:'))
    l.append(num)
    print("Before:")

for x in range (len(l)-1):
        sumOfNumbers=1[x]+1[x+1]
        l1.append(sumOfNumbers)

for x in range(len(l)-1):
    l.insert(pos, l1[x])
    pos=+2
    print(f'L after= {l}')
