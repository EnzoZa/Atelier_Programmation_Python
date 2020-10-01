# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:15:54 2020
Last edit on Mon Sep  10 8:38:54 2020
Fonction de l'atelier 1
Version 1.1
@author: Enzo Zampaglione, Vincent Bonneymare
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
#                           Exercice 1 : Calcul de salaire                    #
#                                                                             #
###############################################################################
    
def exercice1()->float:
    """
    Fonction qui calcule le salaire en fonction des entrées de l'utilisateur.
    
    Fonction ne prenant aucun paramètre d'entrée et renvoyant un float.
    Il est demandé à l'utilisateur de rentrer succesivement le nombre d'heure
    de travail et le taux honoraire auquel ces heures sont payées.
    
    Description des constantes locales:
    
    PALIER_HEURE_2: correspond à la limite à partir de laquelle les heures de
        travail sont payées à un ratio plus élevé égal à HEURE_SUP_1.
    PALIER_HEURE_2: correspond à la limite à partir de laquelle les heures de
        travail sont payées au tarif 2 (HEURE_SUPP_2).
    HEURE_SUP_1: correspond au multiplicateur du tarif des heures
        effectuées dans l'intervalle [160;200].
    HEURE_SUP_2: correspond au multiplicateur du tarif des heures
        effectuées dans l'intervalle ]200;INF[.
    """
    ## Définition des constantes locales ##
    
    PALIER_HEURE_1:int = 160
    PALIER_HEURE_2:int= 200
    HEURE_SUP_1:float = 1.25
    HEURE_SUP_2:float = 1.5
    
    ## Début du script ##
    
    result:float = 0
    nb_heure = check_float("Combien d'heures avez-vous fait : ")
    salaire_horaire = check_float("Quel est votre taux horaire : ")
    if (nb_heure <= PALIER_HEURE_1):
        result = salaire_horaire*nb_heure
    elif (nb_heure <= PALIER_HEURE_2):
        result = salaire_horaire*PALIER_HEURE_1 + ((nb_heure-PALIER_HEURE_1)*salaire_horaire*HEURE_SUP_1)
    else :
        result = salaire_horaire*PALIER_HEURE_1 + ((PALIER_HEURE_2-PALIER_HEURE_1)*salaire_horaire*HEURE_SUP_1) + ((nb_heure-PALIER_HEURE_2)*salaire_horaire*HEURE_SUP_2) 
    return result

###############################################################################
#                                                                             #
#                         Exercice 2 : Reconnaissance de caractère            #
#                                                                             #
###############################################################################
    
def exercice2()->str:
    """
    Fonction qui renvoie la  catégorie d'un caractère rentré par l'utilisateur.
    
    Fonction ne prenant aucun paramètre d'entrée et renvoyant un string.
    Il est demandé à l'utilisateur de rentrer un caractère et seulement un.
    La fonction renverra alors un string qui décrit la nature de ce caractère
    parmis 4 catégories (Lettre minuscule,lettre majuscule,chiffre ou caractère
    spécial).
    
    Il n'existe pas de constantes locales dans cette fonction.
    
    NB: En python il est possible de comparer directement des caractères et
    ainsi ne pas utiliser la fonction ord() sur un caractère. La valeur
    dans la table ASCII du caractère est alors prise en compte.
    """
    ## Début du script ##
    
    #On attribue une valeur par défaut non valide afin de demander à 
    #l'utilisateur un seul caractère.
    char = 'abc'
    result:str = None
    while(len(char)>1):
        char = str(input("Mettez un caractère : "))
    code_ascii = ord(char)
    if (code_ascii >= ord('A') and code_ascii <= ord('Z')):
        result = (str(char) + " est une lettre majuscule")
    elif (code_ascii >= ord('a') and  code_ascii <= ord('z')):
        result = (str(char) + " est une lettre minuscule")
    elif (code_ascii >= ord('0') and  code_ascii <= ord('9')):
        result = (str(char) + " est un chiffre")
    else :
        result = (str(char) + " est un caractère spécial")
    return result

###############################################################################
#                                                                             #
#                           Exercice 3 : Impôts                               #
#                                                                             #
###############################################################################
    
