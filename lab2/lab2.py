import re

String = '''Hello world ghbfdf, kjnkjkj kjn'''
def caculation_space(String):
    counter = 0
    #видаляю всі знаки
    #String = re.sub('[!@#$]', '',String )
    l = len(String)
    #пробіли (початок + кінець)
    if(String[0] == ' ') and (String[l-1] == ' '):
        counter = counter - 1
    elif(String[0] == ' ') or(String[l-1] == ' '):
        counter = counter - 1

    
#пробіли (рахую їх та враховую повтори)
    for i in range (0,l):
        if(String[i-1] == String[i]) and (String[i-1] == ' ') and (String[i] == ' '):
            counter = counter
        
        elif(String[i] == ' '):
            counter = counter + 1
    
    counter = counter + 1     
    return counter



f = open('a.txt', 'r')

print(caculation_space(f.read()))
print(caculation_space(String))
print(String[20])
