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


with open('prodinput.txt') as f:
    prodData = f.read()
    print(process_rucksack(prodData))
