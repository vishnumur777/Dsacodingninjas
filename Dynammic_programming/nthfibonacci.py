def fibo(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n<=2:
        return n
    else:
        result = fibo(n-1)+fibo(n-2)

    memo[n]=result
    return result


if __name__ == "__main__":
    n=10
    n1=50
    print(fibo(n),fibo(n1))
