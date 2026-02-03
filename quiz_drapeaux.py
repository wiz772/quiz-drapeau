# Jeu Quiz sur les Drapeaux
import random
from drapeaux_data import pays, drapeaux
from quiz_utils import melanger_options, afficher_question, verifier_reponse, afficher_score_final

def jouer_quiz(nombre_questions=10):
    """Lance le quiz sur les drapeaux"""
    print("🎮 BIENVENUE AU QUIZ DES DRAPEAUX 🎮")
    print("\nDevine le pays correspondant à chaque drapeau !\n")
    
    # Vérifier le nombre de questions
    if nombre_questions > len(pays):
        nombre_questions = len(pays)
    
    # Créer une liste d'indices mélangés
    indices = list(range(len(pays)))
    random.shuffle(indices)
    
    score = 0
    
    # Boucle pour chaque question
    for i in range(nombre_questions):
        index = indices[i]
        drapeau_actuel = drapeaux[index]
        pays_actuel = pays[index]
        
        # Créer les autres options (tous les pays sauf le bon)
        autres_pays = []
        for j in range(len(pays)):
            if j != index:
                autres_pays.append(pays[j])
        
        # Créer les options mélangées
        options = melanger_options(pays_actuel, autres_pays)
        
        # Afficher la question
        afficher_question(i + 1, drapeau_actuel, options)
        
        # Obtenir la réponse du joueur
        reponse_valide = False
        while not reponse_valide:
            try:
                choix = int(input("Votre réponse (numéro): "))
                reponse_valide = True
            except ValueError:
                print("❌ Erreur ! Entrez un numéro valide.")
        
        # Vérifier la réponse
        if verifier_reponse(choix, options, pays_actuel):
            print("✅ Correct !")
            score += 1
        else:
            print(f"❌ Faux ! La bonne réponse était: {pays_actuel}")
    
    # Afficher le score final
    afficher_score_final(score, nombre_questions)

def menu_principal():
    """Menu principal du jeu"""
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL")
        print("="*50)
        print("1. Jouer (10 questions)")
        print("2. Jouer (5 questions)")
        print("3. Jouer (toutes les questions)")
        print("4. Quitter")
        
        try:
            choix = int(input("\nVotre choix: "))
            
            if choix == 1:
                jouer_quiz(10)
            elif choix == 2:
                jouer_quiz(5)
            elif choix == 3:
                jouer_quiz(len(pays))
            elif choix == 4:
                print("\n👋 Merci d'avoir joué ! À bientôt !")
                break
            else:
                print("❌ Choix invalide ! Choisissez entre 1 et 4.")
        except ValueError:
            print("❌ Erreur ! Entrez un numéro valide.")

if __name__ == "__main__":
    menu_principal()
