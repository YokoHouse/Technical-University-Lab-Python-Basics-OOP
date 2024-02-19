try:
    x = int(input())
    if x < 0:
        raise Exception("Invalid number")
    else:
        print(x**2)
except:
    print("something went wrong")
finally:
    print("goodbye")
    
    