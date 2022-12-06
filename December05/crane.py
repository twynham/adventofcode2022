class Exercise:
    def processFile(inputFile):
        return "A"

with open('prodinput.txt') as f:
    prodData = f.read()
    print(Exercise.processFile(prodData))
