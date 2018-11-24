import operator
import math

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

#compter les fréquences
for e in text:
    if last == e:
        counter+=1
    else:
        frequency[last] = counter
        counter=1
        generalCounter += 1
    last = e

#tri par valeur
frequency_sorted = sorted(frequency.items(), key=operator.itemgetter(1))
frequency_sorted.reverse()

#Print de la valeur en hexa
for key, value in frequency_sorted:
    print(str(key)+ " "+hex(value) + " " + str("%.5f" % (value/len(unsortedtext))))

#Calcul de l'entropie
entropie = 0;

for key, value in frequency_sorted:
    entropie -= value/len(unsortedtext)*math.log2(value/len(unsortedtext))

#Calcul de la quantité de décision

quant_decision = math.log2(len(frequency_sorted))

#Calcul de la redondance

redo = quant_decision - entropie

#Compression maximale

compression_max = entropie/8

#Afficher ces valeurs
print("L\'entropie est de", entropie)
print("La redondance est de", redo)
print("Le taux de compression maximale est de", compression_max)


