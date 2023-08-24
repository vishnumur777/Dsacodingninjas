def getKthlargest(subsequence,k):
    b = list(set(subsequence))
    if len(b)==1:
        return -1
    subsequence.sort()
    return subsequence[len(subsequence)-k]


if __name__ == "__main__":
    b=list(map(int,input().split()))
    k=int(input())
    v=getKthlargest(b,k)
    print(f"The {k}th largest element from the given array is: {v}")


