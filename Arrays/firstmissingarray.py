def firstMissing(arr,n):

    visited=[False for i in range(n+2)]

    # Add all the positive integers in visited array.
    for i in range(n):
        if (arr[i] >= 0 and arr[i] <= n):
            visited[arr[i]] = True

    for i in range(1,n+2):
        if visited[i] is False:
            return i
    return -i

if __name__ == "__main__":
	arr = [ 2,3,1,5,7,4,9,11,15 ]
	print(firstMissing(arr,len(arr)))