def exercice3()->str:
    """
    Fonction qui calcule si une personne est imposable.
    
    Fonction ne prenant aucun paramètre d'entrée et renvoyant un string.
    Il est demandé à l'utilisateur de rentrer un caractère et seulement un
    correspondant au sexe d'une personne.
    Il sera ensuite demandé à l'utilisateur de rentrer un int correspondant
    à l'age d'une personne.
    La fonction renverra alors un string qui décrit si, en fonction des valeurs
    précédement rentrées, la personne est imposable ou non.
    
    Description des constantes locales:
        
    H: permet d'identifier que la personne est un homme.
    F: permet d'identifier que la personne est une femme.
    AGE_MIN_FEMME: correspond à l'age minimal auquel une femme est imposable.
    AGE_MAX_FEMME: correspond à l'age maximal auquel une femme est imposable.
    AGE_MIN_HOMME: correspond à l'age minimal auquel un homme est imposable.
    """
    ## Définition des constantes locales ##
    
    AGE_MIN_HOMME:int = 20
    AGE_MIN_FEMME:int = 18
    AGE_MAX_FEMME:int = 35
    
    ## Début du script ##
    
    result:str = None
    sexe:str = None 
    while(not(sexe=="H" or sexe=="M")):
        sexe = input("Sexe (H ou M) : ")
    age = check_int("Age : ")
    result = "Cette personne est non imposable"
    if(sexe=="H" and age >= AGE_MIN_HOMME):
        result = "Cette personne est imposable"
    elif(sexe=="F" and age>=AGE_MIN_FEMME and age<=AGE_MAX_FEMME):
        result = "Cette personne est imposable"
    return result

###############################################################################
#                                                                             #
#                           Exercice 4 : Reprographie                         #
#                                                                             #
###############################################################################
    
def exercice4()->float:
    """
    Fonction qui calcule le prix à payer pour une quantité de photocopie.
    
    Fonction ne prenant aucun paramètre d'entrée et renvoyant un float.
    Il est demandé à l'utilisateur de rentrer un int correspondant au nombre
    de photocopie effectuée.
    La fonction renverra alors un float correspondra au prix à payer pour le
    nombre de photocopie entré.
    
    Description des constantes locales:
            
    PALIER_1: quantité de copie facturée sans tarif réduit.
    PALIER_2: quantité de copie facturée avec tarif réduit.
    PALIER_3: quantité de copie au delà de laquelle le tarif est doublement
    réduit.
    PREMIER_TARIF: prix à payer pour chaque photocopie initialement.
    SECOND_TARIF: prix à payer pour chaque photocopie lors de la première
    réduction de tarif.
    TROISIEME_TARIF: prix à payer pour chaque photocopie lors de la seconde
    réduction de tarif.
    
    """
    ## Définition des constantes ##
    
    PALIER_1:int = 10
    PALIER_2:int = 20
    PALIER_3:int = 30
    PREMIER_TARIF:float = 0.10
    SECOND_TARIF:float = 0.09
    TROISIEME_TARIF:float = 0.08
    
    ## Début du script ##
    
    result:float = 0
    nb_photocopie = check_int("Combien voulez-vous de photocopie : ")
    if (nb_photocopie <= PALIER_1):
        result =  nb_photocopie*PREMIER_TARIF
    elif (nb_photocopie <= PALIER_3):
        result =  PALIER_1*PREMIER_TARIF + ((nb_photocopie-PALIER_1)*SECOND_TARIF)
    else :
        result = PALIER_1*PREMIER_TARIF + (PALIER_2*SECOND_TARIF) + ((nb_photocopie-PALIER_3)*TROISIEME_TARIF) 
    return result

###############################################################################
#                                                                             #
#                        Exercice 5 : Calcul de frais portuaires              #
#                                                                             #
###############################################################################

