def equilibriumIndex(arr):
    lsum=0
    rsum=0
    for i in range(len(arr)):
        rsum+=arr[i]

    for j in range(len(arr)):
        rsum -= arr[j]
        if lsum == rsum:
            return j
        lsum += arr[j]

    return -1


if __name__ == "__main__":
    r = [ 1,7,3,6,5,6 ]
    print(equilibriumIndex(r))
