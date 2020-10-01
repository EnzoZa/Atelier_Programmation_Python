# -*- coding: utf-8 -*-
"""
Created on Mon Sep  10 14:39:54 2020
Fonction de l'atelier 3
Version 1
@author: Enzo Zampaglione, Vincent Bonneymare
"""
import matplotlib.pyplot as plt
###############################################################################
#                                                                             #
#                       Fonctions Communes                                    #
#                                                                             #      
###############################################################################  

def check_int(phrase:str)->int:
    """Ask user to enter an int
    Keyword argument :
    phrase -- What will be asked to the user
    return an int entered by the user
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
    """Ask user to enter a float
    Keyword argument :
    phrase -- What will be asked to the user
    return a float entered by the user
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
#        EXERCICE 1 : Calculs, Comptage, Maximum, fonctions entières,         #
#        structures itératives                                                #
#                                                                             #
#                                                                             #      
###############################################################################  
    
def somme_1(L:list)->float:
    """Do the sum (with a for)
    Keyword argument :
    L -- list of item who will be summed
    return the sum of the list
    """
    somme:float = 0
    for i in range(len(L)):
        somme += L[i]
    return somme

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def somme_2(L:list)->float:
    """Do the sum (with a foreach)
    Keyword argument :
    L -- list of item who will be summed
    return the sum of the list
    """
    somme:float = 0
    for e in L:
        somme += e
    return somme

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def somme_3(L:list)->float:
    """Do the sum (with a while)
    Keyword argument :
    L -- list of item who will be summed
    return the sum of the list
    """
    somme:float = 0
    i=0
    while(i<len(L)):
        somme += L[i]
        i+=1
    return somme

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def test_exercice1()->None:
    """Test function somme_1/2/3
    Keyword argument :
    None
    return None
    """
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme_3([]))
    #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 11111 : ", somme_1(S))

#La version qui nous semble la plus adaptée est somme_2 (for e in L)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def moyenne(L:list)->float:
    """Average
    Keyword argument :
    L -- list of item which we want the average
    return the average of the list
    """
    result = 0
    if(len(L)>0):
        result = somme_2(L)/len(L)
    return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def nb_sup_1(L:list,e:float)->int:
    """Count the number of item which are greater than the user entry (e) (with a for)
    Keyword argument :
    L -- list of item 
    e -- element to compare 
    return an int (amount of element in L which are greater than e)
    """
    n_sup:int = 0
    for i in range(len(L)):
        if(L[i]>e):
            n_sup += 1
    return n_sup

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def nb_sup_2(L:list,e:float)->int:
    """Count the number of item which are greater than the user entry (e) (with a foreach)
    Keyword argument :
    L -- list of item 
    e -- element to compare 
    return an int (amount of element in L which are greater than e)
    """
    n_sup:int = 0
    for k in L:
        if(k>e):
            n_sup += 1
    return n_sup

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def nb_sup_list(L:list,e:float)->list:
    """Make a list of item which are greater than the user entry (e)
    Keyword argument :
    L -- list of item 
    e -- element to compare 
    return a list of element in L which are greater than e
    """
    n_sup:list = []
    for k in L:
        if(k>e):
            n_sup.append(k)
    return n_sup
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def moy_sup(L:list,e:float)->float:
    """Do the sum of element which are greater than the user entry (e)
    Keyword argument :
    L -- list of item 
    e -- element to compare 
    return the sum of element in L which are greater than e
    """
    return moyenne(nb_sup_list(L,e))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def val_max(L:list)->float:
    """Find the maximum value in a list
    Keyword argument :
    L -- list of item  
    return a float (the maximum of L)
    """
    #max(L)
    maxi:float = 0
    for e in L:
        if(e>maxi):
            maxi=e
    return maxi

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def ind_max(L:list)->int:
    """Find the index maximum value in a list
    Keyword argument :
    L -- list of item  
    return an int (the index of the maximum of L)
    """
    return (L.index(val_max(L)))
            

###############################################################################
#                                                                             #
#        EXERCICE 2 : Recherches, fonctions boolénnes, boucles while          #
#                                                                             #      
###############################################################################    

