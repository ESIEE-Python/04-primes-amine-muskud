"""Importation de la fonction racine carré"""
from math import sqrt

#### Fonction secondaire


def isprime(p:int):
    """
    Vérifie si un nombre p est premier 
    en vérifiant si il possède un diviseur x verifiant 1<x<Sqrt(p)
    Si p est égale à 0 ou 1, la fonction retourne directement FALSE
    """
    x=True
    if p==0:
        x=False
    if p==1:
        x=False
    for i in range(2, int(sqrt(p))+1 ):
        if p%i==0 and i!=p:
            x=False
    return x

#### Fonction principale


def main():
    """
    Vérfie le fonctionnement de la fonction ISPRIME en donnant tous les nombres premiers de 1 à 100
    """
    # vos appels à la fonction secondaire ici
    for n in range(10000):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
