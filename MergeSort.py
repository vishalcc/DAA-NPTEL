def MergeSort(li,s,e):
    if(s<e):
        middle=int((s+e-1)/2)
        MergeSort(li,s,middle)
        MergeSort(li,middle+1,e)
        print(li[s:e])


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = int((l + (r)) / 2)

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        print(l,m,r,arr[l:m],arr[m:r])
start=0
end=7
mergeSort([10,1,3,4,11,2,31,15],start,end)