# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:39:54 2020
Fonction de l'atelier 2
Version 1
@author: Enzo Zampaglione, Vincent Bonneymare
"""
from math import sqrt
import datetime

###############################################################################
#                                                                             #
#                       Fonctions Communes                                    #
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def check_float(phrase:str)->float:
    """
    Fonction qui demande à l'utilisateur de rentrer un float.
    
    Fonction utilisée de manière globale qui prend en entrée un string,
    qui a pour but de questionner l'utilisateur dans
    la console et renvoie un float.
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
            val = float(user_input)
            result = True
        except ValueError:
            user_input = input(phrase)
    return val

###############################################################################
#                                                                             #
#              EXERCICE 1 : Fonction chaîne de caractère : Calcul d'IMC       #
#                                                                             #      
###############################################################################  
    
def message_imc()->str:
    """
    IMC_DESC donne les descriptions des IMC existants
    IMC_VALUE fournit les seuils auquels l'IMC passe dans
        la catégorie supérieure
    Fonction associant une catégorie à un IMC entrer au clavier
    """
    
    IMC_DESC = ["dénutrition ou famine", "maigreur", "corpulence normale", 
                "surpoids", "obésité modérée", "obésité sévère", "obésité morbide"]
    IMC_VALUE = [16.5,18.5,25,30,35,40]
    ind_imc = check_float("Quelle est votre IMC : ")
    isFound=False
    i=0
    while(not isFound):
        if(ind_imc < IMC_VALUE[i]):
            isFound = True
        elif(i==(len(IMC_VALUE)-1)):
            isFound=True
            i+=1
        else :
            i += 1
    return("Vous êtes en " + IMC_DESC[i])

def test_message_imc()->None:
    """ 
    Fonction de test appelant de manière succéssive la fonction message_imc 
    """
    
    j = check_int("Combien de test voulez-vous effectuez : ")
    for i in range(j):
        print(message_imc())

#test_message_imc()

###############################################################################
#                                                                             #
#              EXERCICE 2 : Fonction booléenne : Année bissextile             #
#                                                                             #      
###############################################################################    
        
def est_bissextile(annee:int)->bool:
    """
    Fonction vérifiant si une année est bissextile 
    (elle l'est si elle est divisible par 4 et non par 100)
    """
    result = False
    if(annee%4==0 and annee%100!=0):
        result = True
    return result

def test_est_bissextile()->None:
    """ 
    Fonction de test appelant de manière succéssive la fonction est_bissextile 
    """
    j = check_int("Combien de test voulez-vous effectuez : ")
    annee = 0
    for i in range(j):
        annee = check_int("Quelle année voulez-vous testez : ")
        print(str(est_bissextile(annee)))
        
#test_est_bissextile()

###############################################################################
#                                                                             #
#     EXERCICE 3 : Résolution d'une équation du second degré ax²+bx+c         #
#                                                                             #      
###############################################################################   
        
def discriminant(a:float,b:float,c:float)->float:
    disc = -1
    if(a!=0):
        disc = (b*b) - (4*a*c)
    else:
        print("a doit-être non nul")
    return disc

def racine_unique(a:float,b:float)->float:
    if(a!=0):
        racine = (-b/(2*a))
    else:
        print("a doit-être non nul")
    return racine

def racine_double(a:float,b:float,delta:float,num:int)->float:
    racine = 0
    if(a!=0):
        if(num==1):
            racine = (((-b)+sqrt(delta))/(2*a))
        elif(num==2):
            racine = (((-b)-sqrt(delta))/(2*a))
        else: print("Il n'y a que 2 racines")
    else:
        print("a doit-être non nul")
    return racine

def str_equation(a:float, b:float, c:float)->str:
    char=""
    
    if(a!=0):
        char += (str(a) + "x²")
        if(b!=0 or c!=0):
            char+=" + "
    if(b!=0):
        char += (str(b) + "x")
        if(c!=0):
            char+=" + "
    if(c!=0):
        char += str(c)
    return char

def solution_equation(a:float,b:float,c:float)->str:
    char = (str_equation(a,b,c) + " = 0 \n")
    disc = discriminant(a,b,c)
    if(disc==0):
        char += ("Racine unique x= " + str(racine_unique(a,b)))
    elif(disc>0):
        char += ("Deux racines \n x1= " + str(racine_double(a,b,disc,1)) + "\n et x2= " + str(racine_double(a,b,disc,2)))
    else :
        char += "In n'y a pas de racines réelles"
    return char

def equation(a:float,b:float,c:float)->None:
    print(solution_equation(a,b,c))

def test_equation()->None:
    """ 
    Fonction de test appelant de manière succéssive la fonction equation 
    """
    a = 0
    b = 0
    c = 0
    j = check_int("Combien de test voulez-vous effectuez : ")

    for i in range(j):
        a = check_float("a = ")
        b = check_float("b = ")
        c = check_float("c = ")
        equation(a,b,c)
    
    
###############################################################################
#                                                                             #
#                       EXERCICE 4 : Calculs de date                          #
#                                                                             #      
###############################################################################   

        
def date_est_valide(jour:int,mois:int,annee:int)->bool:
    result = False
    try:
        datetime.date(annee,mois,jour) #datetime.date ne peux pas crée de fausse date
        result = True
    except ValueError:
        result = False
    return result

def saisie_date_naissance()->datetime.date:
    check = False
    while(not check):
        jour = check_int("Quel jour êtes vous né : ")
        mois = check_int("Quel mois êtes vous né : ")
        annee = check_int("Quel année êtes vous né : ")
        if(date_est_valide(jour,mois,annee)):
            d = datetime.date(annee,mois,jour)
            check = True
        else:
            print("\n Date invalide \n")
    return d#.strftime("%d %b %Y")

def age(date_naissance:datetime.date)->int:
    age = 0
    d = datetime.date.today()
    #Age = d.year - date_naissance.year - ((d.month, date_naissance.month) < (d.day, date_naissance.day))
    year = d.year - date_naissance.year
    month = d.month - date_naissance.month
    day = d.day - date_naissance.day
    #datetime.date.today() < date_naissance
    if(month>0 or (month==0 and day>= 0)):
        age = year
    else : age = year - 1
    return age

#age(saisie_date_naissance())

def est_majeur(date_naissance:datetime.date)->bool:
    result = False
    if(age(date_naissance) >= 18):
        result = True
    return result

def test_access()->str:
    char = ""
    date_naissance = saisie_date_naissance()
    if(est_majeur(date_naissance)):
        char = ("Bonjour, vous avez " + str(age(date_naissance)) + " ans. Accès autorisé")
    else :
        char = ("Désolé, vous avez " + str(age(date_naissance)) + " ans. Accès interdit")
    return char

def test_age()->None:
    """ 
    Fonction de test appelant de manière succéssive la fonction test_access 
    """
    j = check_int("Combien de test voulez-vous effectuez : ")
    for i in range(j):
        test_access()
    
    