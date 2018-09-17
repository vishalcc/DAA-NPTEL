def StrangeMerge(A, m, B,n, C):
    i,j,k = 0,0,0
    m,n=len(A),len(B)
    while (i + j < m + n) :
        if (i == m) :
            j+=1
        if (j == n):
            C[k] = A[i]
            i+=1
            k+=1

        if (i < m and j < n) :
            if (A[i] < B[j]):
                C[k] = A[i]
                i+=1
                k+=1
            if (A[i] == B[j]):
                i+=1
                j+=1
            if (A[i] > B[j]):
                j+=1
    print(C)
StrangeMerge([1,4,6,9,100],0,[2,4,3,5,6,11,34],0,[0 for x in range(20)])