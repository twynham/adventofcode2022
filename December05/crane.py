class Exercise:
    def __init__(self, inputFile):
        self.inputData = inputFile
        self.stacks = [[], [], [], [], [], [], [], [], [], [], []]


    def readData(self):
        for line in self.inputData.split('\n'):
            if line.find('[') != -1:
                if line[1:2] != ' ' and line[1:2] != '':
                    self.stacks[1].append(line[1:2])
                if line[5:6] != ' ' and line[5:6] != '':
                    self.stacks[2].append(line[5:6])
                if line[9:10] != ' ' and line[9:10] != '':
                    self.stacks[3].append(line[9:10])
                if line[13:14] != ' ' and line[13:14] != '':
                    self.stacks[4].append(line[13:14])
                if line[17:18] != ' ' and line[17:18] != '':
                    self.stacks[5].append(line[17:18])
                if line[21:22] != ' ' and line[21:22] != '':
                    self.stacks[6].append(line[21:22])
                if line[25:26] != ' ' and line[25:26] != '':
                    self.stacks[7].append(line[25:26])
                if line[29:30] != ' ' and line[29:30] != '':
                    self.stacks[8].append(line[29:30])
                if line[33:34] != ' ' and line[33:34] != '':
                    self.stacks[9].append(line[33:34])
                if line[37:38] != ' ' and line[37:38] != '':
                    self.stacks[10].append(line[37:38])
        self.stacks[1].reverse()
        self.stacks[2].reverse()
        self.stacks[3].reverse()
        self.stacks[4].reverse()
        self.stacks[5].reverse()
        self.stacks[6].reverse()
        self.stacks[7].reverse()
        self.stacks[8].reverse()
        self.stacks[9].reverse()
        self.stacks[10].reverse()


    def readStacks(self):
        for line in self.inputData.split('\n'):
            if line[0:3] == ' 1 ':
                return(line.split(' ')[-1])

    def showStacks(self):
        print(self.stacks[1])
        print(self.stacks[2])
        print(self.stacks[3])
        print(self.stacks[4])
        print(self.stacks[5])
        print(self.stacks[6])
        print(self.stacks[7])
        print(self.stacks[8])
        print(self.stacks[9])
        print(self.stacks[10])
        print ('---------------------')

    def processSteps(self):
        for line in self.inputData.split('\n'):
            if line[0:4] == 'move':
                line = line[5:]
                steps = line.split(' from ')
                fromto = steps[1].split(' to ')
                steps = steps[0]
                movefrom = fromto[0]
                moveto = fromto[1]
                print (len(self.stacks[3]))
                print("Moving " + steps + " from " + movefrom + " -> " + moveto)
                for i in range(int(steps)):
                    char = self.stacks[int(movefrom)].pop()
                    self.stacks[int(moveto)].append(char)
                self.showStacks()

    def processSteps2(self):
        container = []
        for line in self.inputData.split('\n'):
            if line[0:4] == 'move':
                line = line[5:]
                steps = line.split(' from ')
                fromto = steps[1].split(' to ')
                steps = steps[0]
                movefrom = fromto[0]
                moveto = fromto[1]
                print (len(self.stacks[3]))
                print("Moving " + steps + " from " + movefrom + " -> " + moveto)
                for i in range(int(steps)):
                    char = self.stacks[int(movefrom)].pop()
                    container.append(char)
                for i in range(int(steps)):
                    char = container.pop()
                    self.stacks[int(moveto)].append(char)
                self.showStacks()

    def processFile(self):
        self.readData()
        self.processSteps2()
        self.showStacks()
        return "A"


with open('prodinput.txt') as f:
    prodData = f.read()
    exercise = Exercise(prodData)
    print(exercise.processFile())
