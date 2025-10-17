def is_fib_like(aList):
    if len(aList) < 3:
        return True
    else:
        for i in range(3, len(aList)):
            if aList[i] != aList[i - 2] + aList[i - 1]:
                return False
        return True
    
sample = [2, 1, 3, 4, 7, 11, 18, 29]


    
print(is_fib_like(sample))
