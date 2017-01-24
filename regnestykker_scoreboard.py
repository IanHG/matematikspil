#!/usr/bin/python

import random 
import sys

######
# Generer og loop over regnestykker
######
def generer_regnestykker(max_tal, operator):
    # loop over regnestykker
    running = True
    while running:
        # generer tilfaeldigt regnestykke
        tal1 = random.randint(0, max_tal)
        tal2 = random.randint(0, max_tal)
        expression = str(tal1) + " " + random.choice(operator) + " " + str(tal2)
        print(expression + " = ?    (Tryk (e) for exit).")

        # loop over bruger input.
        while 1:
            linje = sys.stdin.readline().rstrip();
            if not linje:
                continue
            if linje == "e":
                running = False
                break
            # Tjek om vi har regnet rigtigt
            if int(linje) == eval(expression):
                print("Rigtig! Flot :)")
                break
            else:
                print("Forkert, proev igen!")

###
# Hoved funktion
###
def main():
    # Bed om svaerhedsgrad af regnestykker
    print("Tast svaerhedsgrad (1, 2, eller 3) :")
    grad = int(sys.stdin.readline().rstrip())
    if grad == 1:
        max_tal = 5
        operator = ["+"]
    elif grad == 2:
        max_tal = 10
        operator = ["+", "-"]
    elif grad == 3:
        max_tal = 10
        operator = ["+", "-", "*"]
    else:
        print("Hemmelig svaerhedsgrad")
        max_tal = 100
        operator = ["+", "-", "*"]
    
    # Kald funktion der genererer regnestykker
    generer_regnestykker(max_tal, operator);
    
    # print en stop besked.
    print("Stopper program");

###
#
###
if __name__ == "__main__":
    main()
