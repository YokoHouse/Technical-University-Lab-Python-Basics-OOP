try:
    fileName = str(input())
    f = open(fileName)
    f.read()
    content = f.read()
    print(content)
except:
    print("Something went wrong when reading the file")
finally:
    f.close()