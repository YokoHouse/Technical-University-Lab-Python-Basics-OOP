cars=["Audi\n","Bentley\n","Toyota\n"]
new_file=open("newfile1.txt",mode="a+", encoding="utf-8")
for car in cars:
    new_file.write(car)
    print("Tell the byte at which the file cursor is:",new_file.tell()) 
    new_file.seek(0)
for line in new_file:
    print(line)