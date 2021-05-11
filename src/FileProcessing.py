class FileProcessing:
    def __init__(self):
        self.oprresult = []
        self.operand = []
        self.result = ""
        self.idxchr = {}

    def findMaxLen(self, arrstr):
        maks = len(arrstr[0])
        for string in arrstr:
            if(maks < len(string)):
                maks = len(string)
        return maks

    def isSolveable(self):
        maksOp = len(self.operand[0])
        for op in self.operand:
            if (maksOp < len(op)):
                maksOp = len(op)
        return len(self.result) >= maksOp and len(self.result) <= maksOp + 1

    def readFile(self, namaFile):
        file = open("../test/"+namaFile, "r")
        file_input = file.read().splitlines()
        for strOperand in file_input:
            if(strOperand[len(strOperand)-1] == '+'):
                break
            else:
                self.operand.append(strOperand)
        self.result = file_input[len(file_input)-1]
        file_input.pop(len(file_input)-2)
        self.oprresult += file_input
        maksLen = self.findMaxLen(file_input)
        idx = 0
        for i in range(maksLen):
            for string in file_input:
                idxtemp = len(string) - 1 - i
                if(idxtemp >= 0):
                    if(self.idxchr.get(string[idxtemp], -1) == -1):
                        self.idxchr[string[idxtemp]] = idx
                        idx += 1

if __name__=="__main__":
    N = input("Masukkan nama file: ")
    p = FileProcessing()
    p.readFile(N)
    print(p.isSolveable())