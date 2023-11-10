from random import randint

life = 50
life_ennemi = 50

while life != 0 and life_ennemi != 0:

    attaque = randint(1, 10)
    attaque_ennemi = randint(1, 10)
    potion_effect = randint (1, 15)
    potion = 3


    print("\n")
    print("tu as", life, "points de vie et", potion, "potions")
    print("\n")
    print ("quel est ton choix ? (1 - attaque ; 2 - potion)")
    choix_utilisateur = input("")
    print("\n")

    if int(choix_utilisateur) == 1:
        print("tu as lancé un sort magique qui a infligé", attaque,"dégats à l'ennemi")
        life_ennemi -= attaque
        print("ennemi lui reste", life_ennemi, "points de vie")
        print("attaque ennemi est de", attaque_ennemi)
        life -= attaque_ennemi
        print("il te reste", life, "points de vie")

    elif int(choix_utilisateur) == 2 and potion > 0:
        print("tu as utilisé une potion pour récupérer", potion_effect,"points de vie")
        life += potion_effect
        potion -= 1
        print("avec la potion il te reste", life, "points de vie car tu as pris une potion de", potion, "points")

    if life <= 0 or life_ennemi <= 0:
        print("le jeu est terminé")
