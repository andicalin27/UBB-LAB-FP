def nrprim(x):
    i=2
    ok=1
    while i<x/2:
        if x%i==0:
            ok=0
        i+=1
    if ok==1:
        return True
    else:
        return False


def SecPrim(sec):
    ct=0
    ctmax=0
    imax=0
    for i in range(0,n-1):
        if nrprim(sec[i]+sec[i+1])==True:
            ct+=1
        else:
            ct=0
        if ctmax<ct:
           ctmax=ct
           imax=i+1

    if ctmax>0:
        return "Die langste Teilfolge ist "+str(sec[imax-ctmax:imax+1])+" Lange:"+str(ctmax+1)
    else:
        return "Es gibt keine primzahlige Summe"


sir=[]
n=int(input("Wie viele Zahlen willst du hinzufugen?"))
for i in range(0,n):
    nr=int(input())
    sir.append(nr)

print(SecPrim(sir))


