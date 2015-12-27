#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

print("Willkommen zum Roulette")
name = input("Wie heißen Sie? ")
wolle_spiele = input("Hallo {}. Wollen Sie wirklich Roulette spielen? (ja/nein) ".format(name))

if wolle_spiele == "nein":
    print("Schade. Exit.")
    exit(0)

games = [ "Rot oder schwarz", "Gerade oder ungerade", "Plein" ]
print("Worauf möchten Sie setzen?")
print("(1) {}".format(games[0]))
print("(2) {}".format(games[1]))
print("(3) {}".format(games[2]))
game_num = int(input("Wählen Sie 1, 2 oder 3: "))

choice = None

if game_num == 1:
    choice = input("(R)ot oder (S)chwarz? ").lower().strip()

    if choice == 'r':
        choice = "Rot"
    else:
        choice = "Schwarz"

elif game_num == 2:
    choice = input("(G)erade oder (U)ungerade? ").lower().strip()
    if choice == 'g':
        choice = "Gerade"
    else:
        choice = "Ungerade"

elif game_num == 3:
    choice = int(input("0..36? "))

else:
    print("Falsche Auswahl. Exit.")
    exit(0)


money_einsatz = int(input("Wieviele Geldeinheiten möchten Sie setzen? "))

print("Liebe(r) {}. Sie haben {} Geldeinheiten auf {} gesetzt. Rien ne va plus!".format(name, money_einsatz, choice))
print("Der Kessel dreht sich............")
print("Der Kessel dreht sich.........")
print("Der Kessel dreht sich......")
print("Der Kessel dreht sich...")

kugel = random.randint(0, 36)
print("Der Kessel stoppt: {}".format(kugel))

rot = [ 32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3 ]
schwarz = [ 15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26 ]
# print(sorted(rot + schwarz))

money_back = 0

if game_num == 1:
    if kugel in rot     and choice == "Rot" or \
       kugel in schwarz and choice == "Schwarz":
        money_back = money_einsatz * 2

elif game_num == 2:
    if kugel % 2 == 0 and choice == "Gerade" or \
       kugel % 2 == 1 and choice == "Ungerade":
        money_back = money_einsatz * 2

elif game_num == 3:
    if kugel == choice:
        money_back = money_einsatz * 36

if money_back == 0:
    print("LEIDER nichts gewonnen.")
else:
    print("GEWONNEN und zwar {} Geldeinheiten. Super. Weiter so.".format(money_back))
