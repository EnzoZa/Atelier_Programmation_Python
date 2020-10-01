# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:51:44 2020
Fonction de l'atelier 5
Version 1 
@author: Enzo Zampaglione Thomas Motbal
"""

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
#      EXERCICE 1: Génération de listes de nombres entiers aléatoires         #
#                                                                             #
#                                                                             #      
###############################################################################  
   
import random as rand

def gen_list_random_int(int_binf=0,int_bsup=9)->list:
    TAILLE_LISTE:int = 10
    result:list = []
    for i in range(TAILLE_LISTE):
        result.append(rand.randint(int_binf,int_bsup))
    return result

###############################################################################
#                                                                             #
#               EXERCICE 2 - Mélange des éléments d’une liste                 #
#                                                                             #
#                                                                             #      
###############################################################################  
    

def mix_list(list_to_mix:list)->list:
    L=list_to_mix[:]
    len_list_to_mix = len(list_to_mix)
    for i in range(len_list_to_mix):
        randomNumber=rand.randint(0, len_list_to_mix-1)
        L[i],L[randomNumber] = L[randomNumber],L[i]
    return L

def test_mix_list(mix_list:callable)->None:
    # Test de votre code
    lst_sorted=[i for i in range(10)]
    print(lst_sorted)
    print('Liste triée de départ',lst_sorted)
    mixed_list=mix_list(lst_sorted)
    print('Liste mélangée obtenue',mixed_list)
    print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted)
    #assert (cf. doc en ligne) permet de vérifier qu’une condition
    #est vérifiée en mode debug (désactivable)
    assert lst_sorted != mixed_list,"Les deux listes doivent être différente après l'appel à mixList..."

###############################################################################
#                                                                             #
#       EXERCICE 3 - Choix aléatoire d'un élément dans une liste              #
#                                                                             #
#                                                                             #      
############################################################################### 
    
def choose_element_list(list_in_which_to_choose:list)->int:
    rand_element = rand.randint(0,len(list_in_which_to_choose)-1)
    return list_in_which_to_choose[rand_element]
        
def test_choose_element_list(choose_element_list:callable)->None:
    # Test de votre code
    lst_sorted = [0,1,2,3,4,5]
    print('Liste triée de départ',lst_sorted)
    e1 = choose_element_list(lst_sorted)
    print('A la première exécution',e1,'a été sélectionné')
    e2 = choose_element_list(lst_sorted)
    print('A la deuxième exécution',e2,'a été sélectionné')
    assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"       

###############################################################################
#                                                                             #
#      EXERCICE 4 - Choix aléatoire de plusieurs éléments dans une liste      #
#                                                                             #
#                                                                             #      
############################################################################### 
    
def extract_elements_list(list_in_which_to_choose:list,int_nbr_of_element_to_extract:list)->list:  
    list_tamp:list = list_in_which_to_choose[:]
    result:list = []
    rand_i:int = 0
    rand_max_len:int = len(list_in_which_to_choose)-1
    for i in range(int_nbr_of_element_to_extract):
        rand_i = rand.randint(0,rand_max_len)
        result.append(list_tamp[rand_i])
        list_tamp.pop(rand_i)
        rand_max_len -= 1
    return result

def test_extract_elements_list(extract_elements_list:callable)->None:
    # Test de votre code
    lst_sorted=[i for i in range(10)]
    print('Liste de départ',lst_sorted)
    sublist = extract_elements_list(lst_sorted,5)
    print('La sous liste extraite est',sublist)
    print('Liste de départ après appel de la fonction est',lst_sorted)


###############################################################################
#                                                                             #
#                                                                             #
#        EXERCICE 5 - Mesure et comparaison des temps d’exécution v.1         #
#                                                                             #
#                                                                             #      
############################################################################### 

import time

def perf_mix(mix_list:callable, shuffle:callable, lst_tailles:list)->(list,list):
    result_mix_list:list = []
    result_shuffle:list = []
    NB_ESSAIE = 100
    start_pc_mix_list = 0
    end_pc_mix_list = 0
    start_pc_shuffle = 0
    end_pc_shuffle = 0
    for i in range(len(lst_tailles)):
        lst:list = [j for j in range(lst_tailles[i])]
        rand.shuffle(lst)
        for j in range(NB_ESSAIE): 
            start_pc_mix_list += time.perf_counter()
            mix_list(lst)
            end_pc_mix_list += time.perf_counter()
        
            start_pc_shuffle += time.perf_counter()
            shuffle(lst)
            end_pc_shuffle += time.perf_counter()

        elapsed_time_pc_mix_list = (end_pc_mix_list-start_pc_mix_list)/100
        result_mix_list.append(elapsed_time_pc_mix_list)
        
        elapsed_time_pc_shuffle = (end_pc_shuffle-start_pc_shuffle)/100
        result_shuffle.append(elapsed_time_pc_shuffle)
        
    return(result_mix_list, result_shuffle)

#perf_mix(mix_list, rand.shuffle, [10,500,5000,10000])

import matplotlib.pyplot as plt

def plot_perf_mix(perf_mix_list:list, perf_shuffle:list, lst_tailles):
    #Ici on décrit les abscisses
    #Entre 0 et 5 en 10 points
    x_axis_list_mix_list = perf_mix_list
    x_axis_list_shuffle = perf_shuffle
    fig, ax = plt.subplots() 
    #Dessin des courbes, le premier paramètre
    #correspond aux point d'abscisse le
    #deuxième correspond aux points d'ordonnées
    #le troisième paramètre, optionnel permet de
    #choisir éventuellement la couleur et le marqueur
    ax.plot(lst_tailles,x_axis_list_mix_list, 'r*-', label='Notre fonction')
    ax.plot(lst_tailles,x_axis_list_shuffle,'g*-', label='Random')
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y', title='Comparaison, notre fonction et Random')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()

#mix_list_shuffle = perf_mix(mix_list, rand.shuffle, [10,500,5000,10000])
#print("Comparaison mix_list/shuffle")
#plot_perf_mix(mix_list_shuffle[0],mix_list_shuffle[1], [10,500,5000,10000])

def perf_mix_element(extract_elements_list:callable, sample:callable, lst_tailles:list, int_nbr_of_element_to_extract:int)->(list,list):
    result_extract_elements_list:list = []
    result_sample:list = []
    NB_ESSAIE = 100
    start_pc_1 = 0
    end_pc_1 = 0
    start_pc_2 = 0
    end_pc_2 = 0
    for i in range(len(lst_tailles)):
        lst:list = [j for j in range(lst_tailles[i])]
        for j in range(NB_ESSAIE):
            start_pc_1 += time.perf_counter()
            extract_elements_list(lst,int_nbr_of_element_to_extract)
            end_pc_1 += time.perf_counter()
        
            start_pc_2 += time.perf_counter()
            rand.sample(lst, int_nbr_of_element_to_extract)
            end_pc_2 += time.perf_counter()
            
        elapsed_time_pc = (end_pc_1-start_pc_1)/100
        result_extract_elements_list.append(elapsed_time_pc)
        
        elapsed_time_pc = (end_pc_2-start_pc_2)/100
        result_sample.append(elapsed_time_pc)
        
    return(result_extract_elements_list, result_sample)

#perf_mix_element(extract_elements_list, rand.sample, [10,500,5000,10000], 3)
    
    
#int_nbr_of_element_to_extract_sample = perf_mix_element(extract_elements_list, rand.sample, [10,500,5000,10000], 3)
#print("Comparaison extract_elements_list/sample")
#plot_perf_mix(int_nbr_of_element_to_extract_sample[0],int_nbr_of_element_to_extract_sample[1], [10,500,5000,10000])

###############################################################################
#                                                                             #
#                                                                             #
#                   EXERCICE 6 - Tri à votre mode                             #
#                                                                             #
#                                                                             #      
############################################################################### 

def sort_list(lst:list)->list:
    L:list = lst[:]
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if(L[j+1]<L[j]):
                L[j], L[j+1] = L[j+1], L[j]
    return L

#mix_list_sorted = perf_mix(sort_list, sorted, [10,500])
#print("Comparaison sort_list/sorted")
#plot_perf_mix(mix_list_sorted[0],mix_list_sorted[1], [10,500])

###############################################################################
#                                                                             #
#                                                                             #
#         EXERCICE 7 - Implémentation des algorithmes de tri classiques       #
#                                                                             #
#                                                                             #      
############################################################################### 

def stupid_sort(lst_to_sort:list)->list:
    L:list = lst_to_sort[:]
    i=0
    while(L!=sort_list(lst_to_sort)):
        i+=1
        L = mix_list(L)
    return L,i

def insertion_sort(lst_to_sort:list)->list :
    L:list = lst_to_sort[:]
    for i in range(1, len(lst_to_sort)) :
        tampon = L[i]
        j = i-1
        while (L[j] > tampon) and (j>=0) :
            L[j+1] = L[j]
            j = j-1
        L[j+1] = tampon 
    return L

def argmin(tab, debut, fin) :
    plus_petit = debut
    for ind in range (debut + 1, fin) : 
        if(tab[ind] < tab[plus_petit]) :
           plus_petit = ind
    return plus_petit

def selection_sort(lst_to_sort:list)->list :
    L:list = lst_to_sort[:]
    for ind in range(0, len(lst_to_sort)) :
        pp = argmin(L, ind, len(L))
        if(pp!=ind) :
            L[ind], L[pp] = L[pp], L[ind]
    return L

def buble_sort_opti(lst:list)->list:
    L:list = lst[:]
    sorted_list:bool = False
    for i in range(len(lst)-1):
        sorted_list = True
        for j in range(len(lst)-i-1):
            if(L[j+1]<L[j]):
                L[j], L[j+1] = L[j+1], L[j]
                sorted_list = False
        if(sorted_list):
            break
    return L

#☺mix_list_sorted = perf_mix(buble_sort_opti, sorted, [10,500,5000,10000])
#print("Comparaison sort_list/sorted")
#plot_perf_mix(mix_list_sorted[0],mix_list_sorted[1], [10,500,5000,10000])

def merge_sort(list_to_sort:list)->list:
    T:list = list_to_sort[:]
    n = len(list_to_sort)
    if n<=1:
         return list_to_sort
    else:
        return fusion(merge_sort(T[0:n//2]), merge_sort(T[n//2:len(T)]))
                             
def fusion(A:list,B:list)->list:
    if(len(A)==0):
        return B
    elif(len(B)==0):
        return A
    if (A[0] < B[0]):
        return [A[0]] + fusion(A[1:], B)
    else:
        return  [B[0]] + fusion(A, B[1:])

#mix_list_sorted = perf_mix(merge_sort, sorted, [10,500,5000])
#print("Comparaison tri fusion/sorted")
#plot_perf_mix(mix_list_sorted[0],mix_list_sorted[1], [10,500,5000])


def get_digit(number:int, n:int)->int:
    return number // 10**n % 10


def radix_sort(lst_to_sort:list)->list:
    maximum:int = 0
    amount_of_digit:int = 0
    for e in lst_to_sort:
        if(e>maximum):
            maximum = e

    amount_of_digit :int= len(str(maximum))
    tableau_trie:bool = False
    length:int = len(lst_to_sort)-1

    for i in range(amount_of_digit):
        length = len(lst_to_sort)-1
        while (length>1 or not tableau_trie):
            tableau_trie = True

            for j in range(length):
                if(get_digit(lst_to_sort[j+1],i)<get_digit(lst_to_sort[j],i)):
                    lst_to_sort[j],lst_to_sort[j+1] = lst_to_sort[j+1],lst_to_sort[j]
                    tableau_trie = False
            length -= 1
    print(lst_to_sort)
    
###############################################################################
#                                                                             #
#                                                                             #
#      EXERCICE 8 - Découverte expérimentale de la complexité de sorted       #
#                                                                             #
#                                                                             #      
############################################################################### 

def plot_perf_mix_all(lst_tailles):
    #Ici on décrit les abscisses
    #Entre 0 et 5 en 10 points


    #calcul des temps
    merge_sort_sorted = perf_mix(merge_sort, sorted, lst_tailles)
    buble_sort_stupid = perf_mix(buble_sort_opti, stupid_sort, lst_tailles)
    insertion_sort_selection = perf_mix(insertion_sort, selection_sort, lst_tailles)
    
    time_insertion=insertion_sort_selection[0]
    time_selection=insertion_sort_selection[1]
    time_buble=buble_sort_stupid[0]
    #time_stupid=buble_sort_stupid[1]
    time_merge_sort = merge_sort_sorted[0]
    time_sorted = merge_sort_sorted[1]
    fig, ax = plt.subplots() 
    #Dessin des courbes, le premier paramètre
    #correspond aux point d'abscisse le
    #deuxième correspond aux points d'ordonnées
    #le troisième paramètre, optionnel permet de
    #choisir éventuellement la couleur et le marqueur
    #ax.plot(lst_tailles,time_stupid, label='Stupide')
    ax.plot(lst_tailles,time_selection, label='Selection')
    ax.plot(lst_tailles,time_insertion, label='Insertion')
    ax.plot(lst_tailles,time_buble, label='Buble')
    ax.plot(lst_tailles,time_merge_sort, label='Fusion')
    ax.plot(lst_tailles,time_sorted, label='Sorted')
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y', title='Comparaison, nos fonction et Sorted')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()

  
plot_perf_mix_all([10,50,100])
