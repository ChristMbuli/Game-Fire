import random

def choice_attack():
    print("Choisissez votre attaque :")
    print("1. Arme (5 points de dégâts )")
    print("2. Épée (3 points de dégâts)")
    print("3. Bouclier (protection)")


def start_game():
    life_Gamer = 20
    life_PC = 20
    protection = 2

    print("\t\t\t\t\t\t\t\tBienvenue dans le jeu de rôle !")
    print("\t\t\t\t\t\t\t\t********************************")
    
    while life_Gamer > 0 and life_PC > 0 :
        print(f"Vie du Joueur : {life_Gamer}")
        print(f"Vie de l'Ordinateur : {life_PC}")

        choice_attack()
        choice = input("Entrez votre choix (1, 2 ou 3) : ")

        if choice == '1':
            life_PC -= 5
            print("Vous avez utilisé l'arme ! L'ordinateur perd 5 points de vie.")
            print(f"Total vie PC : {life_PC}")
        elif choice == '2':
            life_PC -= 3
            print("Vous avez utilisé l'épée ! L'ordinateur perd 3 points de vie.")
            print(f"Total vie PC : {life_PC}")
        elif choice == '3':
            if protection > 0:
                protection -= 1
                print(f"Vous avez activé le bouclier ! Boucliers restants : {protection}")
            else:
                print("Vous n'avez plus de boucliers disponibles !")
        else:
            print("Choix invalide. Vous perdez votre tour.")
        
        
        if life_PC <= 0:
            break

        attack_PC = random.randint(3, 7)

        if choice != '3' or protection == 0:
            life_Gamer -= attack_PC
            print(f"L'ordinateur vous inflige {attack_PC} points de dégâts.")
        else:
            print("Votre bouclier a bloqué l'attaque de l'ordinateur !")
        

            
    if life_PC <= 0:
        print(f"\nL'ordinateur a gagné ! avec une vie {life_PC}")
    else:
        print("\nFélicitations ! Vous avez vaincu l'ordinateur !")

       

start_game()



