# coding:utf-8
res_list = [[], [], [], [], []]
def del_result(x):
	result = x % 5
	if result == 0 && x % 2 == 0:
		res_list[0].append(x)
	elif result == 1:
		res_list[1].append(x)
	elif result == 2:
		res_list[2].append(x)
	elif result == 3:
		res_list[3].append(x)
	else:
		res_list[4].append(x)
	for item_list in res_list:
		item_list

number_list = raw_input().split(' ')
if len(number_list) <= 1000:
	for number in number_list:
		if 0 < number <= 1000:
			del_result(number)

