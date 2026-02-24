def calculate_confidence_mastered(confidence_mastered: float, isCorrect: bool):
    pK = confidence_mastered
    pT = 0.01
    pS = 0.3
    pG = 0.55
    pL: float
    if (isCorrect):
        pL = (pK*(1-pS)) / ( (pK*(1-pS)) + ((1-pK)*(pG)) )

    else:
        pL = (pK*(pS)) / ( (pK*(pS)) + ((1-pK)*(1-pG)) )

    pLn = ( pL + ((1-pL)*pT) )    
    return pLn
