# ukuran matrix
M=8

# mencetak jalurnya
def langkah(lang):
    for i in lang:
        for j in i:
            print(str(j) + " ", end="")
        print("")

# Fungsi cek jika x,y benar
def isSafe(maze,x,y):
    if x >= 0 and x < M and y >= 0 and y < M and maze[x][y] == 1:
        return True

    return False

def solveMaze(maze):
    lang = [[0 for j in range(8)]for i in range (8)]

    if solveMazeUtil(maze,0,1,lang) == False:
        print("Tidak ada solusi")
        return False

    langkah(lang)
    return True

# Fungsi untuk mengecek langkah
def solveMazeUtil(maze,x,y,lang):
    #koordinat finish
    if x == M-2 and y == M-4:
        lang[x][y] = 1
        return True

# Pengecekan jika x dan y valid
    if isSafe(maze,x,y) == True:
        # Menandai koordinat yang merupakan path benar
        lang[x][y] = 1

        # BErpindah ke bawah
        if solveMazeUtil(maze,x+1,y,lang) == True:
            return True

        # Jika pindah ke bawah tidak bisa, maka pindah ke kanan
        if solveMazeUtil(maze,x,y+1,lang) == True:
            return True

        # Jika pindah ke bawah dan ke kanan tidak bisa, maka pindah ke kiri
        if solveMazeUtil(maze, x, y - 1, lang) == True:
            return True

        # Backtrack jika x dan y bukan jalurnya
        lang [x][y] = 0
        return False

if __name__ == "__main__":
    maze = [[0,1,1,0,1,1,1,1],
            [1,1,0,0,0,1,1,0],
            [1,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,0],
            [0,0,0,1,1,1,1,0],
            [1,1,1,0,0,1,1,0],
            [1,1,1,1,1,1,0,1],
            [1,1,1,1,0,0,1,1]]

    solveMaze(maze)