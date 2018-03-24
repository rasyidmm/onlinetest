jalan=["Yes,Yes,Yes,No,Yes,Yes,Yes,Yes"],["Yes,Yes,No,No,No,Yes,Yes,No"],["Yes,Yes,Yes,Yes,Yes,Yes,Yes,No"],["Yes,Yes,Yes,Yes,Yes,Yes,Yes,No"],["No,No,No,Yes,Yes,Yes,Yes,No"],["Yes,Yes,Yes,No,No,Yes,Yes,No"],["Yes,Yes,Yes,Yes,Yes,Yes,No,Yes"],["Yes,Yes,Yes,Yes,No,No,Yes,Yes"]
start=[0][1]
target=[6][4]
temp=[]
x=0
y=0
i=0
j=1

while (x!=6) and (y!=4):
    if(jalan[i][j]==Yes):
        temp.append(i)
        x=i
        temp.append(j)
        y=j
        j+=1
    elif(jalan[i][j]==No):
        j-=1
        i+=1
        x=i
        y=j
print(jalan)
