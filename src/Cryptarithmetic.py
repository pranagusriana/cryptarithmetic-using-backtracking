from FileProcessing import FileProcessing

class Cryptarithmetic:
    def __init__(self, namaFile):
        self.fileObj = FileProcessing()
        self.fileObj.readFile(namaFile)
        self.oprresult = self.fileObj.oprresult
        self.operand = self.fileObj.operand
        self.result = self.fileObj.result
        self.idxchr = self.fileObj.idxchr
        self.arr = []
        self.sol = []
        self.n = 0

    # Fungsi Pembangkit untuk membangkitkan nilai xk
    def tempat(self, i, k):
        for j in range(k):
            if(self.arr[j] == i):
                return False
        return True

    # Fungsi Pembatas untuk mengecek apakah xk yang dibangktkan mengarah ke solusi, jika true maka pembangkitan xk+1 dilanjutkan
    def boundingFunction(self, k):
        maksLen = self.fileObj.findMaxLen(self.oprresult)
        Xi = 0
        # Mengecek constrain, misal ABC + DEF = GHI, memiliki constrain:
        # 1. (C + F) mod 10 = I
        # 2. ((B + E) + (C + F) div 10) mod 10 = H
        # 3. ((A + G) + ((B + E) + (C + F) div 10) div 10) mod 10 = G
        for i in range(maksLen):
            hsl = 0
            for strOpr in self.operand:
                idxtemp = len(strOpr) - 1 - i
                if(idxtemp >= 0):
                    if(self.idxchr[strOpr[idxtemp]] > k):
                        return True
                    hsl += self.arr[self.idxchr[strOpr[idxtemp]]]
            idxResult = self.idxchr[self.result[len(self.result) - 1 - i]]
            xResult = self.arr[idxResult]
            if(idxResult > k):
                return True
            # Jika tidak memenuhi salah satu constraint maka akan mengembalikan nilai False
            if((hsl+Xi) % 10 != xResult):
                return False
            Xi = (hsl + Xi)//10
        # Cek jika karakter valid atau tidak (huruf awal jika panjangnya lebih dari satu dan akan disubstitusi dengan 0 maka return False)
        for strOpRes in self.oprresult:
            if(len(strOpRes) > 1 and self.arr[self.idxchr[strOpRes[0]]] == 0):
                return False
        return True

    # Algoritma backtracking
    def backTracking(self, k):
        for i in range(10):
            if(self.tempat(i, k)):
                self.arr[k] = i
                if(self.boundingFunction(k)):
                    if(k == self.n):
                        self.sol.append(self.arr.copy())
                    else:
                        self.backTracking(k+1)
                    self.arr[k] = -1

    # Fungsi untuk menampilkan solusi ke layar
    def printSolusi(self):
        strRet = ""
        solusike = 1
        arrchr = []
        for key in self.idxchr:
            arrchr += [key]
        strRet += "="*110 + "\n" + " "*20 + f"Terdapat {len(self.sol)} Solusi dari permainan cryptarithmetic ini, yaitu: \n" + "="*110 + "\n"
        for solusi in self.sol:
            strRet += "*"*10 + f" Solusi ke-[{solusike}] : {arrchr} = {solusi} " + "*"*10 + "\n"
            for opr in self.operand:
                for chrOp in opr:
                    strRet += str(solusi[self.idxchr[chrOp]])
                strRet += "\n"
            strRet += "----------+\n"
            for chrRes in self.result:
                strRet += str(solusi[self.idxchr[chrRes]])
            strRet += "\n"
            solusike = solusike + 1
        print(strRet)

    # Fungsi yang dipanggil jika ingin menyelesaikan suatu persoalan cryptarithmetic
    def solve(self):
        self.n = len(self.idxchr) - 1
        if(self.n < 10):
            self.arr = [-1 for i in range(self.n+1)]
            self.backTracking(0)
            if(len(self.sol) > 0):
                self.printSolusi()
            else:
                print("Tidak memiliki solusi")
        else:
            print("Tidak bisa diselesaikan karena jumlah huruf uniknya lebih dari 10")

# Main function
# Untuk melakukan run: buka folder src, lalu ketikkan pada command prompt : python Cryptarithmetic.py
if __name__ == "__main__":
    cr = Cryptarithmetic("test3.txt")
    cr.solve()