def exercice5()->str:
    """
    Fonction qui calcule les frais portuaires annuel d'un bateau.
    
    Fonction ne prenant aucun paramètre d'entrée et renvoyant un string.
    Il est demandé à l'utilisateur de rentrer une chaîne de caractère
    correspondant au nom du bateau, un int correspondant à la longueur du
    bateau puis un int correspondant à la catégorie du bateau.
    La fonction renverra alors un string qui donnera pour le nom, longueur
    et catégorie du bateau, les frais qui seront réclamés.
    
    Description des constantes locales:
            
    COUT_MENSUEL_1: correspond au prix par mois à payer pour un bateau de
    longueur inferieure à LONGUEUR_1.
    COUT_MENSUEL_2: correspond au prix par mois à payer pour un bateau de
    longueur inferieure à LONGUEUR_2.
    COUT_MENSUEL_3: correspond au prix par mois à payer pour un bateau de
    longueur inferieure à LONGUEUR_3.
    COUT_MENSUEL_4: correspond au prix par mois à payer pour un bateau de
    longueur supérieure à LONGUEUR_3.
    TAXE_1: correspond à la valeur de taxe imposée aux bateaux de catégorie 1.
    TAXE_2: correspond à la valeur de taxe imposée aux bateaux de catégorie 2.
    TAXE_3: correspond à la valeur de taxe imposée aux bateaux de catégorie 3.
    LONGUEUR_1: correspond au premier seuil de longueur des bateaux.
    LONGUEUR_2: correspond au second seuil de longueur des bateaux.
    LONGUEUR_3: correspond au troisième seuil de longueur des bateaux.
    
    """
    ## Définition des constantes locales ##
    
    COUT_MENSUEL_1:float = 100
    COUT_MENSUEL_2:float = 200
    COUT_MENSUEL_3:float = 400
    COUT_MENSUEL_4:float = 600
    TAXE_1:float = 100
    TAXE_2:float = 150
    TAXE_3:float = 250
    LONGUEUR_1:float = 5
    LONGUEUR_2:float = 10
    LONGUEUR_3:float = 12
    
    ## Début du script ##
    
    cout_mensuel:float = 0
    taxe:float = 0
    cout_annuel:float = 0
    nom = input("Nom du voilier : ")
    longueur = check_float("Longueur du voilier : ")
    categorie = check_int("Categorie du voilier : ")
    #Vérifiaction du coût mensuel en fonction de la longueur
    if (longueur < LONGUEUR_1):
        cout_mensuel = COUT_MENSUEL_1
    elif (longueur < LONGUEUR_2):
       cout_mensuel = COUT_MENSUEL_2
    elif (longueur < LONGUEUR_3):
       cout_mensuel = COUT_MENSUEL_3
    else :
       cout_mensuel = COUT_MENSUEL_4
    #Vérification de la valeur de la taxe en fonction de la catégorie
    if(categorie == 1):
        taxe = TAXE_1
    elif(categorie == 2):
        taxe = TAXE_2
    else : taxe = TAXE_3
    
    cout_annuel = taxe + cout_mensuel*12
    
    return("Le cout annuel d'une place au port pour le voilier " + nom + " est de " + str(cout_annuel) + " euros")

###############################################################################
#                                                                             #
#                        Exercice 6 : Concessionnaire automobile              #
#                                                                             #
###############################################################################

def exercice6()->float:
    """
    Fonction qui calcule le coût en essence d'un véhicule en fonction du type
    de carburant et du moteur.
    
    Fonction ne prenant aucun paramètre d'entrée et renvoyant un float.
    Il est demandé à l'utilisateur de rentrer un float correspondant
    à une distance en km que devrait parcourir un véhicule, un caractère qui
    définit le type de carburant, suivit d'un float qui définit le volume de la
    cylindrée du véhicule et un float qui définit le prix du carburant par
    litre.
    La fonction renverra alors un float qui est le coût total pour parcourir
    la distance souhaitée avec le véhicule, surcoût compris.
    
    Description des constantes locales:
        
    LIMITE_VOLUME: volume de la cylindrée à partir duquel le tarif essence
    augmente.
    SURCOUT_D: surcoût appliqué au carburant diesel.
    SURCOUT_E: surcoût appliqué au carburant essence.
    CONS_CYL_SUP: consommation d'une cylindrée essence dont le volume est 
    supérieur à la limite de volume (LIMITE_VOLUME)  pour 100 km.
    CONS_CYL_INF: consommation d'une cylindrée essence dont le volume est 
    inférieur à la limite de volume (LIMITE_VOLUME) pour 100 km.
    CONS_D: consommation d'une cylindrée diesel pour 100 km.
    """
    ## Définition des constantes locales ##
    
    LIMITE_VOLUME:int = 2000 
    SURCOUT_D:float = 1.7
    SURCOUT_E:float = 1.5
    CONS_CYL_SUP :float= 10
    CONS_CYL_INF:float = 8
    CONS_D:float = 8
    
    ## Début du script ##
    
    type_carburant = None
    result:float = 0
    km = check_float("Combien avez-vous parcouru de km ? ")
    while(not(type_carburant=="D" or type_carburant=="E")):
        type_carburant = input("Diesel ou Essence (D ou E) : ")
    cylindree = check_float("Quelle est la cylindrée de votre vehicule : ")
    prix_carburant = check_float("Combien coûte le carburant au litre: ")
    if(type_carburant == "E" and cylindree>LIMITE_VOLUME):
        result = (km/CONS_CYL_SUP)*SURCOUT_E*prix_carburant
    elif(type_carburant == "E" and cylindree<LIMITE_VOLUME):
        result = (km/CONS_CYL_INF)*SURCOUT_E*prix_carburant
    else:
        result = (km/CONS_D)*SURCOUT_D*prix_carburant
    return result

