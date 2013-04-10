#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""financial1 [Startkapital] [Zinssatz p.a.] [Laufzeit in Jahren]
    -h    help, diesen "Docstring"-Text anzeigen
    -o    output, Werte als Datei (raus)schreiben
    -p    plot, (vorher mit -o generierte) *.dat Dateien zur Darstellung an gnuplot weiterreichen

Beispiel der Anlage von 5 Euro bei 2 bzw 3 Prozent Zinsen auf 50 Jahre:
$ ./financial1.py 5 2 50 -o
$ ./financial1.py 5 3 50 -o
$ ./financial1.py -p
"""

import sys

# Ermittelte Werte als Datei (raus)schreiben? als boolean
isFileOutput = False

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
    isFileOutput = True

if "-p" in sys.argv:
    """plot, *.dat Dateien zur Darstellung an gnuplot weiterreichen"""
    # Seek dat files
    import glob
    datFiles = glob.glob("*.dat")
    if 0 == len(datFiles):
        print "Fehler: Keine dat Dateien gefunden"
        sys.exit()
    # Form plot command
    plotCommand = "" # '5.0pa.dat' with line, '6.0pa.dat' with line
    for i, f in enumerate(datFiles):
        if 0 == i: # first iteration
            plotCommand += "echo \"plot '"+f+"' with line "
            if len(datFiles)-1 == i: # first is also last iteration?
                plotCommand += '" | gnuplot -persist'
            else:
                plotCommand += ", "
        elif len(datFiles)-1 == i: # last iteration
            plotCommand += "'"+f+"' with line "+'" | gnuplot -persist'
        else: # middle iteration/s
            plotCommand += "'"+f+"' with line, "
    #print "plot command is >>"+plotCommand+"<<"
    # Execute plot command
    import os
    os.system(plotCommand)
    sys.exit()

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
if isFileOutput:
    datfile = open(str(zinssatz)+"pa.dat", "w") # new file
else:
    datfile = None

print "Summe am Ende der Laufzeit: " + str(round(zins(sKapital, zinssatz, laufzeit, 1, fileHandle=datfile), 2)) + " Euro"

if isFileOutput:
    datfile.close()

