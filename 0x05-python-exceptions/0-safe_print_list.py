#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

	try:
		for count in range(x):
			print(my_list[count], end=" ")
		return x
	except IndexError:
	  return count
	 finally:
	  print()
