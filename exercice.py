#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    mon_nombre = float(input('Veuillez entrer un nombre: '))
    if mon_nombre < 0:
        mon_nombre = -mon_nombre
    # return abs(mon_nombre)
    return mon_nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    resultat = []
    for prefixe in prefixes:
        nom = prefixe + suffixe
        resultat.append(nom)
    return resultat




def prime_integer_summation() -> int:
     nombrePremier = 0
    nombre = 2
    somme = 0
    while (nombrePremier < 100):
        estPremier = True
        for i in range(1,nombre+1):
            if (nombre % i == 0 and i != 1 and i!= nombre):
                estPremier = False
                break
        if estPremier:
            nombrePremier += 1
            somme += nombre
        nombre += 1
    return somme 


def factorial(number: int) -> int:
    result = 1
    if number != 0:
        for i in range (number):
            result *= (number - i)
        return result  
    
    #for i in range (1,number):
     #   number *= (number-i)
    #return number
    #ne fontionne pas avec 0
 
def use_continue() -> None:
    for chiffre in range (1, 11):
        if chiffre == 5:
            continue
        print(chiffre)
        
       # for chiffre in range (1, 11):
        #if chiffre == 5:
         #   pass
        #else :
         #   print (chiffre 
    
def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
