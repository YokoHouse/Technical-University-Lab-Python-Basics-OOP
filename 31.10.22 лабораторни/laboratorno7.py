import string


for number in range(1,20):
    if number==5:
        continue
    if number==11:
        break
    print(number)


for letter in range(ord('a'), ord('z')):
    if letter=='a':
        continue
    if letter=='y':
        break
    print(chr(letter))