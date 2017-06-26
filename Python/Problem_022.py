# Author Christian Seely

def problemTwentyTwo():
    # Read in the text file and sort the names.
    with open('C:\\Users\\Christian\\Desktop\\p022_names.txt', 'r') as oFile:
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
