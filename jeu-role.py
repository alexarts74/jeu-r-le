from random import randint

point_vie = 50
point_vie_ennemi = 50
potions = 3
potions_recup = randint(15, 50)
attaque_ennemies = randint(5, 15)
attaque = randint(5, 10)

while point_vie > 0:

    print("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
    print(f"Vous avez", point_vie, "points de vies et ", potions,"potion(s) en main.")

    answer = input("")

    if int(answer) == 1 and point_vie_ennemi != 0:
        point_vie_ennemi = point_vie_ennemi - attaque
        print(f"Votre attaque a fait {attaque} points de dégats ")
        print(f"Il reste {point_vie_ennemi} points de vie a l'ennemi")
        point_vie = point_vie - attaque_ennemies
        print(f"L'ennemi vous a infligé {attaque_ennemies} points de dégats il te reste {point_vie} points de vie")

    elif int(answer) == 2 and potions != 0 and point_vie_ennemi != 0:
        potions -= 1
        point_vie = point_vie + potions_recup
        print(f"Vous avez", point_vie, "points de vies et ", potions,"potion(s) en main.")
        point_vie = point_vie - attaque_ennemies
        print(f"L'ennemi vous a infligé {attaque_ennemies} points de dégats il te reste {point_vie} points de vie")
