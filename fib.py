def fib_rec(n):
	if n <=1:
		return n
	else:
		return fib_rec(n-1) + fib_rec(n-2)


def fib(n):
	if n <=1:
		return n

	pointer_1 = 1
	pointer_2 = 0

	for i in range(1, n):
		pointer_2, pointer_1 = pointer_1, pointer_1 + pointer_2

	return pointer_1

print(fib(10))
