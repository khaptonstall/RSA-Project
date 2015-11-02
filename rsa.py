# coding=utf-8
## Title: rsa.py
## Description: Cryptography RSA project that deals with exploring the tools used in RSA encryption
## Author: Kyle Haptonstall



def intToBinary(n):
    return bin(n)[2:]

def powerMod(num, exp, modulus):
    result = 1
    base = num % modulus
    while intToBinary(exp) != '0':
        if intToBinary(exp)[-1:] == '1':
            result = (result * base) % modulus
        exp = exp >> 1
        base = (base * base) % modulus
    return result

print(powerMod(2,6543643253245234,55))

def extendedEuclidean(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    ## sList/tList will hold Bézout coefficients
    sList = [1,0]
    tList = [0,1]
    ## qList/rList will hold quotients and remainders, respectively
    qList = []
    rList = [a,b]
    i = 2
    while rList[i - 1] != 0:
        q = rList[i - 2] / rList[i - 1]
        r = rList[i - 2] - (q * rList[i - 1])
        s = sList[i - 2] - q * sList[i - 1]
        t = tList[i - 2] - q * tList[i - 1]

        qList.append(q)
        rList.append(r)
        sList.append(s)
        tList.append(t)
        i += 1
    return (rList[len(rList) - 2], sList[len(sList) - 2], tList[len(tList) - 2])

print(extendedEuclidean(240, 46))
