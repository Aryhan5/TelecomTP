import operator
#vive git

f = open("input.txt", 'r')
g = open("output.txt", 'w')
unsortedtext = (''.join(list(f.read())))
f.close()
f = open("input.txt", 'r')
text = (''.join(sorted(list(f.read()))))


outtext = ""
frequency = {}
orderedFreq = {}

generalCounter = 0
counter = 1
size = len(text)

last = ''
g.write(text)

#compter les frequences
for e in text:
    if last == e:
        counter+=1
    else:
        frequency[last] = counter/size
        counter=1
        generalCounter += 1
    last = e

#tri par valeur
frequency_sorted = sorted(frequency.items(), key=operator.itemgetter(1))
frequency_sorted.reverse()
frequency_sorted = {key: value for (key, value) in frequency_sorted}

#Code de Shannon-Fano

def Shannon_Fano(occ, code={}, max=1):
    #liste des clés
    keys = []

    #Creation du dictionaire de valeurs
    for key in occ.keys():
        if max == 1:
            code[key] = ""
        keys.append(key)

    if len(occ) == 2:
        code[keys[0]] += '0'
        code[keys[1]] += '1'
        return code

    elif len(occ) == 1:
        code[keys[0]] += '0'
        return code

    else: #Appel récursif

        somme = 0
        mid = False
        first = {}
        first_c = {}
        second = {}
        second_c = {}

        counter = 0

        for i in range(0, len(occ)):
            if not mid:
                code[keys[i]] += '0'
                somme += occ[keys[i]]
                first[keys[i]] = occ[keys[i]]
                first_c[keys[i]] = code[keys[i]]
            else:
                code[keys[i]] += '1'
                second[keys[i]] = occ[keys[i]]
                second_c[keys[i]] = code[keys[i]]

            if not mid:
                if i == len(keys)-2:
                    mid = True
                    first = Shannon_Fano(first, first_c, somme)
                elif (abs(max*0.5-somme)) < abs(max*0.5-(somme+occ[keys[i+1]])): #Si cet élément est plus proche de la moitié que le suivant
                    mid = True
                    first = Shannon_Fano(first, first_c, somme)


            counter += 1
        second = Shannon_Fano(second, second_c, (max-somme))
        first.update(second)
        return first

SF_Code = Shannon_Fano(frequency_sorted)
for key, value in SF_Code.items():
    if(len(key) == 0): #prendre en compte les caractères nulr
        print(key + " " + hex(0) + " " + value)
    else:
        print(key+" "+hex(ord(key))+" "+value)