import xlwt
import numpy as np

Nsample=4000
Ddim=20

np.random.seed(11)
ys = np.random.normal(0,1,Nsample*Ddim).reshape(Nsample,Ddim)
book = xlwt.Workbook()
sheet1=book.add_sheet('NewSheet_1')

for i in range(Ddim):
    for j in range(Nsample):
        sheet1.write(j,i,ys[j,i])

book.save('sample_'+str(Nsample)+"_"+str(Ddim)+'.xls')
