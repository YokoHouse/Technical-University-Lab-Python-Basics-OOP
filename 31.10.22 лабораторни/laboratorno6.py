n=int(input())

sum=0
while True:
    sum+=n%10
    n=n//10
    if not n:
        break