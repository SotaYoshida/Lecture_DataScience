import glob

fs = glob.glob("Pytho*ipynb")

for f in fs:
    inp=open(f,"r")
    lines=inp.readlines()
    inp.close()

    oup = open(f,"w")
    tls = lines[:-2]
    for line in tls:    
        print(line.rstrip(),file=oup)

    print('   {',file=oup)
    print('      "cell_type": "markdown",',file=oup)
    print('      "metadata": {',file=oup)
    print('        "id": "q943wB7Z4DYK"',file=oup)
    print('      },',file=oup)
    print('      "source": [',file=oup)
    print('        "--\\n",',file=oup)
    print('        "\\n",',file=oup)
    print('        "Copyright (C) 2021 Sota Yoshida\\n",',file=oup)
    print('        "\\n",',file=oup)
    print('        "[ライセンス:クリエイティブ・コモンズ 4.0 表示 (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.ja)"',file=oup)
    print('      ]',file=oup)
    print('    }',file=oup)
    print('  ]',file=oup)
    print('}',file=oup)
    oup.close()
    
