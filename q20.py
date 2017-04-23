"""
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""


def divisible_by_7(n):
	for item in range(1,n):
		if(item%7==0):
			print(item)
			yield