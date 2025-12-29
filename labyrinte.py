# coding : UTF-8

"""
jeux d'aventure avec des chemin,enigme et systeme de vie
"""

#module du jeu
import time
import random

#variable du jeu
vie=100
inventaire=[] # cette vas contenir les objet collecter par le joeur 
score=0
position="entree"

#cette fonction va afficher l'etat actuel du jouer
def afficher_etat(): 
    print(f"\n  vie:{vie}/100 | score:{score} | inventaire:{inventaire}")

#fonction qui retire un point
def perdre_vie(degats):
    global vie # permet de modifier la variable globale "vie"
    vie -=degats
    print(f" -{degats} point de vie ")
    if vie<=0:
        print(" MAFF , TU ES MORT! Game Over....")
        return False
    return True

#fonction qui permet d'ajouter un piont
def gagner_points(points):
    global score
    score +=points
    print(f"{points}points")

#fonction qui vas ajouter un objet dans l'inventaire
def ajouter_objet(objet):
    inventaire.append(objet)
    print(f"Tu as obtenu: {objet}")

#fonction qui vas proposer un egnime mathematique au joueur
def egnime_maths():
    print("\n \tEGNIMES MATHEMATIQUE\n j'espere que tu es fort o)o)o)")
    print("tu dois resoudre cette ignime pour avancer..")
    # Pour test, énigme fixe
    reponse_correct = 2
    question = "1+1= ? "
    
    print(f"Question: {question}")

    try:
        reponse = int(input("Ta reponse : "))

        if reponse==reponse_correct:
            print("MINCE? La reponse est correct!!! La porte s'ouvre....")
            gagner_points(20)
            return True #succes
        else:
            print(f"MOUfff!!!, La reponse est fausse. C'etait {reponse_correct}")
            return perdre_vie(15)
    except ValueError: #si l'utilisateur n'entre pas un nombre
        print("Entre un nombre!!!")
        return perdre_vie(10)

#fonction qui vas gerer un combat avec un monstre
def combat_monstre():
    print("\n UN MONSTRE APPARAIT!!")

    force_monstre= random.randint(10,30) #force aleatoire du monstre
    print(f"\n Force du monstre: {force_monstre}")

    print("\n\t Option de combat:")
    print("1) Attaquer(Risquer)")
    print("2) Esquiver (prudance)")
    print("3) Utiliser un objet\n")

    try:
        choix= int(input("Que fais tu mon petit (1-3) ?  "))
    except ValueError:
        print("\nEntrée invalide, veuillez entrer un nombre entre 1 et 3.")
        return perdre_vie(5)  # pénalité légère pour un mauvaise entree 

    if choix == 1:
        print(" \nTu attaques le monstre(c'est toi le monstre)")
        if random.random()>0.4: # 60% de chance de reussir
            degat = random.randint(20,40)
            print(f"    tu m'inflige {degat} degats")
            if degat>force_monstre:
                print("TU as vaincu le monstre")
                gagner_points(30)
                return True #victoire
            else:
                print("Le monstre contre_attaque")
                return perdre_vie(20) #defaite
        else:
            print("Tu rate ton attaque!")
            return perdre_vie(20)
    elif choix == 2:
        print(" TU tente d'esquiver gars!!!")
        if random.random()>0.3: # 70% de chance de reussir
            print(" Yess mon petit tu as  eviter le monstre!! ")
            return True # succes de l'esquive
        else:
            print(" Le monstre vas te rattraper")
            return perdre_vie(15) #echec de l'esquive
    elif choix==3:
        if "potion" in inventaire:
            print("   Tu utilise une potion!!")
            inventaire.remove("potion")
            global vie
            vie = min(100,vie+30) # donc sa te soigne sans depasser 100 
            return True #potion utilise avec succes
        else:
            print("Tu n'as pas de potion!!")
            return perdre_vie(20) #tu n'as pas de potion dans l'iventaire et du coup tu perd des point de vie
    else:
        print(" Man si tu veux tu existe , le monstre profite!!!")
        return perdre_vie(10)

