#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""financial1 [Startkapital] [Zinssatz p.a.] [Laufzeit in Jahren]
        -h      help, diesen "Docstring"-Text anzeigen
        -o      output, Werte in Datei schreiben
"""

import sys

# Ermittelte Werte als Datei (raus)schreiben? als boolean
fileOutput = False

def zins(sKapital, zinssatz, laufzeit, currentYear, fileHandle):
    # Ende der Laufzeit erreicht?
    if currentYear > laufzeit:
        return sKapital
    # Zinsen addieren
    sKapital += (sKapital/100) * zinssatz
    if fileHandle != None:
        fileHandle.write(str(currentYear)+" "+str(sKapital)+"\n")
    print "Summe am Ende des " + str(currentYear) + ". Jahres: " + str(round(sKapital, 2)) + " Euro"
    return zins(sKapital, zinssatz, laufzeit, 1+currentYear, fileHandle)

# Einstellungsparameter?
if "-h" in sys.argv:
    """Hilfetext anzeigen"""
    print __doc__
    sys.exit()

if "-o" in sys.argv:
    """Ermittelte Werte als Datei (raus)schreiben"""
    fileOutput = True

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
if fileOutput:
    datfile = open(str(zinssatz)+"pa.dat", "w") # new file
else:
    datfile = None

print "Summe am Ende der Laufzeit: " + str(round(zins(sKapital, zinssatz, laufzeit, 1, fileHandle=datfile), 2)) + " Euro"

if fileOutput:
    datfile.close()

