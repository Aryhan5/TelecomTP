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

for e in text:
    if last == e:
        counter+=1
    else:
        frequency[e] = e + " " + hex(counter) + " " + str('%.5f' % (counter/size))
        counter=1
        generalCounter += 1
    last = e

counter = 0
counter2 = 0
while len(frequency) > 0:
    try:
        orderedFreq[counter2] = frequency.pop(unsortedtext[counter])
        counter2+=1
        counter+=1
    except:
        counter += 1

print(text)

for i in range(0, len(orderedFreq)):
    print(orderedFreq[i])




