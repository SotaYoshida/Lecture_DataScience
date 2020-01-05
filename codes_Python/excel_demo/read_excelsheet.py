import xlrd
import glob
import numpy as np
import matplotlib.pylab as plt
import os

class xlread:
    def __init__(self,inpf):
        self.inpf = inpf
        self.book = xlrd.open_workbook(inpf)
        self.sheet1=self.book.sheet_by_index(0)
        self.Nc=self.sheet1.ncols
        self.Nr=self.sheet1.nrows
    def val(self,i,j):
        print("val["+str(i)+","+str(j)+"]",self.sheet1.cell(i,j).value)

    def xlsearch(self,tfloat):
        ls = []
        for j in range(Nc):
            for i in range(Nr):
                if abs(self.sheet1.cell(i,j).value) < tfloat:
                    ls+= [ [i,j] ]
        print("indices for val.<"+str(tfloat), ls )

    def plot(self):
        for j1 in range(Nc):
            col1 = self.sheet1.col_values(j1)
            for j2 in range(j1,Nc):
                if j1 == j2 :
                    continue
                col2 = self.sheet1.col_values(j2)
                fig = plt.figure(figsize=(6,6))
                ax = fig.add_subplot(1,1,1)
                ax.set_facecolor("#D3DEF1")
                ax.set_xlim(-2,2);ax.set_ylim(-2,2)
                ax.set_xlabel(str(j1)+"th colum");ax.set_ylabel(str(j2)+"th colum")
                ax.scatter(col1,col2,marker="o",s=1,alpha=0.7,color="k")            
                plt.savefig("./pic/corr_"+str(j1)+"vs"+str(j2)+".pdf")
                plt.close()
if __name__ == "__main__":
    os.system("mkdir pic")
    inps=glob.glob("./*xls")
    tfloat=1.e-2
    for inpf in inps:
        N=inpf.split("_")
        try:
            Nr=int(N[-2]);Nc=int(N[-1].split(".")[0])
        except:
            print("err!");exit()
        np.random.seed(11)## for reploducibility
        i=np.random.choice(range(Nr))
        j=np.random.choice(range(Nc))
        t_xl= xlread(inpf)
        t_xl.val(i,j)
        ls = t_xl.xlsearch(tfloat)
        t_xl.plot()
