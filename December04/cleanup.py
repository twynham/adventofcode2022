def process(inputdata):
    total = 0
    checkline = 0
    for line in inputdata.split('\n'):
        checkline += 1
        print (checkline)
        valueranges = line.split(',')
        firstelfrange = valueranges[0].split('-')
        secondelfrange = valueranges[1].split('-')
        firstelfmin = int(firstelfrange[0])
        firstelfmax = int(firstelfrange[1])
        secondelfmin = int(secondelfrange[0])
        secondelfmax = int(secondelfrange[1])
        if (firstelfmin >= secondelfmin and firstelfmax <= secondelfmax)\
            or (secondelfmin >= firstelfmin and secondelfmax <= firstelfmax):
            total += 1
            print (firstelfmin)
            print (firstelfmax)
            print (secondelfmin)
            print (secondelfmax)
            print (str(total) + " found on line: " + line)

    return total


def processoverlap(inputdata):
    total = 0
    checkline = 0
    for line in inputdata.split('\n'):
        checkline += 1
        print (checkline)
        valueranges = line.split(',')
        firstelfrange = valueranges[0].split('-')
        secondelfrange = valueranges[1].split('-')
        firstelfmin = int(firstelfrange[0])
        firstelfmax = int(firstelfrange[1])
        secondelfmin = int(secondelfrange[0])
        secondelfmax = int(secondelfrange[1])
        if (firstelfmin <= secondelfmin and firstelfmax >= secondelfmin)\
            or (firstelfmin <= secondelfmax and firstelfmax >= secondelfmax) \
            or (secondelfmin <= firstelfmin and secondelfmax >= firstelfmin) \
            or (secondelfmin <= firstelfmax and secondelfmax >= firstelfmax):
            total += 1
            print (firstelfmin)
            print (firstelfmax)
            print (secondelfmin)
            print (secondelfmax)
            print (str(total) + " found on line: " + line)

    return total

with open('prodinput.txt') as f:
    prodData = f.read()
    print(process(prodData))
    print(processoverlap(prodData))