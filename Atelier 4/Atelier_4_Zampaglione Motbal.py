# -*- coding: utf-8 -*-
"""
Created on Mon Sep  15 8:46:45 2020
Fonction de l'atelier 4
Version 1
@author: Enzo Zampaglione, Thomas Motbal
"""

###############################################################################
#                                                                             #
#                       Fonctions Communes                                    #
#                                                                             #      
###############################################################################  

def check_char(phrase:str)->chr:
    """Ask user to enter an char
    Keyword argument :
    phrase -- What will be asked to the user
    return an char entered by the user
    """
    result:bool = False
    user_input = input(phrase)
    print("\n")
    while(not result) : 
        try:
            #Si les 2 lignes suivantes sont exécutées sans erreur, on 
            # a une entrée valide.
            if(len(user_input)==1 and user_input.isalpha()):
                val = user_input
                result = True
            else:
                user_input = input(phrase)
        except ValueError:
            #Si on a une erreur de valeur, on demande à l'utilisateur d'entrer
            #à nouveau une valeur.
            user_input = input(phrase)
    return val

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
#               EXERCICE 1 : Manipulations simples                            #
#                                                                             #
#                                                                             #      
###############################################################################  
""" 
JF-GIAMMARI
def full_name3(str_arg: str) -> str:
     Transform text (Uppercase for Name, Lowercase for surname)
    str_arg -- The string who contain the name/surname
    return the formated text
    
    res = str_arg.split()
    return res[0].upper() + " " + res[1].capitalize()
"""
""" a faire"""

def full_name(name:str)->str:
    """Transforme text, uppercase for name, capitalize for surname
    Keyword argument :
    name -- str name we need to transforme
    return an str (name transformed)
    """
    n:int=0
    result:str=""
    while name[n]!=" " and n<=len(name):
        result+=name[n].upper()
        n+=1
    result+=name[n].upper()
    n+=1
    result+=name[n].upper()
    n+=1
    while n!=len(name):
        result+=name[n]
        n+=1
    return result
    
def full_name_2(str_arg:str)->str:
    """Transforme text, uppercase for name, capitalize for surname
    Keyword argument :
    name -- str name we need to transforme
    return an str (name transformed)
    """
    name = ""
    espace = 0
    espace_found = False
    for i,c in enumerate(str_arg):
        if(c == " "):
            espace = i
            espace_found = True
        elif(espace_found and i>espace+2):
            name+=str_arg[i]
        else:
            name+=str_arg[i].upper()
    return name


def check_corps(corps:str)->bool:
    """Check if the body of an email address is correct
    Keyword argument :
    corps -- body of the email address
    return a bool (True = body correct/ False = body incorrect)
    """
    result = True
    if(corps[0] == '.' or corps[-1] == '.'): #commence pas par un point
        result = False
        return result
    for i in corps:
        if(not(i.isalpha() or i.isnumeric() or i=="." or i=="-") or i==" "):
            result = False
    return result

def is_mail(str_arg:str)->(int,int):
    """Check if an email address is correct
    Keyword argument :
    str_arg -- the email address
    return a (int,int) ((0,1) = body error / (0,2) = arobase error / (0,3) = name domain / (0,4) = point error / (1,0) = email address correct)
    """
    CORPS_ERROR = (0,1)
    AROBASE_INCORRECT = (0,2)
    NOM_DOMAINE_ERROR = (0,3)
    POINT_ERROR = (0,4)
    
    result=(1,0)
    arobase = str_arg.find('@')
    point = str_arg.rfind('.')
    if(arobase==-1):
        result = AROBASE_INCORRECT
    elif(64>arobase>3):
        if(not check_corps(str_arg[0:arobase])):
            result = CORPS_ERROR
    else:
        result = CORPS_ERROR
    
    if(point==-1 or point<=arobase):
        result=POINT_ERROR
    elif(len(str_arg[arobase+1:point])<3):  #3 caractère minimum
        result = NOM_DOMAINE_ERROR  
    else:
        if(not check_corps(str_arg[arobase+1:point])):
                result = NOM_DOMAINE_ERROR
    return result
    
  
    
        
        
###############################################################################
#                                                                             #
#                       EXERCICE 2 : Mots croisés                             #
#                                                                             #      
###############################################################################    

def mots_Nlettres(lst_mot:list,n:int)->list:
    """Keep the words into the list (lst_mot) with the number of characters desired (n)
    Keyword argument :
    lst_mot -- a list of word
    n -- the desired number of characters 
    returns a list of words with the desired number of characters
    """
    result = []
    for i in lst_mot:
        if(len(i) == n):
            result.append(i)
    return result