def position_1(L:list, e:int)->int:
    """Try to find the index of the user entry in a list (with a for)
    Keyword argument :
    L -- list of item  
    e -- element search
    return an int (the index of e), return -1 by default
    """
    ind:int = -1
    for i in range(len(L)):
        if(L[i]==e):
            ind = i
    return ind

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def position_2(L:list, e:int)->int:
    """Try to find the index of the user entry in a list (with a while)
    Keyword argument :
    L -- list of item  
    e -- item search
    return an int (the index of e), return -1 by default
    """
    i:int = 0
    ind:int = -1
    while(not(L[i] == e) and i<len(L)):
        i += 1
        if(L[i==e]):
            ind = i
    return ind

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def nb_occurences(L:list, e:int)->int:
    """Count how many time an item (e) is in a list (L)
    Keyword argument :
    L -- list of item  
    e -- element
    return an int (how many time e is in L)
    """
    occurences = 0
    for i in L:
        if(i==e):
            occurences += 1
    return occurences

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def est_triee_1(L:list)->bool:
    """Check if a list is sorted (with a for)
    Keyword argument :
    L -- list of item  
    return a bool (True = sorted / False = unsorted)
    """
    check = True
    for i in range(len(L)-1):
        if(L[i] > L[i+1]):
            check = False
    return check

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def est_triee_2(L:list)->bool:
    """Check if a list is sorted (with a while)
    Keyword argument :
    L -- list of item  
    return a bool (True = sorted / False = unsorted)
    """
    check:bool = True
    i:int = 0
    while(check or i==(len(L)-1)):
        if(L[i]>L[i+1]):
            check = False
        i+=1
    return check

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def position_tri(L:list,e:int)->int:
    """Check the position of an item (e) in a sorted list (L) (with the dichotomous method)
    Keyword argument :
    L -- list of item  
    e -- item
    return a int (position of e)
    """
    minimum:int = 0
    maximum:int = len(L)
    milieu:int = 0
    while(L[milieu] != e):
        milieu = int((minimum + maximum)/2)
        if(L[milieu]<e):
            minimum += 1
        elif(L[milieu]>e):
            maximum -= 1
    return milieu

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def a_repetitions(L:list)->bool:
    """Check if there is repeating item in a list (L)
    Keyword argument :
    L -- list of item  
    return a bool (True = repetition / False = no repetition)
    """
    T:list = []
    result:bool = False
    i:int = 0
    while((not result) and i != len(L)):
        x = L[i]
        if(x in T):
           result = True
        else:
            T.append(x)
            i += 1
    return result
            

###############################################################################
#                                                                             #
#                       EXERCICE 3 : Séparation                               #
#                                                                             #      
###############################################################################   
        
def LSEP(L:list)->list:
    """Sort a list by sign
    Keyword argument :
    L -- list of item  
    return a list sorted by sign
    """
    result:list = [0 for i in range(len(L))]
    ind_min:int = 0
    ind_max:int = len(L)-1
    for i in L:
        if (i<0):
            result[ind_min] = i
            ind_min += 1
        elif (i>0):
            result[ind_max] = i
            ind_max -= 1
    return result
        
    
    
###############################################################################
#                                                                             #
#             EXERCICE 4 : Application : fonctions - histogramme              #
#                                                                             #      
############################################################################### 
    
def histo(F:list)->list:
    """Check how many time each item is in the list and return it in a list
    Keyword argument :
    F -- list of item  
    MAXVALEUR -- represents the maximum of values ​​which is between 0-8
    max(F) = 8
    return a list (index = value of the function, value at index = how many 
    time the item is in the list)
    """
    MAXVALEUR = max(F)
    H:list = [0 for i in range(MAXVALEUR + 1)]
          
    for i in F:
        H[i] += 1
        
    return H

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def est_injective(F:list)->bool:
    """Check if a list is injective
    Keyword argument :
    L -- list of item  
    return a bool (True = injective / False = no injective)
    """
    H = histo(F)
    result = True
    for i in H:
        if i>1:
            result = False
    return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def est_surjective(F:list)->bool:
    """Check if a list is surjective
    Keyword argument :
    L -- list of item  
    return a bool (True = surjective / False = no surjective)
    """
    H = histo(F)
    result = True
    for i in H:
        if i<1:
            result = False
    return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def est_bijective(F:list)->bool:
    """Check if a list is bijective
    Keyword argument :
    L -- list of item  
    return a bool (True = bijective / False = no bijective)
    """
    return(est_injective(F) and est_surjective(F))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def affiche_histo(F:list)->None:
    """Print the function in a histogram (using print)
    Keyword argument :
    L -- list of item  
    return the histogram of the function as a print
    """
    H = histo(F)
    print("TEST HISTOGRAMME")
    print("F = " + str(F))
    print("HISTOGRAMME")
    MAXOCC = val_max(H) 
    TAILLE = len(H)
    line=" "
    #i correspond à la ligne
    for i in range(MAXOCC):
        #j correspond à la colonne
        line+=str(MAXOCC-i)+"║ "
        for j in range(TAILLE):
            if(H[j]>=MAXOCC-i):
                line+=" █  "
            else:
                line+="    "
        line+=" "
        print(line)
        line=" "
    line+=" ╚══"
    for j in range(TAILLE):
        line+="════" 
    print(line)
    line="    "
    for j in range(TAILLE):
        if(j<10):
            line+=" "+str(j)+"  "
        if(j>=10):
            line+=" "+str(j)+" "

    print(line)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
       
