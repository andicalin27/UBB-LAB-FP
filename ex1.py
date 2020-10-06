
p=1
x=1

def produs(nr):
    global p
    if nr==0:

         return p
    else:
        p=p*nr


print("Insert numbers:")
while x!=0:
    produs(x)
    x=int(input())

print(produs(x))


