"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def allEvenNumbers(first,last):
	a = [x for x in range(first,last+1)]
	b=[]
	for element in a:
		even=True
		for character in str(element):
			if int(character)%2==0:
				pass
			else:
				even=False
		if even==True:
			b.append(element)
	a = []
	a = [str(x) for x in b]
	print(",".join(a))