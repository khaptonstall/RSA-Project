# coding=utf-8
## Title: rsa.py
## Description: Cryptography RSA project that deals with exploring the tools used in RSA encryption
## Author: Kyle Haptonstall

from random import randint
from random import randrange
import inspect

########################################
######### Problem 1: Power Mod #########
########################################
def intToBinary(n):
    return bin(n)[2:]

def powerMod(num, exp, modulus):
    result = 1
    base = num % modulus
    while intToBinary(int(exp)) != '0':
        if intToBinary(exp)[-1:] == '1':
            result = (result * base) % modulus
        exp = exp >> 1
        base = (base * base) % modulus
    return result


########################################
#### Problem 2: Extended Euclidean #####
########################################
def extendedEuclidean(a,b):
    if a == 0:
        return (b, 0, 1)
    if b == 0:
        return (a, 1, 0)

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

print("Problem 2: ")
print("ExtendedGCD for (240, 46): ")
print( extendedEuclidean(240, 46))
print("ExtendedGCD for (971, 977): ")
print( extendedEuclidean(971, 977))
print()


########################################
####### Problem 3: Miller-Rabin  #######
########################################
def powerOfTwoFactor(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        d /= 2
        s += 1
    return s, d

def millerRabin(n):
    if n == 2: return True
    if n % 2 == 0 or n < 2: return False
    s, d = powerOfTwoFactor(n)
    k = 10

    for _ in xrange(k):
        a = randint(2, n - 1)
        x = powerMod(a, d, n)
        if x != 1:
            i = 0
            while x != (n - 1):
                if i == s - 1:
                    return False
                else:
                    i += 1
                    x = powerMod(x,2,n)
    return True

print("Problem 3: Miller-Rabin test.")
print("On prime 104729 = ")
print( millerRabin(104729))
print("On composite 46783912 = ")
print( millerRabin(46783912))
print()

########################################
## Problem 4: Generate 4096-bit key  ###
########################################
def randPrime(n,m):
    p = 4
    print("choosing prime")
    while millerRabin(p) == False:
        p = randrange(n, m)
    print("got prime")
    return p


def generateKey():
    ## Step 1: Choose 2 primes
    p = randPrime(2**2047 , 2**2048)
    q = randPrime(2**2047, 2**2048)
    while q == p:


    ## Step 2: Compute n = p*q
    n = p * q

    ## Step 3: Computer Euler totient
    t = (p - 1) * (q - 1)

    ## Step 4: Choose e where:
        ## 1 < e < euler(n)
        ## GCD(e, euler(n)) == 1
    e = randPrime(3,t)
    while extendedEuclidean(e, t)[0] != 1:
        e = randPrime(3,t)

    ## Step 5: Choose d
    ## Then take the first bezout coefficient mod t
    d = extendedEuclidean(e, t)[1] % t
    print("Public:")
    print(n, e)
    print("Private")
    print(n, int(d))
    c = powerMod(23,e,n)
    print(c)
    print(powerMod(c,int(d),n))
    print("Done")
    ## Return moduli n, public exp e, private exp d
    return(n,e,d)

keys = generateKey()
message = 23
c = powerMod(message, keys[1],keys[0])
m = powerMod(c,int(keys[2]),keys[0])

print("Problem 4: Keys = ")
print(keys)
print("Message = " + message)
print("Encrypted message = " + c)
print("Decrpyted message = " + m)
print()


########################################
## Problem 5: Breaking 4096-bit RSA  ###
########################################
#-Increase of 1000 years per 256-bits
#         x | y
#      -----|-----
#       768 | 1.5
#      -----|-----
#      1024 | 1,000
#      -----|-----
#      1280 | 1,000,000

# Answer: 1.5*10^39 years


########################################
####### Problem 6: Student Grade  ######
########################################
n = 17769189669575992232634159615638339924213778815802742950826319854421116745671384179192858782617500195092541524147420254359925525623320277763708202851473834662456345282290499273541946396434601554937332987306431273773536658622587641427769079644253177741780894730085202969994276000949464332485592770698765929667
e = 65537
encryptedGrade = 15382598372555542846781974555617571906087878457041650802685645434918374329782374838826025208742903800851508665141816397721683174171534217111970459666092608749037753856820588468107022470389816629167676806984485687409437746356111871222776196738336335167449947096989452963217642508480452169819932060709828270714
for i in xrange(100, 1000):
    if powerMod(i,e,n) == encryptedGrade:
        print("Problem #5: Student Grade = " + i)
        break

## Answer: 92.9
## What to do before encryption:
# Before RSA encryption, the teacher can use randomized salt variable that they
# could concatenate with the 3-digit integer value. Upon decryption,
# the student will know that the first 3-digits of the decrypted number is
# then the grade given.

########################################
######## Problem 7: RSA Moduli  ########
########################################
rsaModuli = [513706836203126403485131271471300237433254803572721841652476758567073657978919717637337634426822560021994859788128782348716111798958654276526574947670856488227319706999248888661212872350795857436007858673178239911818489143760105032711466660664411108538289881790810706588732538671284087502817551619320313190537,
415038981974124085906522625795446827259827356774059458690831493191090163052648298495391787333376203758898331541186279992790419752000394297836238751361958120699759319652229062819302411169758586640200439735033564634390571647665018146887997796216303972860536042917723959294323928570076275829250648265252911248067,
474973778066150627526166613001076492056695934364755007755778525935640650022030243665358520219065202510871558728994154628349376585228662381300854022537478646886554713895898757735764518290620071674435650065964125608135725422681397741753493130422939527795328411530475960724238086792169021573296712336095768718127,
494505508724975040428934108385202907062886162618279457818452964523719482923784832557072622561371499319315509447932327277903760619317065560960446554599186494267585001172180008256644503385422594203648913162819435988059265463317324316773049529014353261878342839145581503449167263784960225642132623081397899397353,
230656435714587384812598461262185798958068206230050402566268120599759858752633524954026325144364546256648000414431965884689565788188307842637218973578288893232670963843442343533559140391796403055643905210510131426405543069902171179083726794513713469794253332707608583127762272843422334837107293328181353155231,
302347089780517647030469745598698997509832635731085808093722370132636200849255018835281032749243467642642382609335978026953583607612605240931041912590000741665259659055820234978304487713111069485804958710705742632035194588838255997297309580578477667558886654413281124909808704154471434047845553952480206257137,
432733651433894189222670632830373632207193518509047195837180149485907236396432202557618026909681807890995547316103267728396788322220123076592907434088932456205158891106368871304519441258391797654457712045398355805490210925386140429646321323218827185748687037798667429586328208039728846560972661784493375989939,
466709294451240008611974779202732407695689249329163647500824531901177704237605599104790250868545171352710181659899863427738881567263108163026599233581314450453299550972437637866608197648027709838706495731222823258311371791877694546290572194437370688025942402777514094606018279038748822187780860623332792207477,
530135339126579884360447027397811845093741051257793921950989065280765107124312004155958175091838886900959763439167020259211585900804974258179327582456369811608071898572221150765767648286131280525062735007836971920437243800738225873600559772215475100017914270805179114686903764605346168093191739301920153002493,
351946954695229198556248040231405233968939450268137474145574103474897771821874886678323245007036344221647931637548971978291052286721760112053266290836908941351280822382606721369910864548763151132383195016742448724209443376635858372323256613813854460953094381620289016817393871819213013083946409960795397012937]


results = []


for a in rsaModuli:
    for b in rsaModuli:
        gcd = extendedEuclidean(a, b)
        if (gcd[0] > 1) & (gcd[0] != a):
            results.append((gcd[0], (a / gcd[0])))
            break

decyptionExp = []
for i in results:
    t = (i[0] - 1) * (i[1] - 1)
    e = 65537
    extgcd = extendedEuclidean(e,t)
    d = extgcd[1]
    d = d % t
    decyptionExp.append(d)

print("Problem #6: Printing decryption exponents: ")
print(decyptionExp)
