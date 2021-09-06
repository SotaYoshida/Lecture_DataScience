import glob

def rep():
    inps = glob.glob("./notebooks/*chapter*ipynb")
    for inpf in inps:
        inp=open(inpf,"r")
        lines=inp.readlines()
        inp.close()
        oupf = open(inpf,"w")
        for line in lines:
            tl = line.rstrip()
            if "AdDS2020" in tl:
                tl.replace("AdDS2020","AdDS2021")
            print(tl,file=oupf)
        oupf.close()
#rep()

def forURL():
    # ** Lecture_DataScience/blob/master/** =>
    # https://github.com/SotaYoshida/Lecture_DataScience/tree/2021/notebooks
    inps = glob.glob("./notebooks/*ipynb")
    for inpf in inps:
        inp=open(inpf,"r")
        lines=inp.readlines()
        inp.close()
        oupf = open(inpf,"w")
        for line in lines:
            tl = line.rstrip()
            if "Lecture_DataScience/tree/2021/" in tl:
                tl=tl.replace("nce/tree/2021/","nce/blob/2021/")
            print(tl,file=oupf)
        oupf.close()
forURL()
def README():
    inp=open("README.md","r")
    lines=inp.readlines()
    inp.close()
    oupf=open("README.md","w")
    for line in lines:
        tl = line.rstrip()
        if "Lecture_DataScience/tree/2021/" in tl:
            tl=tl.replace("nce/tree/2021/","nce/blob/2021/")
        print(tl,file=oupf)
    oupf.close()
README()