def test_exercice2(mots_Nlettres:callable)->None:
    """Test function mots_Nlettres
    Keyword argument :
    mots_Nlettres -- function
    return None
    """
    lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer"]
    print(mots_Nlettres(lst_mot, 4))
    print(mots_Nlettres(lst_mot, 5))
    print(mots_Nlettres(lst_mot, 6))
    print(mots_Nlettres(lst_mot, 7))


def commence_par(mot:str, prefixe:str)->bool:    
    """Check if a word (mot) starts with a specific prefix (prefixe) 
    Keyword argument :
    mot -- a word
    prefixe -- a prefix
    return a bool (True = word starts with the prefix / False = word does not starts with the prefix)
    """
    return(mot.find(prefixe) == 0)
    

def finit_par(mot:str, suffixe:str)->bool:
    """Check if a word (mot) ends with a specific suffix (suffixe) 
    Keyword argument :
    mot -- a word
    suffix -- a suffix
    return a bool (True = word ends with the suffix / False = word does not ends with the suffix)
    """
    return(mot.rfind(suffixe) == len(mot)-len(suffixe))

def commencent_par(lst_mot:list, prefixe:str)->list:
    """Check for each item of a list of word (mot) if they starts with a specific prefix (prefixe) 
    Keyword argument :
    lst_mot -- a list of word
    prefixe -- a prefix
    return a list of words who have this prefix
    """
    result = []
    for i in lst_mot:
        if(commence_par(i,prefixe)):
            result.append(i)
    return result

def finissent_par(lst_mot:list, suffixe:str)->list:
    """Check for each item of a list of word (mot) if they ends with a specific suffix (suffixe) 
    Keyword argument :
    lst_mot -- a list of word
    suffix -- a suffix
    return a list of words who have this suffix
    """
    result = []
    for i in lst_mot:
        if(finit_par(i,suffixe)):
            result.append(i)
    return result
        
def liste_mots(lst_mot:list,prefixe:str,suffixe:str,n:int)->list:
    """Check for each item of a list of word (mot) if they starts and ends with a specific prefix and suffix (prefixe, suffixe) 
    Keyword argument :
    lst_mot -- a list of word
    prefix -- a prefix
    suffix -- a suffix
    return a list of words who have this prefix and suffix
    """
    result = commencent_par(lst_mot,prefixe)
    result = mots_Nlettres(result,n)
    result = finissent_par(result, suffixe)
    return result

def test_liste_mots(liste_mots:callable)->None:
    """Test function liste_mots
    Keyword argument :
    liste_mots -- function
    return None
    """
    lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer"]
    prefixe = ["jo", "cou", "a"]
    suffixe = ["oir", "r", "ir"]
    print(liste_mots(lst_mot,prefixe[0],suffixe[0] ,4))
    print(liste_mots(lst_mot,prefixe[1],suffixe[2] ,5))
    print(liste_mots(lst_mot,prefixe[0],suffixe[1] ,6))
    print(liste_mots(lst_mot,prefixe[2],suffixe[0] ,7))
    print(liste_mots(lst_mot,prefixe[0],suffixe[1] ,5))

def dictionnaire(fichier:str)->list:
    """Reading a file
    Keyword argument :
    fichier -- the file
    return a list (content of the file)
    """
    f=open(fichier + ".txt","r",encoding='utf8')
    list_mot =[]
    contents = f.readlines()
    #print("** Contenu du fichier **")
    for i in range(len(contents)):
         list_mot.extend(contents[i].split())
    #print("** fin **")
    f.close()  
    return list_mot    
###############################################################################
#                                                                             #
#                       EXERCICE 3 : Jeu du pendu                             #
#                                                                             #      
###############################################################################   
        
#commence_par(mot, prefixe)

import random as rand

def placesLettre(char:str, mot:str)->list:
    """Find all the index of a letter in a word
    Keyword argument :
    char -- a letter
    mot -- a word
    return a list of index
    """
    pla_lettre = []
    for i in range(len(mot)):
        if(commence_par(mot[i], char)):
            pla_lettre.append(i)
    return pla_lettre

def outputStr(mot:str)->str:
    """Replace all the letter of a word by "_ "
    Keyword argument :
    mot -- a word
    return a string of "_ "
    """
    result:str = ""
    for i in mot:
        result += "_ "
    return result

