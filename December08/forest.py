import operator


class Trees:

    def __init__(self, inputfile):
        self.directories = {}
        self.fulldirectories = {}

    def count(self):
        return(-1)


with open('prodinput.txt') as f:
    prodData = f.read()
    trees = Trees(prodData)
    print(trees.count())
