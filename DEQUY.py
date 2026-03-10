def fibo(n):
    if n < 0: return "Không hợp lệ"
    if n <= 1: return n
    return fibo(n-1) + fibo(n-2)

n = 10
print(f"Số Fibonacci thứ {n} là: {fibo(n)}")
