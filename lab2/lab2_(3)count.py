from collections import Counter

txt = '''
Sadok vyshnevyi kolo khaty,
Khrushchi nad vyshniamy hudut,
Pluhatari z pluhamy ydut, 
Spivaiut iduchy divchata, 
A materi vecheriat zhdut.

Semia vecheria kolo khaty, 
Vechirnia zironka vstaie. 
Dochka vecheriat podaie, 
A maty khoche nauchaty, 
Tak soloveiko ne daie.

Poklala maty kolo khaty 
Malenkykh ditochok svoikh; 
Sama zasnula kolo yikh. 
Zatykhlo vse, tilko divchata 
Ta soloveiko ne zatykh.
'''
word_list = []
for word in txt.split():
    clear_word = ""
    for letter in word:
        if letter.isalpha():
            clear_word += letter.lower()
    word_list.append(clear_word)
a = Counter(word_list)
print(a.items())
a1 = a.keys()
a2 = a.values()
print(a1)
    
