def stalinsort(arr,n):
    shoot = []
    for i in range(n-1):
        if arr[i+1] < arr[i]:
            shoot.append(arr[i+1])

    for i in shoot:
        arr.pop(arr.index(i))

    return arr

if __name__ == "__main__":
    arr = [ 10,20,15,5,25 ]
    print(stalinsort(arr,len(arr)))

