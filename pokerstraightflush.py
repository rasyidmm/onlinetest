kartu=["Aw","Ak","Ah","Ad","2w","2k","2h","2d","3w","3k","3h","3d","4w","4k","4h","4d","5w","5k","5h","5d","6w","6k","6h","6d","7w","7k","7h","7d","8w","8k","8h","8d","9w","9k","9h","9d","10w","10k","10h","10d","Jw","Jk","Jh","Jd","Qw","Qk","Qh","Qd","Kw","Kk","Kh","Kd"]

klx=[]
for i in range(36):
    for j in range(i,i+17,4):
        klx.append(kartu[j])
    print(klx)
    klx.clear()
print("Straight Flush= ",)
