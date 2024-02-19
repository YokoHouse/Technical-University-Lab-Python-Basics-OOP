my_file=open("test1.txt","r")
print(my_file.read())

my_file.close()
my_file=open("test1.txt","r")
print(my_file.readline())
print(my_file.readline(2))