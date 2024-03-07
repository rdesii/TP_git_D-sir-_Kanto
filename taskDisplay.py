def charger_liste():
    print("Chargement de la liste de tâches...")

def creer_liste():
    print("Création d'une nouvelle liste de tâches...")

def main():
    print("Bienvenue dans le gestionnaire de tâches!")

    while True:
        print("\nQue souhaitez-vous faire?")
        print("1. Charger une liste de tâches")
        print("2. Créer une nouvelle liste de tâches")
        print("3. Quitter")

        choix = input("Entrez le numéro de votre choix: ")

        if choix == "1":
            charger_liste()
        elif choix == "2":
            creer_liste()
        elif choix == "3":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

if __name__ == "__main__":
    main()
