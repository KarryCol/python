# coding:utf-8
import math

def is_prime_number(a):
	if a > 1:
		num_sqrt = int(math.sqrt(a))
		for i in range(2, num_sqrt + 1):
			if (a % i) == 0:
				return False
		return True
	else:
		return False

result = 0
number = int(input())

if 1 < number < 100000:
	for num in range(1, number):
			if (num % 2 == 0):
				continue
			if is_prime_number(num):
				temp = num + 2
				if 2 < temp < number:
					if is_prime_number(temp):
						result = result + 1
print (result)