from collections import Counter

#завдання 1
mas1 = '''Hello world ыаыва       kjnkjkj kjn
ралоардларлд дларларорлрадл ардларлдрар 555555555555555
555'''

def caculation_space(String):
    c = 0
    for word in String.split():
        c = c + 1 
    return c
print(caculation_space(mas1))



#завдання 2
f = open('a.txt', 'r')
a =  f.read()
print(caculation_space(a))
c = 0
k = []
g = []
for line in a.splitlines():
    if(c % 2 == 1):
        k.append(line)
        k.append('\n')
    elif(c % 2 == 0):
        g.append(line)
        g.append('\n')
    c = c + 1
str1 = ''.join(k)
str2 = ''.join(g)
b1 = open('b1.txt', 'w')
b1.write(str1.upper())
b1.close()
b2 = open('b2.txt', 'w')
b2.write(str2.lower())
b2.close()
f.close()

#завдання 3
