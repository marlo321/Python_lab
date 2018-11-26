print("Hello world")

def division(x, y):
    if(x < 0) or  (y < 0):
        raise Exception('give positive')

    if((x%y) == 0):
        return True
    else:
        return False
    
def simple(a, b):
    lst = []
    k = 0
    if(a < 0):
        raise Exception('give positive number a')
    if(b < 0):
        raise Exception('give positive number b')
    if (a > b):
        raise Exception('give second bigger than second')
    

    for i in range(a, b+1):
        for j in range(2, i):
            if division(i,j):
                k = k + 1
        if (k == 0):
            lst.append(i)
        else:
            k = 0
    return lst

mas2=['a', ['c', 1, 3], ['f', 7, [4, ['4']]], [{'lalala': 111}]]
print(mas2)

mas3=[]

def Func3(spysok):
    for i in range(0, len(spysok)):
        if(isinstance(spysok[i], list)):
            Func3(spysok[i])
        else:
            mas3.append(spysok[i])
    return mas3




print(Func3(mas2))

        
print(division(8,4))
print(simple(1, 15))
