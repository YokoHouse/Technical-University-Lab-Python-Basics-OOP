fruits=["Orange\n","Banana\n","Apple\n"]
new_file=open("newfile.txt", mode="a+", encoding="utf-8")
new_file.writelines(fruits)
for line in new_file:
    print(line)
new_file.close()