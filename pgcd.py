def pgcd(a,b):
    """
    La fonction pgcd permet de déterminer le pgcd de deux nombres entrés en argument.
    """
    
    # Premier cas de figure: a < b, si a est inférieur à b alors on procède une permutation des deux valeurs.
    
    if a<b:
        c=a
        a=b
        b=c
        
    # Deuxième cas de figure: a = 0, si a est égale à 0 alors la fonction renvoie la valeur b comme celle du pgcd.

    elif a==0:
        return b
    # r est le reste de la division de a par b.
    r=a%b

    # Troisième cas de figure: a > b, si a est supérieur à b tant que le reste est non nulle on affecte à a la valeur de b et à b celle de r.
    while(r!=0):
        a=b
        b=r
        r=a%b
        
    # Si le reste est nulle alors la fonction retourne b comme la valeur du pgcd.
    return b
    
# Juste un code pour tester la fonction.

a=int(input("Entrez le premier nombre.\n"))
b=int(input("Entrez le deuxième nombre.\n"))
print(f"Le PGCD de({a},{b}) est: {pgcd(a,b)}")