###############################################################################
#                                                                             #
#                        Exercice 7 : Elections législatives                  #
#                                                                             #
###############################################################################
    
def exercice7()->str:
    """ 
    Fonction qui donne le gagnant d'une election.
    
    Fonction ne prenant aucun paramètre d'entrée et renvoyant un string.
    Il est demandé à l'utilisateur de rentrer un string étant le nom des
    candidats se présentant à l'election ainsi que un float étant leur
    suffrage.
    Si il n'y a pas de gagnant, seul les candidats ayant un suffrage supérieur
    a CAP_ELIMINATOIRE seront présents au second tour. Il est alors demandé
    une seconde fois à l'utilisateur de rentrer les suffrages correspondant aux
    candidats du second tour.
    La fonction renverra finalement un string donnant le nom du gagant.
    
    Description des constantes locales:
        
    CAP_PREMIER_TOUR: correspond au pourcentage requis pour qu'un candidat soit
    élu dès le premier tour.
    CAP_ELIMINATOIRE: correspond au pourcentage requis pour qu'un candidat
    puisse participer au second tour si aucune personne n'est élue.
    NB_CANDIDATS: correspond au nombre de candidats présent à l'election.
    
    NB: Il faudrait idéalement trouver une alternative à l'utilisation de
    multiple return dans la fonction en stockant le resultat dans une
    variable et en utilisant un ou des booléens.
    """
    ## Définition des constantes locales ##
    
    CAP_PREMIER_TOUR:float = 50
    CAP_ELIMINATOIRE:float = 12.5
    NB_CANDIDATS:int = 4
    
    ## Début du script ##
    
    candidat = {} #dictionnaire regroupant les candidats en clé et leur pourcentage de vote en valeur
    eliminer = [] #liste des candidats éliminés
    leaderT1:str = None
    leaderT2:str = None
    total_vote:float = 0
    for i in range(NB_CANDIDATS):
        nom = str(input("Nom du candidat : "))
        candidat[nom] = float(input("Suffrage : "))
        total_vote += candidat[nom]
    if(total_vote != 100): #Si le nombre de vote total est incorrect:
        return("Suffrage incorrect : il n'y pas 100% de vote")   
    #Pour chaque candidat présent:
    for nom_candidat in candidat:
        if (candidat[nom_candidat]> leaderT1):
            leaderT1 = candidat[nom_candidat]
            winnerT1 = nom_candidat
        #Si il dépasse le seuil requis de victoire, il remporte l'election
        if (candidat[nom_candidat] >= CAP_PREMIER_TOUR):
            return nom_candidat
        #Si il ne dépasse pas le seuil éliminatoire, il ne sera pas retenu
        #au second tour
        elif (candidat[nom_candidat] < CAP_ELIMINATOIRE):
            eliminer.append(nom_candidat)
    for out in eliminer :
        del candidat[out]
    #On débute le second tour des elections
    for nom_candidat in candidat:
        candidat[nom_candidat] = check_float( str(nom_candidat) + " Suffrage deuxieme tour : ")
    #On vérifie de nouveau le suffrage de chaque candidat du second tour
    for nom_candidat in candidat:
        if (candidat[nom_candidat] > leaderT2):
            leaderT2 = candidat[nom_candidat]
            winnerT2 = nom_candidat
    if (winnerT1 == winnerT2) : 
        return winnerT1
    else : return("Pas de gagnant")

