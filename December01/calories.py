def count(inputdata, rank):
    """Process the data file and return the calories"""

    count = 0
    counts = []
    for lines in inputdata.split('\n\n'):

        for line in lines.split('\n'):
            count += int(line)

        counts.append(count)
        count = 0

    counts.sort(reverse=True)

    return counts[rank]


with open('prodinput.txt') as f:
    dataFile = f.read()
    print (count(dataFile, 0))
