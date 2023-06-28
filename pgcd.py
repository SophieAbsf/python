def pgcd(a,b):
    if a<b:
        c=a
        a=b
        b=c
    elif a==0:
        return b
    r=a%b
    while(r!=0):
        a=b
        b=r
        r=a%b
    return b

a=int(input("Entrez le premier nombre.\n"))
b=int(input("Entrez le deuxième nombre.\n"))
print(f"Le PGCD de({a},{b}) est: {pgcd(a,b)}")