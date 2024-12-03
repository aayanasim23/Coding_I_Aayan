def isEven(number):
    if (number % 2) == 0:
        return True
    else:
        return False


def minVal(numb1, numb2):
    if numb1 < numb2:
        return numb1
    else:
        return numb2


result_minVal = minVal(2, 3)
result_isEven = isEven(result_minVal)


print(result_isEven, result_minVal)
