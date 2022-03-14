convert = {
	'zero' : ('###','# #','# #','# #','###'),
	'uno': ('  #','  #','  #','  #','  #'),
	'due': ('###','  #','###','#  ','###'),
	'tre': ('###','  #','####','  #','###'),
	'quattro': ('# #','# #','###','  #','  #'),
	'cinque': ('###','  #','###','#  ','###'),
	'sei' : ('###','#  ','###','# #','###'),
	'sette': ('###','  #','  #','  #','  #'),
	'otto' : ('###','###','###','###','###'),
	'nove' : ('###','# #','###','  #','###')
}
list1 = ['  #','  #','  #','  #','  #']
list2 = ['###','  #','###','#  ','###']
list3 = ['###','  #','####','  #','###']
list4 = ['# #','# #','###','  #','  #']
list5 = ['###','#  ','###','  #','###']
list6 = ['###','#  ','###','# #','###']
list7 = ['###','  #','  #','  #','  #']
list8 = ['###','# #','###','# #','###']
list9 = ['###','# #','###','  #','###']
list0 = ['###','# #','# #','# #','###']


def print_number(numero):
	global list1,list0,list2,list3,list4,list5,list6,list7,list8,list9
	for i in numero:
		if i == '1':
			for row in range(5):
				print(list1[row])
		if i == '2':
			for row in range(5):
				print(list2[row])
		if i == '3':
			for row in range(5):
				print(list3[row])
		if i == '4':
				for row in range(5):
					print(list4[row])
		if i == '5':
			for row in range(5):
				print(list5[row])
		if i == '6':
			for row in range(5):
				print(list6[row])
		if i == '7':
			for row in range(5):
				print(list7[row])
		if i == '8':
			for row in range(5):
				print(list8[row])
		if i == '9':
			for row in range(5):
				print(list9[row])
		if i == '0':
			for row in range(5):
				print(list0[row])
		 

print_number(input("Enter the number you wish to display: "))



