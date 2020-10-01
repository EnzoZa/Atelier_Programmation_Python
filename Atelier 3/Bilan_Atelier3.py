# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 08:38:57 2020
Fonction de l'atelier bilan
Version 2
@author: Enzo Zampaglione
"""


###############################################################################
#                                                                             #
#                               Fonctions Générales                           #
#                                                                             #
###############################################################################

def check_int(phrase:str)->int:
    """
    Fonction qui demande à l'utilisateur de rentrer un int.
    
    Fonction utilisée de manière globale qui prend en entrée un string,
     qui a pour but de questionner l'utilisateur dans
    la console et renvoie un int.
    La fonction demandera à l'utilisateur d'effectuer une entrée clavier tant
    que celle-ci ne sera pas valide.
    
    Il n'existe pas de constantes locales dans cette fonction.
    """
    ## Début du script ##
    
    result:bool = False
    user_input = input(phrase)
    print("\n")
    while(not result) : 
        try:
            #Si les 2 lignes suivantes sont exécutées sans erreur, on 
            # a une entrée valide.
            val = int(user_input)
            result = True
        except ValueError:
            #Si on a une erreur de valeur, on demande à l'utilisateur d'entrer
            #à nouveau une valeur.
            user_input = input(phrase)
    return val

###############################################################################
#                                                                             #
#                               Exercice 1                                    #
#                                                                             #
###############################################################################
    

def fill_list(b_inf:int, b_sup:int, max_len:int)->list:
    """fill in a list of elements included in the limits (b_inf/b_sup) entered in parameters
    Keyword argument:
    b -- list of int enter by the user
    return a list (b)
    """
    b:list = []
    i:int = 0
    check:bool = True
    while(i<max_len and check):
        val = check_int("Saisir un élément entre {} et {}, il reste {} place : " .format(b_inf, b_sup, max_len-len(b)))
        if(b_inf<=val<=b_sup): #je rajoute la condition (and val.isdigit()) si je n'utilise pas ma fonction check_int
            b.append(val)
        else:
            check = False
        i+=1
    return b

def test_fill_list(fill_list:callable)->None:
    """Test function fill_list
    Keyword argument :
    fill_list -- function
    return None
    """
    print("Test entre 0 et 10 avec une taille de 5")
    print(fill_list(0,10,5))
    print("Test entre -10 et 10 avec une taille de 7")
    print(fill_list(-10,10,7))
    print("Test entre -10 et 0 avec une taille de 5")
    print(fill_list(-10,0,5))
    print("Test entre 100 et 105 avec une taille de 5")
    print(fill_list(100,105,5))
    print("Test entre 0 et 1000 avec une taille de 15")
    print(fill_list(0,1000,15))
    print("Test entre -100 et -50 avec une taille de 5")
    print(fill_list(-100,-50,5))