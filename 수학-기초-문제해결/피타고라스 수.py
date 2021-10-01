n = int(input())
for i in range(1,n+1):
    for j in range(i,n+1):
        if (n*n-2*i*n-2*j*n+2*i*j == 0):
            l = [i, j, int((i*i+j*j)**(0.5))]
            print(l)