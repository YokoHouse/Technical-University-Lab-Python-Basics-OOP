num = 10
L=lambda n:n*2+1
print('nechetni chisla')
for k in range(num):
    print(L (k), end='')

print('\n Kvadrati na chislata')

for k in range(num):
    print((lambda x:x*x)(k+1), end='')