import requests
from PIL import Image
from IPython.display import display
import os
import numpy as np
from scipy import linalg
from numpy.linalg import svd, matrix_rank

#os.system('wget "https://github.com/SotaYoshida/Lecture_DataScience/blob/main/notebooks/pic_for_notebook/u_ta.png" -O u_ta.png')
img = Image.open('u_ta.jpeg')
gray_img = img.convert('L')
gray_img.save('u_ta_mono.jpeg')
gray_img = gray_img.resize((gray_img.width//3, gray_img.height//3))  #画像をリサイズ
gray_img 


a = np.asarray(gray_img)
u, s, v = svd(a)
fullrank = matrix_rank(a)
print("full rank => ", fullrank)

# 陽に必要な行列要素の数を計算する関数
def num_of_me(u,s,v,rank):
    m,n = u.shape
    return m * rank + rank + rank*n

#低ランク近似を得る
for factor in [0.05, 0.1, 0.2, 0.3, 1.0]:
    rank = int(factor*fullrank)
    ur = u[:, :rank]
    sr = np.matrix(linalg.diagsvd(s[:rank], rank,rank))
    vr = v[:rank, :]
    b = np.asarray(ur*sr*vr)
    img = Image.fromarray(np.uint8(b))
    USVd = np.dot(ur, np.dot(sr,vr))
    print("rank",rank, " Fnorm ", linalg.norm(a-USVd,"fro"), " # of m.e. ", num_of_me(u,s,v,rank) )
    img.save('u_ta_reconstruct_rank'+str(rank)+'.jpeg')
    display(img)
