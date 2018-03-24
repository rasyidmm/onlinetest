jalan =[1,1,1,0,1,1,1,1],\
       [1,1,0,0,0,1,1,0],\
       [1,1,1,1,1,1,1,0],\
       [1,1,1,1,1,1,1,0],\
       [0,0,0,1,1,1,1,0],\
       [1,1,1,0,0,1,1,0],\
       [1,1,1,1,1,1,0,1],\
       [1,1,1,1,0,0,1,1]
temp = []
y = 0
x = 0
step=[]
start =jalan[x][y]
def carijalan(jalan):
    for i in jalan:
        for x in i:
            if jalan[x][y+1] == 1 and jalan[x][y+2] ==1 and jalan[x][y+3] ==1:
                print("jalan buntu")
            elif jalan[x][y+1] == 1:
                if jalan[x+1][y+1] == 1 and jalan[x+2][y+1] == 1 and jalan[x+3][y+1] == 1 and jalan[x+4][y+1]:
                    print("jalan buntu")
                elif jalan[x+1][y+1] == 1 and jalan[x+2][y+1] == 1 and jalan[x+3][y+1] == 1:
                    if jalan[x+3][y+1] == 1 and jalan[x+3][y+2] == 1 and jalan[x+3][y+3] == 1 and jalan[x+3][y+4] == 1 and jalan[x+3][y+5] == 1 and jalan[x+3][y+6] == 1 and jalan[x+3][y+7] == 1:
                        print ("jalan buntu")
                    elif jalan[x+3][y+1] == 1 and jalan[x+3][y+2] == 1 and jalan[x+3][y+3] == 1 and jalan[x+3][y+4] == 1 and jalan[x+3][y+5] == 1 and jalan[x+3][y+6] == 1:
                        if jalan[x+3][y+6] == 1 and jalan[x+4][y+6] == 1 and jalan[x+5][y+6] == 1 and jalan[x+6][y+6] == 1:
                            print("jalan buntu")
                        elif jalan[x+3][y+6] == 1 and jalan[x+4][y+6] == 1 and jalan[x+5][y+6] == 1:
                            if  jalan[x+5][y+6] == 1 and  jalan[x+5][y+7] == 1:
                                print("jalan buntu")
                            elif  jalan[x+5][y+6] == 1 and  jalan[x+5][y+6-1] == 1 and  jalan[x+5][y+6-2] == 1:
                                print("jalan buntu")
                            elif jalan[x+5][y+6] == 1 and  jalan[x+5][y+6-1] == 1:
                                if jalan[x+5][y+6-1] == 1 and jalan[x+6][y+6-1] == 1 and jalan[x+7][y+6-1] == 1:
                                    print ("jalan buntu")
                                elif jalan[x+5][y+6-1] == 1 and jalan[x+6][y+6-1] == 1:
                                    if jalan[x+6][y+6-1] == 1 and jalan[x+6][y+6] == 1:
                                        print("jalan buntu")
                                    elif jalan[x+6][y+6-1] == 1 and jalan[x+6][y+6-2] == 1:
                                        print("finish")



print(carijalan(jalan))
