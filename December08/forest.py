import operator


class Trees:

    def __init__(self, inputfile):
        self.forestheights = {}
        self.forestvisible = {}
        self.rows = 0
        self.columns = 0

        row = 0
        for line in inputfile.split('\n'):
            for column in range (0,len(line)):
                position = str(row)+','+str(column)
                self.forestheights[position] = int(line[column:column+1])
            row += 1

        self.rows = row
        self.columns = column

        #print(self.forestheights)

    def processdata(self):

        # scan from left to right
        for row in range(0,self.rows):
            maxheight = 0
            for column in range(0,self.columns+1):
                position = str(row)+','+str(column)

                if column == 0:
                    #print ("Hit edge at " + position)
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True
                elif self.forestheights[position] > maxheight:
                    #print ("Found taller tree at " + position)
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True

        print(self.count())

        # scan from right to left
        for row in range(0,self.rows):
            maxheight = 0
            for column in range(self.columns,-1,-1):
                position = str(row)+','+str(column)
                if column == self.columns:
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True
                elif self.forestheights[position] > maxheight:
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True

        print(self.count())

        # scan from top to bottom
        for column in range(0,self.columns+1):
            maxheight = 0
            for row in range(0,self.rows):
                position = str(row)+','+str(column)

                if row == 0:
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True
                elif self.forestheights[position] > maxheight:
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True

        print(self.count())

        # scan from bottom to top
        for column in range(0,self.columns+1):
            maxheight = 0
            for row in range(self.rows-1,-1,-1):
                position = str(row)+','+str(column)

                if row == self.rows-1:
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True
                elif self.forestheights[position] > maxheight:
                    maxheight = self.forestheights[position]
                    self.forestvisible[position] = True

        print(self.count())

        # for i in range (0,5):
        #         position = '0,'+str(i)
        #         print(self.forestvisible.get(position))
        #         position = '4,'+str(i)
        #         print(self.forestvisible.get(position))
        #         position = str(i)+',0'
        #         print(self.forestvisible.get(position))
        #         position = str(i)+',4'
        #         print(self.forestvisible.get(position))


    def count(self):
        count = 0
        for column in range(0,self.columns+1):
            for row in range (0,self.rows):
                position = str(row)+','+str(column)
                #print (position)
                status = self.forestvisible.get(position)
                if status:
                    count += 1

        return(count)



with open('prodinput.txt') as f:
    prodData = f.read()
    trees = Trees(prodData)
    trees.processdata()
    print(trees.count())
    print(trees.forestvisible)

