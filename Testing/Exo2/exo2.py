def reaction(v):
    return round(v/3.6)

def freinage(v, isWet):
    if isWet:
        return round(((v**2)/200)*2)
    
    return round((v**2)/200)

def distanceDarret(v, isWet):
    return reaction(v) + freinage(v, isWet)

def verifierSiPossibleDeSarreter(v, d, isWet):
    return distanceDarret(v, isWet) < d

