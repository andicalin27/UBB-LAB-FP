
p=1
x=1

def produs(nr):
    global p
    if nr!=0:
        p=p*nr


print("Insert numbers:")
while x!=0:
    produs(x)
    x=int(input())

print(p)
ct=0
while p>0:
    if p%10==0:
        ct+=1
    p=p/10
print(ct)



