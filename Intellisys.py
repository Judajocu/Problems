from dataclasses import dataclass
import operator
import itertools

Letters = list()

@dataclass
class pairT:
  first: str
  second: str

@dataclass()
class pairT:
    first: str
    second: str

@dataclass(order=True)
class entryT():
    lastName: str
    firstName: str
    phoneNumber: str

@dataclass()
class pointT:
    x: int
    y: int

@dataclass()
class cityT:
    name: str
    coordinates: pointT

def Map(x,y):
    CityList = []
    point = pointT(int(x),int(y))
    CityList.append(cityT("Stgo", pointT(1, 2)))
    CityList.append(cityT("Rdgz", pointT(2, 2)))
    CityList.append(cityT("Janico", pointT(5, 2)))
    CityList.append(cityT("SD", pointT(1, 7)))
    CityList.append(cityT("HK", pointT(18, 2)))
    CityList.append(cityT("Pop", pointT(13, 72)))
    for item in CityList:
        if  item.coordinates == point:
            print(item.name)
            Caller()

    Caller()

def Caller():
    print("Menu")
    print("1.Look for a city")
    print("2.Exit")
    a = int(input("Select an option "))
    if a == 1:
        x,y = input("Input the coordinates:").split()
        Map(x,y)
    else:
        return 0

def  caseInsensitive():
    entryTList = []
    entryTList.append(entryT("Perez","Carlos","8092315687"))
    entryTList.append(entryT("Rodrigyes", "Loki", "8095681234"))
    entryTList.append(entryT("Crasg", "JOshy", "8099456845"))
    entryTList.append(entryT("Crasg", "josha", "8099456845"))
    entryTList.append(entryT("Lantigua", "Oka", "8095714682"))
    entryTList.append(entryT("Veras", "Anna", "8093671864"))
    entryTList.append(entryT("Santos", "Osadwq", "80903708551"))
    entryTList.append(entryT("Lora", "Las", "8092510370"))
    for i in range(entryTList.__len__()):
        entryTList[i].lastName = entryTList[i].lastName.lower()
        entryTList[i].firstName = entryTList[i].firstName.lower()
    #entryTList.sort(key=lambda x: x.lastName)
    b =sorted(entryTList,key=operator.attrgetter('lastName','firstName','phoneNumber'))
    print(b, sep='/n')


def PairCmpFn(pair1, pair2):
    if pair1 == pair2:
        print(True)
    else:
        print(False)


def Cartesian():
    one = ["A", "B", "C"]
    two = ["X", "Y", "W", "Y"]
    c = []
    for item in one:
        for part in two:
            c.append(pairT(item, part))
    print(c)
    PairCmpFn(c[0], c[1])


def Cannonbal(height):
    if height == 1:
        return 1
    else:
        return Cannonbal(height - 1) + height


def ReverseString(string):
    c = string[::-1]
    print(c)


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    print(a)


def checking(target, weights, size):
    if (size == len(weights) + 1):
        return False
    k = False
    for t in itertools.combinations(weights, size):
        if (sum(t) == target):
            print(t)
            k = True
    if k == False:
        size = size + 1
        return checking(target, weights, size)
    elif k == True:
        return True


def IsMeasurable(target, weights):
    return checking(target, weights, 1)


def ListMnemonics(string):

    CombinationGetter("", string)

def CombinationGetter(prefix, number):
    if len(number) == 0:
        Letters.append(prefix)
    else:
        options = Combinations(number[0])
        for i  in options:
            CombinationGetter(prefix + i, number[1:])

def Combinations(ch):
    if ch == '0':
        return '0'
    elif ch == '1':
        return '1'
    elif ch == '2':
        return 'ABC'
    elif ch == '3':
        return 'DEF'
    elif ch == '4':
        return 'GHI'
    elif ch == '5':
        return 'JKL'
    elif ch == '6':
        return 'MNO'
    elif ch == '7':
        return 'PRS'
    elif ch == '8':
        return 'TUV'
    elif ch == '9':
        return 'WXY'
    else:
        Ilegal()

def Ilegal():
    print("Inalid input")
    return 0

def  caseSensitive():
    entryTList = []
    entryTList.append(entryT("Perez","Carlos","8092315687"))
    entryTList.append(entryT("Rodrigyes", "Loki", "8095681234"))
    entryTList.append(entryT("Crasg", "josha", "8099456845"))
    entryTList.append(entryT("Crasg", "josha", "8099457845"))
    entryTList.append(entryT("Lantigua", "Oka", "8095714682"))
    entryTList.append(entryT("Veras", "Anna", "8093671864"))
    entryTList.append(entryT("Santos", "Osadwq", "80903708551"))
    entryTList.append(entryT("Lora", "Las", "8092510370"))
    #entryTList.sort(key=lambda x: x.lastName)
    b =sorted(entryTList,key=operator.attrgetter('lastName','firstName'))
    print(b, sep='/n')

if __name__ == '__main__':
    #First problem
    #caseSensitive()
    #caseInsensitive()

    #Second problem
    #Caller()

    #Third problem
    # Cartesian()

    #Fourth problem
    # c = Cannonbal(4)
    # print(c)

    #Fifth problem
    # ReverseString("hola world")

    #Sixth problem
    # gcd(42,12)

    #Seventh problem
    # lista = list()
    # lista = [2,5,3,8,4]
    # d = IsMeasurable(23,lista)

    #Eighth problem
    ListMnemonics("70233")
    print(Letters)