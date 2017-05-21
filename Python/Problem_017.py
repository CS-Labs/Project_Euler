# Author Christian Seely

# Define mappings between numbers and words.
oByOnesDict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
oByTensDict = {
    '2': "twenty",
    '3': "thirty",
    '4': "forty",
    '5': "fifty",
    '6': "sixty",
    '7': "seventy",
    '8': "eighty",
    '9': "ninety",
}

oSpecialCaseDict = {
    '0': "ten",
    '1': "eleven",
    '2': "twelve",
    '3': "thirteen",
    '4': "fourteen",
    '5': "fifteen",
    '6': "sixteen",
    '7': "seventeen",
    '8': "eighteen",
    '9': "nineteen",
}
# Ugly brute force way...
# Works by iterating through the numbers 1 to 1000 where each number is converted to
# to the word(s) associated with its values which are then appended onto the accumulator
# sNum. During the process no spaces are added since they do not count as part of
# the character length. Once we have finished we return the length of our accumulator.
def problemSeventeen():
    sNum = ''
    for i in range(1, 1001):
        for j, c in enumerate(str(i)[::-1]):  # Iterate through the number stating at 1's place.
            if len(str(i)) == 4:
                sNum += 'onethousand'
                break
            if j == 0:
                if len(str(i)) == 2:
                    if str(i)[0] == '1' or str(i)[1] == '0':
                        continue
                    sNum += (oByOnesDict[c])
                elif len(str(i)) == 3 and (str(i)[2] == '0' or str(i)[1] == '1'):
                    continue
                else:
                    sNum += (oByOnesDict[c])
            elif j == 1:
                if len(str(i)) == 3 and str(i)[1] == '0':
                    continue
                if c == '1':
                    if len(str(i)) == 2:
                        sNum += oSpecialCaseDict[(str(i)[1])]
                    else:
                        sNum += oSpecialCaseDict[(str(i)[2])]
                else:
                    sNum += oByTensDict[c]
            elif j == 2:
                if str(i)[2] == '0' and str(i)[1] == '0':
                    sNum += oByOnesDict[c] + 'hundred'
                else:
                    sNum += oByOnesDict[c] + 'andhundred'
    return len(sNum)


print(problemSeventeen())
