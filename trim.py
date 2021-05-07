import glob

inps = glob.glob("*chapter*ipynb")
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
    
