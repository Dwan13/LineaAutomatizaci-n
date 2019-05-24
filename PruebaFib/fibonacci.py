def fib(n):
    if n < 2:
        return n
    else:
        fn = fib(n-1) + fib(n-2)
        return fn
	
