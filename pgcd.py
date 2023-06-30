def pgcd(num1,num2):
    """
    La fonction pgcd permet de déterminer le pgcd de deux nombres entrés en argument.
    """
    
    # Premier cas de figure: num1< num2, si a est inférieur à b alors on procède une permutation des deux valeurs.
    
    if num1<num2:
        tmp=num1
        num1=num2
        num1=tmp
        
    # Deuxième cas de figure: num1 = 0, si a est égale à 0 alors la fonction renvoie la valeur num2 comme celle du pgcd.

    elif num1==0:
        return num2
    # rest est le reste de la division de num1 par num2.
    rest=num1%num2

    # Troisième cas de figure: num1 > num2, si num1 est supérieur à num2 tant que le reste est non nulle on affecte à num1 la valeur de num2 et à num2 celle de rest.
    while(rest!=0):
        mum1=num2
        num1=rest
        rest=num1%num2
        
    # Si le reste est nulle alors la fonction retourne num2 comme la valeur du pgcd.
    return num2
    
# Juste un code pour tester la fonction.

num1=int(input("Entrez le premier nombre.\n"))
num2=int(input("Entrez le deuxième nombre.\n"))
print(f"Le PGCD de({num1},{num2}) est: {pgcd(num1,num2)}")
