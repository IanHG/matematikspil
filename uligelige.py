#!/usr/bin/python

import random 
import sys

###
# Hoved funktion
###
def main():
    running = True
    print("Tast svaerhedsgrad:")  # Skriv ud
    max_tal = int(sys.stdin.readline().rstrip())  # Tag bruger input

    while running:
        # generer tilfaeldigt tal
        tal = random.randint(0, max_tal)  # Generer et tilfaeldigt tal
        print("Er %i lige (l) eller ulige (u)? Tryk (e) for exit." % tal); 

        # loop over bruger input.
        while 1:
            linje = sys.stdin.readline().rstrip();
            if linje == "e":
                running = False
                break
            if not linje:
                continue
            # Tjek om vi har gaettet rigtigt
            if ((tal % 2 == 0) and (linje == "l")) or ((tal % 2 == 1) and (linje =="u")):
                print("Rigtig! Flot :)")
                break
            else:
                print("Forkert, proev igen!")
    
    # print en stop besked.
    print("Stopper program");

###
#
###
if __name__ == "__main__":
    main()
