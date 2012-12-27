#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""financial1 [Startkapital] [Zinssatz p.a.] [Laufzeit in Jahren]
        -h      Diesen "Docstring"-Text anzeigen
"""

import sys

def zins(sKapital, zinssatz, laufzeit, currentYear):
    zSum = sKapital
    # Ende der Laufzeit erreicht?
    if currentYear <= laufzeit:
        # Zinsen addieren
        sKapital += (sKapital/100) * zinssatz
        print "Summe am Ende des " + str(currentYear) + ". Jahres: " + str(round(sKapital, 2)) + " Euro"
        currentYear += 1 
        return zins(sKapital, zinssatz, laufzeit, currentYear)
    return zSum

# Einstellungsparameter?
if "-h" in sys.argv:
        print __doc__
        exit()

# Startkapital
if len(sys.argv) >= 2:
        sKapital = sys.argv[1]
        print "Startkapital ist", sKapital, "Euro"
else:
        sKapital = raw_input("Startkapital in Euro eingeben: ")
sKapital = float(sKapital)

# Zinssatz
if len(sys.argv) >= 3:
        zinssatz = sys.argv[2]
        print "Zinssatz ist", zinssatz, "Prozent p.a."
else:
        zinssatz = raw_input("Zinssatz in Prozent p.a. eingeben: ")
zinssatz = float(zinssatz)

# Laufzeit
if len(sys.argv) >= 4:
        laufzeit = sys.argv[3]
        print "Laufzeit ist", laufzeit, "Jahre"
else:
        laufzeit = raw_input("Laufzeit in Jahren eingeben: ")
laufzeit = int(laufzeit)

# Berechnung
print "Summe am Ende der Laufzeit: " + str(round(zins(sKapital, zinssatz, laufzeit, 1), 2)) + " Euro"

