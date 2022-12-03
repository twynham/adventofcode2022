def process_rucksack(inputdata):
    total = 0
    for lines in inputdata.split('\n'):
        midpoint = int(len(lines)/2)
        compartmentA = lines[0:midpoint]
        compartmentB = lines[midpoint:midpoint*2]
        found = ""
        for i in range(midpoint):
            if compartmentB.find(compartmentA[i]) > -1:
                found = compartmentA[i]
        priority = ord(found) - 96
        if priority < 0:
            priority = ord(found) - 38
        total += priority
    return total


def process_groupings(inputdata):
    total = 0
    lineno = 1
    line1 = ""
    line2 = ""
    line3 = ""
    for lines in inputdata.split('\n'):
        if (lineno + 2)%3 == 0:
            line1 = lines
        if (lineno + 1)%3 == 0:
            line2 = lines
        if lineno%3 == 0:
            line3 = lines
            found = ""
            foundin2 = ""
            for i in range(len(line1)):
                if line2.find(line1[i]) > -1:
                    foundin2 = foundin2 + line1[i]
            for i in range(len(foundin2)):
                if line3.find(foundin2[i]) > -1:
                    found = foundin2[i]
            priority = ord(found) - 96
            if priority < 0:
                priority = ord(found) - 38
            total += priority

        lineno += 1
    return total


with open('prodinput.txt') as f:
    prodData = f.read()
    print(process_rucksack(prodData))
    print(process_groupings(prodData))
