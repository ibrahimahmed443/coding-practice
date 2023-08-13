def gcd(a, b):

	while b:
		a, b = b, a % b

	return a

print(gcd(1653264, 3918848))
