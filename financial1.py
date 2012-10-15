# !/bin/python

def zins(sKapital, zinssatz, laufzeit, currentYear):
    zSum = sKapital
    # Ende der Laufzeit erreicht?
    if currentYear <= laufzeit:
        # Zinsen addieren
        sKapital += (sKapital/100) * zinssatz
        print "Summe am Ende des " + str(currentYear) + ". Jahres: " + str(round(sKapital, 2)) + " Euro"
        currentYear += 1 
        return zins(sKapital, zinssatz, laufzeit, currentYear)
    return str(zSum)

sKapital = float(raw_input("Startkapital in Euro eingeben: "))
zinssatz = float(raw_input("Zinssatz in Prozent p.a. eingeben: "))
laufzeit = int(raw_input("Laufzeit in Jahren eingeben: "))

print "Summe am Ende der Laufzeit: " + zins(sKapital, zinssatz, laufzeit, 1) + " Euro"