def Test_Histogramme(L:list)->None:
    """Print the function in a histogram (using MatPlotLib)
    Keyword argument :
    L -- list of item  
    return the histogram of the function as a print
    """
    print("Histogramme avec MatPlotLib")
    plt.hist(L,rwidth=0.80)
    
###############################################################################
#                                                                             #
#               EXERCICE 5 : Tests, recherche d'erreurs                       #
#                                                                             #      
###############################################################################  

def present(L:list, e:int)->bool:
    """Search if an item is in a list
    Keyword argument :
    L -- list of item
    e -- item
    return a bool (True = item is in the list/False = item is not in the list)
    """
    result = False
    for i in L:
        if i==e:
            result = True
    return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def test_present(present:callable)->None:
    """Test function present
    Keyword argument :
    present -- function
    return None
    """
    if(not present((),0)):
        print("SUCCES: test liste vide")
    else:
        print("ECHEC: test liste vide")
    
    list_test = (1,2,3,4,5,6,7,8,9,10)
    test_debut = present(list_test, 1)
    test_fin = present(list_test, 10)
    test_milieu = present(list_test, 5)
    test_absent = present(list_test, 26)
    
    if(test_debut):
        print("SUCCES: test liste debut")
    else:
        print("ECHEC: test liste debut")
        
    if(test_fin):
        print("SUCCES: test liste fin")
    else:
        print("ECHEC: test liste fin")
        
    if(test_milieu):
        print("SUCCES: test liste milieu")
    else:
        print("ECHEC: test liste milieu")
        
    if(not test_absent):
        print("SUCCES: test liste absent")
    else:
        print("ECHEC: test liste absent")

#VERSION 1
def present1 (L, e) :
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            return(True)
        else :
            return (False)
    return (False)

#VERSION 2
def present2 (L, e) :
    b=True
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            b=True
        else :
            b=False
    return (b)

#VERSION 3    
def present3 (L, e) :
    b=True
    for i in range (0, len(L), 1) :
        return (L[i] == e)
    
#VERSION 4
def present4 (L, e) :
    b=False
    i=0
    while (i<len(L) and b) :
        if (L[i] == e) :
            b=True
    return (b)

############################################
#                CORRECTION                #
############################################

def present1_corriger(L:list, e:int)->bool:
    #On enleve le else dans la boucle pour car sinon on arrêter tout à la première itération
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            return(True)
    return (False)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def present2_corriger(L:list, e:int)->bool:
    b=False
    #On initialise b à false et on enleve le else dans la boucle pour 
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            b=True
    return (b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def present3_corriger(L:list, e:int)->bool:
    #avec le return dans la boucle pour, le programme return le resultat juste pour la premiere itération
    b=True
    for i in range (0, len(L), 1) :
        if (L[i] == e):
            return (L[i] == e)
    return not b

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def present4_corriger(L:list, e:int)->int:
    b=False
    i=0
    while (i<len(L) and not b) : #il faut que b soit à true dans le while
        if (L[i] == e) :
            b=True
        i += 1 #il faut incrémenter le i pour éviter les boucles infinis 
    return (b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def pos(L:list, e:int)->list:
    """Find all the position of an item in a list
    Keyword argument :
    L -- list of item
    e -- item
    returns a list of all the position of an item
    """
    result:list = []
    for i in range(len(L)):
        if(L[i] == e):
            result.append(i)
    return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def test_pos(pos:callable):
    """Test function pos
    Keyword argument :
    pos -- function
    return None
    """
    if(len(pos((),0)) == 0):
        print("SUCCES: test liste vide")
    else:
        print("ECHEC: test liste vide")
    
    list_test = (3,4,5,7,2,7)
    test_unique = pos(list_test, 2)
    test_multiple = pos(list_test, 7)
    test_absent = pos(list_test, 26)
    
    if(test_unique == [4]):
        print("SUCCES: test liste unique")
    else:
        print("ECHEC: test liste unique")
        
    if(test_multiple == [3,5]):
        print("SUCCES: test liste multiple")
    else:
        print("ECHEC: test liste multiple")
        
    if(test_absent == []):
        print("SUCCES: test liste absent")
    else:
        print("ECHEC: test liste absent")
        
        
#VERSION 1
def pos1(L, e) :
    Lres = list(L)
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres += [i]
    return Lres

# VERSION 2
def pos2(L, e) :
    Lres = list(L)
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[i] = i
    return Lres

# VERSION 3
def pos3(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres

# VERSION 4
def pos4(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    j=0
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[j]= i
    return Lres

############################################
#                CORRECTION                #
############################################
    
#VERSION 1/2
def correction_pos1(L, e) :
    #Il faut initer Lres à []
    Lres = []
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres += [i]
    return Lres

# VERSION 3
def correction_pos3(L, e) :
    #nb= L.count(e)
    Lres = []
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres

# VERSION 4
def correction_pos4(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    j=0
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[j]= i
            #Il faut incrementer le j pour ne pas effacer la valeur precedente
            j+=1
    return Lres

