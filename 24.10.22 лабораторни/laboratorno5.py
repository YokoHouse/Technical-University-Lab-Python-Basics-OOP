import string


a=3.75
b=9.624
s='area'
print(' a=' + str(a) + ' b=' + str(b) + ' S=' + str(a*b))
print('a = %d, b=%d, %s=%d' %(a,b,s,a*b))
print('a = %d, b=%d, %s=%f' %(a,b,s,a*b))

# %d - цели числа
# %f - дробни числа
# %s - низ, стрингове
# %.3f - отстъп до 3 знака след точката 4.572