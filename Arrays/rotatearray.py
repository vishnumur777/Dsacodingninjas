def rotateArray(arr,k):
    for i in range(k):
        arr.append(arr.pop(0))

    return arr


n=int(input())
arr=list(map(int,input().split()))
k=int(input())

res=rotateArray(arr, k)
print(*res)



