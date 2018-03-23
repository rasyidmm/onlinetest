n =1
c = int(input("masukan angka : "))
z = int(c / 2)

for r in range(z):
    for j in range( r + 1):
        print("*", end= "")
    print()
for x in reversed(range(z+1)):
    for k in range(x - 1):
        print("*", end= "")
    print()

for x in reversed(range(z)):
    for k in range(x + 1):
        print(" ", end= "")
    for j in reversed(range( z - (x+1))):
        print("#", end= "")
    for m in range(z-x):
        print("#", end= "")
    print()
for x in range(z):
    for k in reversed(range(x + 1)):
        print(" ", end= "")
    for j in range( z -x):
        print("#", end= "")
    for m in reversed(range(z-(x+1))):
        print("#", end= "")
    print()



for q in range(z):
    for x in reversed(range(c)):
        if(0 == x%2):
            print("+ ",end="")
            print("+ ",end="")
        else:
            print("- ",end="")
            print("- ",end="")
    print()
    for x in reversed(range(c)):
        if(0 == x%2):
            print("+ ",end="")
            print("+ ",end="")
        else:
            print("- ",end="")
            print("- ",end="")
    print()
    for x in reversed(range(c)):
        if(0 == x%2):
            print("- ",end="")
            print("- ",end="")
        else:
            print("+ ",end="")
            print("+ ",end="")
    print()
    for x in reversed(range(c)):
        if(0 == x%2):
            print("- ",end="")
            print("- ",end="")
        else:
            print("+ ",end="")
            print("+ ",end="")
    print()
