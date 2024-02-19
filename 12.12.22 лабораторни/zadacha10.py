import pickle
tup1=[22,44,66]
p1 = pickle.dumps (tup1)
print(p1)
t2 = pickle.loads (p1)
print (t2)

with open ("a.txt", 'wb') as f:
    pickle.dump (tup1,f)

with open ("a.txt", 'rb') as f:
    t3 = pickle.load (f)

print (t3)