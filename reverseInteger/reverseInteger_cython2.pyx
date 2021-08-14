import cython
@cython.ccall
def reverseInteger(x : int) -> int:
    strValue:str = str(x)
    if x > 2**31: return 0
    if x < 0:
        return int(strValue[:0:-1])*-1
    else:
        return int(strValue[::-1])
