from time import sleep
from os import system
from encryptionKey import encryptKey, decryptKey
import re
import random #random.randrange(min,max,step)
class Encryptor:
    
    #__getoptsKey = {}
    __fileLocation = " " #file 
    __mode = " "  #getopts
    __lines = [] #file lines
    __buildLine = [] #builds new line
    __encryptKey = {}
    __stringText = " "
    lineCounter = 0
    __methodType = " "
    def __init__(self, typeM, typeEn, textInput):
        self.__mode = typeM.lower().strip('-')
        self.__methodType = typeEn
        if typeEn == "En":
            self.__encryptKey = encryptKey()
        else: 
            self.__encryptKey = decryptKey()
        #checkEncryptionKey()
        if self.__mode.find('s') != -1:
            self.__stringText = textInput.lower().strip()
            self.argInterpt()
            #print('####')
            #print(self.__stringText)
        else : 
            self.__fileLocation = textInput
        #print("here")
    def argInterpt(self):
        if self.__mode[0].find('s') != -1: #standard iself.pushStringnput/enecrpt/output line
            #self.standardInput()
            pass
        elif self.__mode[0].find('f') != -1: #encrpyt from file
            pass
        elif self.__mode[0].find('help') != -1:
            pass
        else:
            print("""Invalid flag: {} \nFORMAT python3 .py(file) arg1(-s,f) arg2(txt)
            \nType --help for advanced syntax help""".format(self.__mode[0]))
            sleep(5)
            exit()
            #mode is not valid. Progam will not exit
    def buildNewLine(self, charLine):
        i=0
        print("THIS IS CHAR:" ,charLine)
        for char in charLine:
            print("FOR CHAR:", char)
            if i == 0:
                strLine = str(char) 
            else:        
                strLine += char
            i= i + 1
        print("FINAL ", strLine)
        if self.__mode == 's':
            print("came oiut her")
            return strLine
        if self.__mode == 'f':     
            self.__tempPlates.update({self.lineCounter : strLine})
            self.lineCounter += 1
        
    def readFile(self): #STILL NEED TO DEBUG
        try: 
            openFile = open(self.__fileLocation, "r", encoding="utf8")
            self.__lines = openFile.splitLines()
            for line in self.__lines:
                i = 0     
                for letter in line:
                    self.__buildLine[i]=self.__encryptKey[letter] #conversion
                    if i == (len(self.line)-1):
                        self.buildNewLine(self.__buildLine)
                        break
                    i+=1
        except FileNotFoundError:
            print("File {} does not Exist.\nCheck spelling and make sure file exists".format(self.__fileLocation))
            sleep(2)    
            exit()
    def standardInput(self):
        i = 0
        self.__buildLine.clear()
        for letter in self.__stringText:
            print("Letter   ", letter)
            if letter == '.' or letter == ' ':
                self.__buildLine.append(letter)
            else:
                print(i)
                self.__buildLine.append(self.__encryptKey[letter])
                print(self.__encryptKey[letter])
                print(self.__buildLine)
            i+=1
        
        line = self.buildNewLine(self.__buildLine)
        line = re.split('[!.?]', line) #lossy encrytion... Make key for marks
        i=0
        for sent in line:
            if i == 0: #for re-capitalizing line
                newString = sent
            else:
                temp = sent.capitalize() + "."
                newString += temp
            i+=1
        return newString
    def checkEncryptionKey(self): #STILL NEED TO DEBUG
        try: 
            openFile = open("/home/erik/Documents/Programming/PythonEncrpytor/encryptionKey.py") #, "r", encoding="utf8"
            print("Encryption key Found\n")
            openFile.close()
        except FileNotFoundError:
            print("Encrpytion Key not Found")
            sleep(2)    
            exit()
        