###############################################################################
#                                                                             #
#                    Exercice 8 : Compagnie assurance automobile              #
#                                                                             #
###############################################################################

def exercice8_temps_abo(temps:int)->int:
    """
    Fonction qui indique si le client est inscrit depuis assez longtemps
    pour profiter d'un bonus.
    
    Fonction prenant un int en paramètre d'entrée correspondant au temps
    d'abonnement et renvoyant un int correspondant au bonus du client.
    
    Description des constantes locales:
        
    TEMPS_MIN: correspond au temps necessaire pour profiter d'un bonus.
    POINT_DEFAULT: correspond au nombre de point bonus pour toute personne
    ayant un temps d'abonnement inferieur à TEMPS_MIN.
    POINT_BONUS: correspond au nombre de point bonus pour toute personne
    ayant un temps d'abonnement supérieur à TEMPS_MIN.
    """
    ## Définition des constantes locales ##
    
    TEMPS_MIN:int = 1
    POINT_DEFAULT:int = 0
    POINT_BONUS:int = 1
    
    ## Début du script ##
    
    if(temps>=TEMPS_MIN):
        return POINT_BONUS
    else : return POINT_DEFAULT

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def exercice8_main()->str:
    """
    Fonction qui demande à l'utilsateur des informations pour calculer le
    niveau de tarif de l'assurance automobile.
    
    Fonction main de l'exercice 8 ne prenant aucun paramètre d'entrée et 
    renvoyant un string.
    Il est demandé à l'utilisateur de rentrer succesivement quatre int étant
    l'age du conducteur, depuis combien de temps il possède le permis,
    le nombre d'accident qu'il a eu et son temps d'abonnement.
    La fonction renvoie un string qui décrit le tarif auquel le client est
    soumis pour son assurance.
    
    Il n'existe pas de constantes locales dans cette fonction.
    """
    ## Début du script ##
    
    age = check_int("Quelle est votre âge : ")
    temps_permis = check_int("Cela fais combien d'années que vous avez le permis : ")
    nb_accident = check_int("Combien avez vous eu d'accident : ")
    temps_abonnement = check_int("Cela fais combien d'année que vous êtes dans notre entreprise : ")
    return exercice8_prog(age, temps_permis, nb_accident, temps_abonnement)
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
def exercice8_prog(age:int, temps_permis:int, nb_accident:int,
                   temps_abonnement:int)->str:
    """
    Fonction qui calcule le niveau de tarif de l'assurance automobile.
    
    Fonction de l'exercice 8  prenant quatre paramètres d'entrée étant l'age,
    le temps de possession du permis, le nombre d'accident et le temps
    d'abonnement de l'utilisateur et renvoyant un string indiquant son tarif.
    
    Description des constantes locales:
        
    INDICE_REFUSE: correspond à la position du tarif refusé
    INDICE_ROUGE: correspond à la position de la couleur rouge dans COULEUR
    INDICE_ORANGE: correspond à la position de la couleur orange dans COULEUR
    INDICE_VERT: correspond à la position de la couleur verte dans COULEUR
    AGE_BONUS: correspond à l'age à partir duquel des changements de bonus
    sont appliqués.
    TEMPS_PERMIS_BONUS: correspond au temps requis de possession de permis pour
    obtenir un bonus?
    SEUIL_ACCIDENT_1: correspond au nombre d'accident necessaire pour avoir un
    premier malus
    SEUIL_ACCIDENT_2: correspond au nombre d'accident necessaire pour avoir un
    second malus
    COULEUR: correspond aux différents niveaux de tarif.
    """
    ## Définition des constantes locales ##
    INDICE_REFUSE:int = 0  
    INDICE_ROUGE:int=1
    INDICE_ORANGE:int=2
    INDICE_VERT:int=3
    AGE_BONUS:int = 25
    TEMPS_PERMIS_BONUS:int = 2
    SEUIL_ACCIDENT_1:int = 1
    SEUIL_ACCIDENT_2:int = 2
    COULEUR:str = ["Refusé", "Rouge", "Orange", "Vert", "bleu"]

    ## Début du script ##
    
    result:str = None
    fidelite = exercice8_temps_abo(temps_abonnement)
    if(age>=AGE_BONUS and temps_permis>=TEMPS_PERMIS_BONUS):
        if(nb_accident==SEUIL_ACCIDENT_1):
            result = COULEUR[INDICE_ORANGE+fidelite]
        elif(nb_accident>=SEUIL_ACCIDENT_2):
            result = COULEUR[INDICE_ROUGE+fidelite]
        else : 
            result = COULEUR[INDICE_VERT+fidelite]
    else :
        if((age<AGE_BONUS and temps_permis>=TEMPS_PERMIS_BONUS) or (age>=AGE_BONUS and temps_permis<TEMPS_PERMIS_BONUS)):
            if(nb_accident==SEUIL_ACCIDENT_1):
                result = COULEUR[INDICE_ROUGE+fidelite]
            elif(nb_accident>=SEUIL_ACCIDENT_2):
                result = COULEUR[INDICE_REFUSE+fidelite]
            else : 
                result = COULEUR[INDICE_ORANGE+fidelite]
        else :
            if(nb_accident>=SEUIL_ACCIDENT_1): 
                result = COULEUR[INDICE_REFUSE+fidelite]
            else : 
                result = COULEUR[INDICE_ROUGE+fidelite]
    return result

