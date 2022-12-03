def count(inputdata, rank):
    """Process the data file and return the calories"""

    return sorted((sum(int(line) for line in lines.split('\n'))) for lines in inputdata.strip().split('\n\n'))[-rank-1]


with open('prodinput.txt') as f:
    dataFile = f.read()
    print(count(dataFile, 0))
