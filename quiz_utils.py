# Fonctions utilitaires pour le quiz
import random

def melanger_options(bonne_reponse, autres_options, nombre_options=4):
    """Crée une liste d'options mélangées avec la bonne réponse"""
    options = [bonne_reponse]
    
    # Ajouter des options aléatoires
    options_disponibles = autres_options[:]
    random.shuffle(options_disponibles)
    
    for i in range(min(nombre_options - 1, len(options_disponibles))):
        options.append(options_disponibles[i])
    
    # Mélanger toutes les options
    random.shuffle(options)
    
    return options

def afficher_question(numero, drapeau, options):
    """Affiche une question du quiz"""
    print(f"\n{'='*50}")
    print(f"Question {numero}")
    print(f"{'='*50}")
    print(f"\nQuel pays a ce drapeau ? {drapeau}\n")
    
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    print()

def verifier_reponse(choix, options, bonne_reponse):
    """Vérifie si la réponse est correcte"""
    if choix < 1 or choix > len(options):
        return False
    
    return options[choix - 1] == bonne_reponse

def afficher_score_final(score, total):
    """Affiche le score final"""
    print(f"\n{'='*50}")
    print(f"SCORE FINAL: {score}/{total}")
    print(f"{'='*50}")
    
    pourcentage = (score / total) * 100
    
    if pourcentage == 100:
        print("🏆 PARFAIT ! Tu es un expert en drapeaux !")
    elif pourcentage >= 80:
        print("🌟 Excellent ! Très bonne connaissance des drapeaux !")
    elif pourcentage >= 60:
        print("👍 Bien joué ! Continue comme ça !")
    elif pourcentage >= 40:
        print("📚 Pas mal, mais il y a encore du travail !")
    else:
        print("💪 Continue à apprendre, tu vas progresser !")
