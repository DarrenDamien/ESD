################################################################################
#@Calculatice
#@02/01/2017
#@Negouai Darren
################################################################################

#Module Import

#Fontions et variables

#Body du code

print "Bonjour Ordinateur"

entree1 = int(raw_input("Tapez le Premier Chiffre: "))
entree2 = int(raw_input("Tapez le Second Chiffre: "))
operateur = raw_input("Tapez l'operateur: ")
resultat = 0


if operateur == "+":
    resultat = entree1 + entree2

elif operateur == "-":
    resultat = entree1 - entree2

elif operateur =="*":
    resultat = entree1 * entree2

elif operateur =="/":
    resultat = entree1 / entree2

print resultat