def outputStr_answer(list_char:list, mot:str)->str:
    """Replace all the letter of a word by "_ " except the letter in list_char
    Keyword argument :
    list_char -- list of caractere who don't need to be transform
    mot -- a word
    return a string of "_ " and letter
    """
    result:str = ""
    for i in mot:
        if i not in list_char:
            result += "_ "
        else:
            result+=i
    return result


def select_word(sorted_words:dict, word_len:int)->str:
    """select a randomword in a dictionary (sorted_words) with a specific length (word_len)
    Keyword argument :
    sorted_words -- a dictionary
    word_len -- length of the word we desire
    return a string (a random seleted)
    """
    mot:str = ""
    clef_random = rand.randint(3,word_len)
    valeur_random = len(sorted_words[clef_random])-1
    mot = sorted_words[clef_random][rand.randint(0,valeur_random)]
    return mot

def runGame():
    """It's a hangman's game
    Keyword argument :
    None
    return None
    """
    C = ["|---] ","| O ","| T ","|/ \ ","|______"]
    EASY = 1
    NORMAL = 2
    HARD = 3
    TAILLE_MOT_MAX = 23
    BORNE_HARD = 8
    BORNE_INF_NORMAL = 7
    BORNE_SUP_NORMAL = 9
    BORN_INF_EASY = 3
    BORNE_SUP_EASY = 6
    #dSetWords = {"fromage":len("fromage"), "bonjour":len("bonjour"), "enzo":len("enzo"), "guitare":len("guitare")}
    dSetWords = dictionnaire_pendu("littre")
    j:int = 0
    check:bool = False
    taille_mot:int = 0
    #Choisis la difficulter
    while(not check):
        difficulter = check_int("Pour niveau EASY taper 1 : \n"  
                                +"Pour niveau NORMAL taper 2 : \n"
                                +"Pour niveau HARD taper 3 : \n")
        if(difficulter==EASY or difficulter==NORMAL or difficulter==HARD):
            check = True
    if(difficulter == EASY):
        taille_mot = rand.randint(BORN_INF_EASY,BORNE_SUP_EASY)
    elif(difficulter == NORMAL):
        taille_mot = rand.randint(BORNE_INF_NORMAL,BORNE_SUP_NORMAL)
    else:
        taille_mot = rand.randint(BORNE_HARD, TAILLE_MOT_MAX)
    mot:str = select_word(dSetWords, taille_mot) #mot à trouver
    #print(mot)
    letter_found:bool = False #pour print les lettres correctes
    char:str = [] #lettre proposer par l'user
    list_char:list = []#liste des lettre correct proposer par l'user

    win:str = mot #condition de victoire
    j = 0
    #début du jeu
    while(j<5 and len(win)!=0):
        if(letter_found):
            print(outputStr_answer(list_char, mot))
        else:
            print(outputStr(mot))
        print(5-j, "erreur restants")
        char = check_char("Veuillez saisir une lettre : ")
        pla_lettre = len(placesLettre(char, mot))
        #Si erreur
        if(pla_lettre == 0):
            j+=1 
            for i in range(j):
                print(C[i], "\n")   
        else:
            list_char.append(char)
            letter_found = True
            win = win.strip(str(list_char))
    if(j==5):
        print("Dommage !")
    else:
        print("BRAVO ! le mot était {}" .format(mot))

def dictionnaire_pendu(fichier:str)->list:
    """Reading a file
    Keyword argument :
    fichier -- the file
    return a dictionary (content of the file, key are the lenght of words and values are the words)
    """
    f=open(fichier + ".txt","r",encoding='utf8')
    dico = {}
    contents = f.readlines()
    #print("** Contenu du fichier **")
    for i in range(len(contents)):
        contents[i] = contents[i].strip("\n")
        taille_du_mot = len(contents[i])
        try:
            dico[taille_du_mot].append(contents[i])
        except:
            dico[taille_du_mot] = [contents[i]]
    #print("** fin **")
    f.close()  
    return dico
    
###############################################################################
#                                                                             #
#                       EXERCICE 4 : Aide scrabble                            #
#                                                                             #      
############################################################################### 

def mot_correspond(mot:str,motif:str)->bool:
    """Check if a word (mot) matches a pattern (motif) (dots can replace any letters)
    Keyword argument :
    mot -- the word
    motif -- the pattern
    return a bool (True = word matches the pattern/ False = word does not matches the pattern)
    """
    i=0
    result = True
    if(len(mot) == len(motif)):
        while(result and i<len(mot)):
            if(mot[i]!=motif[i] and motif[i]!='.'):
                result = False
            i+=1
    else :
        result = False
    return result

