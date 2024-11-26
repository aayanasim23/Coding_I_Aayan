def isEven (number):

    if (number % 2) == 0:
        return(True)
    else:
        return(False)
isEven(2)

def minVal(numb1, numb2):
    if numb1 < numb2:
        return(numb1)
    else:
        return(numb2)

minVal(3, 2)


print(isEven(minVal), minVal(2,3))

