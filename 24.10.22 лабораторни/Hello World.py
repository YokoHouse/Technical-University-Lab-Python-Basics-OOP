from logging import StringTemplateStyle
import numbers
import string


numbers = [1, 2, 3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

second_name = ["Ivanov", "Georgiev", "Manolova"]

print(numbers)
print(strings)
print(names)
print("The second name on the name list is %s" % second_name)