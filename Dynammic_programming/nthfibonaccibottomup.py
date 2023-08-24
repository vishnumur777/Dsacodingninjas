def fibo(n):
    memo = {}
    for i in range(1,n+1):
        if i<=2:
            result=1
        else:
            result=memo[i-1]+memo[i-2]
        memo[i]=result

    return memo[n]


if __name__ == "__main__":
    n=int(input())
    print(fibo(n))


