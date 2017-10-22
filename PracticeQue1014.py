# coding:utf8

week_tuple = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT', 'G': 'SUN'}

fir_sentence = input('first sentence：')
sec_sentence = input('second sentence：')
thi_sentence = input('third sentence：')
fou_sentence = input('fourth sentence：')

day = None
hour = None
minute = None
result_time = []
def find_time(a,b,needNum):
	for a_index,a_item in enumerate(a):
		for b_index,b_item in enumerate(b):
			if (a_index == b_index) and (a_item == b_item):
				if needNum == 1:
					if a_item.isalpha():
						minute = a_index
						return minute
				else:
					if len(result_time) == 0 and a_item.isalpha():
						result_time.append(a_item)
					elif len(result_time) > 0 and (a_item.isdigit() or a_item.isupper()):
						result_time.append(a_item)
					if len(result_time) == 2:
							return result_time	
if(0 < len(fir_sentence) <= 60 and 0 < len(sec_sentence) <= 60):
	temp_list = find_time(fir_sentence, sec_sentence, 2)
	day = temp_list[0]
	hour = temp_list[1]
	if hour.isalpha() and hour.isupper():
		hour = ord(hour) - 64 + 9

if(0 < len(fir_sentence) <= 60 and 0 < len(sec_sentence) <= 60):
	minute = find_time(thi_sentence, fou_sentence, 1)

print ('%s %02d:%02d' % (week_tuple[day], int(hour), int(minute)))




