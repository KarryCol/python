# coding:utf-8
# 有一个测试运行超时
import math

def is_prime_number(a):
	if a > 1:
		sqrt_number = int(math.sqrt(a))
		for i in range(2, sqrt_number+1):
			if (a % i) == 0:
				return False
		return True
	else:
		return False
		
# [start, end] = map(lambda x:int(x), input().split(' '))
[start, end] = map(int, input().split(' '))

if start <= end <= 10000:
	total = end - start + 1
	index = 1
	result_list = []
	for i in range(1, 999999):
		if is_prime_number(i):
			index = index + 1
			if index > start:
				result_list.append(i)
				if len(result_list) == total:
					break
	for index,number in enumerate(result_list):
		if index != 1 and (index+1) % 10 == 0:
			print (number)
		elif index == len(result_list)-1:
			print (number)
		else:
			print (number, end=' ')