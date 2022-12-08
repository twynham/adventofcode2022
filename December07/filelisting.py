import operator


class FileListing:

    def __init__(self, inputfile):
        self.datafile = inputfile
        self.currentdirectory = []
        self.directories = {}
        self.fulldirectories = {}


    def getfileusage(self):
        lines = self.datafile.split('\n')
        linecount = len(lines)
        for i in range(0,linecount):
            if lines[i][0:1] == '$':
                command = lines[i][2:4]
                params = lines[i][5:]
                if command == 'cd':
                    if params == '/':
                        self.currentdirectory.clear()
                    elif params == '..':
                        self.currentdirectory.pop()
                    else:
                        self.currentdirectory.append(params)


#                print("Command: " + command + " params " + params)
#                print(self.currentdirectory)

                currentdir = '/'
                for dir in self.currentdirectory:
                    currentdir += dir + '/'

                print (lines[i] + ' ==> ' + currentdir)

                if command == 'ls':
                    totalbytes = 0
                    if i + 1 <= linecount-1:
                        while lines[i+1][0:1] != '$':
                            i += 1
                            print(lines[i])
                            print(lines[i][0:3])
                            print(lines[i].split(' ')[0])
                            if lines[i][0:3] != 'dir':
                                totalbytes += int(lines[i].split(' ')[0])
                            if i + 1 > linecount-1:
                                break
                    print(currentdir + ' ' + str(totalbytes))
                    self.directories[currentdir] = totalbytes

        print(self.directories)

        for key in self.directories:
            stub = key
            self.fulldirectories[stub] = 0
            for searchkey in self.directories:
                if searchkey[0:len(stub)] == stub:
                    self.fulldirectories[stub] += self.directories[searchkey]

        print(self.fulldirectories)
        resultbytes = 0
        for key in self.fulldirectories:
            if self.fulldirectories[key] <= 100000:
                resultbytes += self.fulldirectories[key]

        sorted_d = sorted(self.fulldirectories.items(), key=operator.itemgetter(1))
        print(sorted_d)
        for key in sorted_d:
            if sorted_d[key] >= 28888895:
                print(key + ' = ' + sorted_d[key])

        return(str(resultbytes))


with open('prodinput.txt') as f:
    prodData = f.read()
    listing = FileListing(prodData)
    print(listing.getfileusage())