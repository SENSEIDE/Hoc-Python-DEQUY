memo = {}
def fibo_fast(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fibo_fast(n-1) + fibo_fast(n-2)
    return memo[n]

print(fibo_fast(100))
