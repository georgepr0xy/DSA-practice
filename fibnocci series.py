def fib(n):
    if n <= 1:
      return n
    return fib(n-1) + fib(n-2)

b =fib(4)
print(b)

    