#"fonction principale du jeu" 
def jeu_aventure():
    global position
    print("\t BIENVENUE DANS L'AVENTURE DU CHATEAU MYSTIQUE DU KING\n")
    print("Tu te retrouves devant un chateau mystérieux et ton objectif est de trouver le trésor légendaire du king")

    while vie>0 and score<100: # ici elle permet de faire continuer tant que le joueur es en vie et n'as pas gagner
        afficher_etat()

        if position == "entree":
            print("""
            Tu es a l'entree du chateau ,
            devant toi, trois portes
            1- [°] Porte en bois(Gauche)
            2- [*] Porte en fer (Milieu)
            3- [$] Porte dorée (Droite)
            """)
            try:
                choix = int(input("Choissez une porte :)  :"))
            except ValueError:
                print("Entrée invalide, veuillez entrer 1, 2 ou 3.")
                continue # pour retourner au debut de la boucle
            
            if choix== 1:
                print("TU ouvre la porte en bois")
                time.sleep(1) #pause de 1 seconde
                position="bibliotheque"
            elif choix==2:
                print("Tu ouvre la porte en fer...")
                time.sleep(1)
                position="salle_de_combat"
            elif choix == 3:
                print("Tu ouvre un porte doréé...")
                time.sleep(1)
                position="salle_du_tresor"
            else:
                print("MOUFF?, tu ne joue pas ?...") # le joeur reste a la meme position
        elif position == "bibliotheque":
            print("""
                    BIBLIOTHEQUE ANCIEN...
                  des vieux livre poussiereux recouvre le mur, 
                  au centre , un table avec un vieux Grimoire

            """)
            print("Que fais tu ?")
            print("1- Lire le grimoire")
            print("2- Chercher une sortie")
            print("3- Retourner à l'entrée ")
            try:
                choix = int (input(" Ton Choix :)  :"))
            except ValueError:
                print("Entrée invalide, veuillez entrer 1, 2 ou 3.")
                continue

            if choix==1:
                if egnime_maths():
                    print("\n Le grimoire revele un passage secret :)")
                    ajouter_objet("clé ancienne")
                    position="passage_secret"
                else : 
                    position="entree"
            elif choix==2:
                print("TU trouve une porte un genre un genre ...")
                position="passage_secret"
            elif choix==3:
                print("Tu retourne a l'entree")
                position="entree"
        elif position == "salle_de_combat":
            print("""SALLE D'ENTRAINEMENT
                Cette salle a été utilisée pour 
                l'entraînement des anciens gardes
                """)
            if combat_monstre():
                print("\n Apres le combat, tu trouve une potion...")
                ajouter_objet("potion")
                print("Une nouvelle porte apparait...")
                position="couloir"
            else:
                position="entree" # le joueur retourne a l'entre si le combat est perdu
        elif position == "Salle du tresor":
            print("""
                SALLE DU TRESOR
                Des piece d'or et des joyaux brillant
                sous la faible lumiere
                """)
            if "clé ancienne" in inventaire:
                print("TU utilise ta clé ancienne pour ouvrir le coffre...")
                print("FÉLICITATIONS!!! tu as trouvé le trésor !!!")
                gagner_points(100)
                break # sort de la boucle while bref marque la fin du jeu
            else:
                print("Le coffre au tresor est ferme a cle")
                print("Tu dois trouver la clé ancienne!!!")
                position="entree"

        elif position == "passage_secret":
            print("""
                PASSAGE SECRET
                Un étroit couloir éclairé par des torches
                L'air est humide et froid :) 
                """)
            print("Que fais tu ?")
            print("1- Avance prudemment")
            print("2- Revenir en arriere")
            try:
                choix= int(input("Ton choix : "))
            except ValueError:
                print("Entrée invalide, veuillez entrer 1 ou 2.")
                continue

            if choix == 1:
                print("Tu avance dans le passage")
                time.sleep(2)
                print("TU arrives dans une salle bizare!!")
                position="salle_du_tresor"
            else:
                print("Mince , tu decide faire demi-tour....:)")
                position="bibliotheque"
        elif position == "couloir":
            print("""
                LONG COULOIR
                le couloir semble sans fin.
                Des bruits etrange resonnent....

                """)

            print("Que fais tu ?")
            print("1- Courir")
            print("2- Marcher doucement")
            print("3- Attendre")
            try:
                choix= int(input("Ton choix : "))
            except ValueError:
                print("Entrée invalide, veuillez entrer 1, 2 ou 3.")
                continue

            if choix == 1:
                print("Tu cours et trébuches!!")
                perdre_vie(10)
                print("Tu te retrouves à l'entrée...")
                position="entree"
            elif choix==2:
                print("Tu passes inaperçu et découvres une porte...")
                position = "salle_du_tresor"
            else:
                print("Rien ne se pase...")#rete dans le couloir


    #fin du jeu (lorsque tu sort dda boucle)
    print("\n"+"="*50)
    print("FIN DE L'AVENTURE")  
    print(f"Score final:{score}")
    print(f"Vie restante:{vie}")
    print(f"Inventaire:{inventaire}")

    if score >=100:
        print(" TU AS GAGNÉ!! LE TRÉSOR EST À TOI ; merde....")
    else:
        print(" Mouff tu as fait de ton mieux, il faut réessayer")



jeu_aventure()