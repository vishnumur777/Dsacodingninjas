def isPossible(arr,n):
    count = 0
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            count+=1
            if count > 1:
                return False
            if i<2 or arr[i] >= arr[i-2]:
                arr[i-1] = arr[i]
            else:
                arr[i] = arr[i-1]

    return True

a = [ 4,2,3,4 ]

print(isPossible(a,len(a)))
