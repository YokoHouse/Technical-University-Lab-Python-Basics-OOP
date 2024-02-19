n = int(input('брой числа'))
maxnum = 0

for i in range(1,n,+1):
    num = int(input('Въведи число'))
    if num >= maxnum:
        maxnum=num
        print('Най-голямото число' + maxnum)