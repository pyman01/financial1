# !/bin/python

print "Startkapital in euro eingeben:"
sKapital = raw_input()

print "Zinssatz in Prozent (z.B. 5) eingeben:"
zinssatz = raw_input()

print "Laufzeit in Jahren eingeben:"
laufzeit = raw_input()

def zins(sKapital, zinssatz, laufzeit, currentYear):
    zSum = sKapital 
    if currentYear <= laufzeit:
        sKapital += (sKapital/100) * zinssatz
        currentYear += 1 
        #print "Jahr: " + str(currentYear) + " " + str(sKapital) + " euro"
        return zins(sKapital, zinssatz, laufzeit, currentYear)
    return zSum

print int(zins(float(sKapital), int(zinssatz), int(laufzeit), 1))

