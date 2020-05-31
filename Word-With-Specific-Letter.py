import sys

class InputFile:
    def __init__(self ,FileName , encoding = "UTF-8"):
        self.File = open(FileName , "r" , encoding = encoding)
        self.fileStartPoint = 0
    
    def closeConnection(self):
        self.File.close()

    def readNChar(self , N ):
        return self.File.read(N)

    def startPosition(self):
        while(True):
            text = self.File.readline()
            if(text[0] != "#"):
                break
        
        while(True):
            text = self.File.readline()
            if(text[0] != " "):
                break
        
        self.fileStartPoint = self.File.tell()
        
    def readNextWord(self):
        text = ""
        char = ''
        
        while(True):
            char = self.File.read(1)
            if(char == ""):
                return 0
            if(char == "\t"):
                break
            text+=char
        
        while(True):
            if(self.File.read(1)=="\n"):
                break

        return text

class stringWorks:
    def __init__(self):
        self.charlist = []
        self.lengthOfList = 0

    def isUsable(self , text):
        for charInText in text :
            retValue = False
            for charNeedToBeCompared in self.charlist:
                if(charInText == charNeedToBeCompared):
                    retValue = True
                    break
            if(retValue == False):
                return False
        return True

class OutputFile:
    def __init__(self, FileName):
        self.File = open(FileName , "w" , encoding="UTF-8")

    def closeConnection(self):
        self.File.close()

    def writeWord(self , text):
        self.File.write(text + "\n")


print("Input File Name?")

inputFile = InputFile("%s.txt" %input())
inputFile.startPosition()

tmp = stringWorks()

print("How Many Character In Compare List?")
tmp.lengthOfList = int(input())

for i in range(0 , tmp.lengthOfList , 1):
    print( "%d <= " %(i+1) , end = "" )
    tmp.charlist.append(sys.stdin.read(2)[0])

print("Output File Name?")
outputFile = OutputFile( "%s.txt" %input() )

while(True):
    text = inputFile.readNextWord()
    
    if(text == 0):
        break

    if(tmp.isUsable(text)):
        outputFile.writeWord(text)

    

outputFile.closeConnection()
inputFile.closeConnection()
