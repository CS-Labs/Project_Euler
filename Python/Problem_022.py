# Author Christian Seely

import os

def problemTwentyTwo():
    sPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Problem_Externals', 'p22names.txt'))
    # Read in the text file and sort the names.
    with open(sPath, 'r') as oFile:
        aNames = sorted(oFile.read().replace('"', '').split(','))
    iTotalScore = 0
    aNameIndexPairs = zip(aNames, range(1, len(aNames)+1)) # (name, index)
    for sName, iIndex in aNameIndexPairs:
        iNameScore = 0
        for char in sName.lower():
            iNameScore += (ord(char) - 96) # Convert the character to index in alphabet.
        iTotalScore += (iNameScore * iIndex)

    return iTotalScore

print(problemTwentyTwo())
