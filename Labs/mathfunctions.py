def isEven(number):
    try:    
        if (number % 2) == 0:
            return True
        else:
            return False
    except:
        print("Give me a integer please!")



def minVal(numb1, numb2):
    try:
        if numb1 < numb2:
            return numb1
        else:
            return numb2
    except:
        print("Give me a integer please!")


result_minVal = minVal(2, 3)
result_isEven = isEven(result_minVal)


print(result_isEven, result_minVal)
