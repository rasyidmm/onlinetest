def prime(angka):
    count = 0
    for i in range(1,angka + 1):
        if(angka % i == 0):
            count += 1
    if(count==2):
        return "prime"
    else:
        return "not prime"

jj = prime(10)
print(jj)