###############################################################################
#                                                                             #
#                               Fonctions de test                             #
#                                                                             #
###############################################################################
def test_atelier1_printlist()->None:
    """
    Fonction de test servant à imprimer le menu.
    
    Il n'existe pas de constantes locales dans cette fonction.
    """
    ## Début du script ##
    
    print("1-Calcul de salaire")
    print("2-Reconnaissance de caractère")
    print("3-Impôts")
    print("4-Reprographie")
    print("5-Calcul de frais portuaires")
    print("6-Concessionaire automobile")
    print("7-Elections legislatives")
    print("8-Compagnie d'assurance automobile")
    print("9-Fin du  programme")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
def test_atelier1_lancer(choice:int)->None:
    """
    Fonction de test servant à lancer une fonction choisie.
    
    Il n'existe pas de constantes locales dans cette fonction.
    """
    ## Début du script ##
    
    print("###############################################")
    if choice==1:
        print("Exercice 1: Calcul de salaire")
        print("Le salaire payé sera de :"+ str(exercice1()) +"\n")
    elif choice ==2:
        print("Exercice 2: Reconnaissance de caractère")
        print("Analyse du caractère : "+ str(exercice2()) +"\n")
    elif choice ==3:
        print("Exercice 3: Impôts")
        print("Détermination de l'imposabilité : "+ str(exercice3()) +"\n")
    elif choice ==4:
        print("Exercice 4: Reprographie")
        print("Le prix à payer pour les copies sera : "+ str(exercice4()) +"\n")
    elif choice ==5:
        print("Exercice 5: Calcul de frais portuaires")
        print(str(exercice5()) +"\n")
    elif choice ==6:
        print("Exercice 6: Concessionnaire automobile")
        print("Le coût total sera de : "+ str(exercice6()) +"\n")
    elif choice ==7:
        print("Exercice 7: Elections legislatives")
        print("Le gagnant de l'election est : "+ str(exercice7()) +"\n")
    elif choice ==8:
        print("Exercice 8:Compagnie d'assurance automobile")
        print("Niveau du tarif client : "+ str(exercice8_main()) +"\n")
    elif choice == 9:
        print("Vous avez choisi d'arrêter le programme.")
    if(choice<9):
        print("###############################################")
              
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
              
def test_atelier1()->None:
    """
    Fonction Main du programme.

    Il n'existe pas de constantes locales dans cette fonction.
    """
    ## Début du script ##
    
    choice:int = -1
    print("Atelier1 v1.1  Bonnemayre Vincent / Zampaglione Enzo\n")
    while(choice<9):
        test_atelier1_printlist()
        while(0>choice or 9<choice):
            choice = check_int("Entrez votre choix :")
        test_atelier1_lancer(choice)
        if(choice<9):
            choice = -1
    print("Fin d'execution du script.")

###############################################################################
#                                                                             #
#                                    Start                                    #
#                                                                             #
###############################################################################
    
test_atelier1()