def presente(lettre:str, mot:str)->int:
    """Check if a letter (lettre) is in a word (mot)
    Keyword argument :
    lettre -- a letter
    mot -- the word
    return a bool (True = letter is in the word/ False = letter is not in the word)
    """
    return mot.find(lettre)

def mot_possible_opti(mot:str, lettres:str)->bool:
    return (mot.strip(lettres) == "")

def mot_possible(mot:str, lettres:str)->bool:
    """Check if the word (mot) can be obtained with letters (lettres)
    Keyword argument :
    mot -- the word
    lettres -- the letters
    return a bool (True = the word can be obtained with the letters/ False = the word can't be obtained with the letters)
    """
    result = True
    list_lettres:str = lettres
    partition:list = []
    for i in mot:
        index = presente(i, list_lettres)
        if(index>=0):
            partition = list(list_lettres.partition(i))
            partition.pop(1)
            list_lettres = "".join(partition)
        else:
            result = False
    return result

def mot_optimaux(dico:list, lettres:str)->list:
    """Check if you can obtain optimal words (based on length) in the dictionary (dico) with letters (lettres)
    Keyword argument :
    dico -- the dictionary
    lettres -- the letters
    return a list of words of maximum length present in the dictionary who we can obtain with the letters 
    """
    list_mot = []
    for i in range(len(lettres), 0, -1):
        mot_existant = mots_Nlettres(dico, i)
        #if(len(mot_existant) > 0)
        for i in mot_existant:
            if(mot_possible(i, lettres)):
                list_mot.append(i)
    return list_mot

#print(mot_optimaux(dictionnaire('littre'), 'plmaisbrsuq'))
    

###############################################################################
#                                                                             #
#            EXERCICE 5 : Vérification d'expressions arithmétiques            #
#                                                                             #      
###############################################################################  

def ouvrante(car:str)->bool:
    """Check whether a character is a parenthesis, bracket, or open brace
    Keyword argument :
    car -- the caractere
    return a bool (True = car is a parenthesis, bracket, or open brace/ False = is not a parenthesis, bracket, or open brace)
    """
    list_ouvrante:list = ["[","(","{"]
    return(car in list_ouvrante)

def fermante(car:str)->bool:
    """Check whether a character is a parenthesis, bracket, or closing brace
    Keyword argument :
    car -- the caractere
    return a bool (True = car is a parenthesis, bracket, or closing brace/ False = is not a parenthesis, bracket, or closing brace)
    """
    list_fermante:list = ["}",")","]"]
    return(car in list_fermante)

def operateur(car:str)->bool:
    """Check whether a character is a + or a *
    Keyword argument :
    car -- the caractere
    return a bool (True = car is a + or a */ False = is not a + or a *)
    """
    list_operateur:list = ["+", "*", "-"] #j'ai rajouté -
    return(car in list_operateur)

def nombre(car:str)->bool:
    """Check if a caractere is a number
    Keyword argument :
    car -- the caractere
    return a bool (True = car is a number/ False = is not a number)
    """
    return(car.isdigit()) #isnumeric()

def caractere_valide(car:str)->bool:
    """Check if a caractere is a number/+/*/()/{}/[]
    Keyword argument :
    car -- the caractere
    return a bool (True = car is a number/+/*/()/{}/[]/ False = is not a number/+/*/()/{}/[])
    """
    return (nombre(car) or operateur(car) or ouvrante(car) or fermante(car))


def reverse(car:str)->str:
    """Check if a caractere is a number/+/*/()/{}/[] and if the caractere is a ]/}/) return (/{/[
    Keyword argument :
    car -- the caractere
    return a string((/{/[ = ]/}/ | number/+/*/()/{}/[] =  the caractere hitself | "")
    """
    ouvrant = ["(","]","{"]
    fermant = [")","[","}"]
    result:str = ""
    found = False
    if(caractere_valide(car)):
        for i in range(len(fermant)):
            if(car == fermant[i]):
                result = ouvrant[i]
                found = True
        if(not found):
            result = car
    return result
    
def verif_parenthese(expression:str)->bool:
    """check if the arithmetic expression contained in a expression is valid
    Keyword argument :
    expression -- the expression
    return a bool (True = the expression is valid/False = the expression is not valid)
    """
    result = True
    p:list = []
    i:int = 0
    while(result and i<len(expression)):
        car = expression[i]
        if(caractere_valide(car)):
            if(ouvrante(car)):
                p.append(car)
            elif(fermante(car)):
                if(p[-1] == reverse(car)):
                    p.pop()
                else:
                    result = False
            i+=1
        else:
            result = False
    if(len(p) != 0):
        result = False
    return result
    
    