class Rope():

    def __init__(self, inputFile):
        self.datafile = inputFile
        self.tailpositions = {}

    def process(self):

        hx = 0
        hy = 0
        tx = 0
        ty = 0

        for line in self.datafile.split('\n'):
            direction = line[0:1]
            distance = int(line[2:])


            for i in range(0,distance):

                # find where the tail is in relation to the head

                diffx = hx - tx
                diffy = hy - ty
                diff = str(diffx) + ',' + str(diffy)

                if direction == 'R':
                    hx += 1
                    if diff == '1,-1':
                        tx += 1
                        ty -= 1
                    if diff == '0,-1':
                        pass
                    if diff == '-1,-1':
                        pass
                    if diff == '1,0':
                        tx += 1
                    if diff == '0,0':
                        pass
                    if diff == '-1,0':
                        pass
                    if diff == '1,1':
                        tx += 1
                        ty += 1
                    if diff == '0,1':
                        pass
                    if diff == '-1,1':
                        pass


                if direction == 'L':
                    hx -= 1
                    if diff == '1,-1':
                        pass
                    if diff == '0,-1':
                        pass
                    if diff == '-1,-1':
                        tx -= 1
                        ty -= 1
                    if diff == '1,0':
                        pass
                    if diff == '0,0':
                        pass
                    if diff == '-1,0':
                        tx -= 1
                    if diff == '1,1':
                        pass
                    if diff == '0,1':
                        pass
                    if diff == '-1,1':
                        tx -= 1
                        ty += 1

                if direction == 'U':
                    hy += 1
                    if diff == '1,-1':
                        pass
                    if diff == '0,-1':
                        pass
                    if diff == '-1,-1':
                        pass
                    if diff == '1,0':
                        pass
                    if diff == '0,0':
                        pass
                    if diff == '-1,0':
                        pass
                    if diff == '1,1':
                        tx += 1
                        ty += 1
                    if diff == '0,1':
                        ty += 1
                    if diff == '-1,1':
                        tx -= 1
                        ty += 1

                if direction == 'D':
                    hy -= 1
                    if diff == '1,-1':
                        tx += 1
                        ty -= 1
                    if diff == '0,-1':
                        ty -= 1
                    if diff == '-1,-1':
                        tx -= 1
                        ty -= 1
                    if diff == '1,0':
                        pass
                    if diff == '0,0':
                        pass
                    if diff == '-1,0':
                        pass
                    if diff == '1,1':
                        pass
                    if diff == '0,1':
                        pass
                    if diff == '-1,1':
                        pass

                # print (str(hx) + ',' + str(hy) + ' --> ' + str(tx) + ',' + str(ty))
                self.tailpositions [str(tx) + ',' + str(ty)] = True

        print(self.tailpositions)

        return (len(self.tailpositions))

with open('proddata.txt') as f:
    prodData = f.read()
    rope = Rope(prodData)
    print(rope.process())

