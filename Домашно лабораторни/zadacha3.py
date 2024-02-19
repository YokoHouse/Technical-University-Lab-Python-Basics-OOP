text = input()
l=[]
d = dict()
count = 0
pos = 0

for i in text:
    for x in range(len(text)):
        if text[x]==text[pos]:
            count+=1
        d[i]=count
        count=0
        pos+=1

print(d)
