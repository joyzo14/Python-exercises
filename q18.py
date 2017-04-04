"""
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""

def validPasswords(word):
	a=word.split(",")
	b=[]
	for item in a:
		if re.search(r'[a-z]',item)==None:
			continue
		if re.search(r'[A-Z]',item)==None:
			continue
		if re.search(r'[0-9]',item)==None:
			continue
		if re.search(r"[$#@]",item)==None:
			continue
		if len(item)<6 or len(item)>12:
			continue
		b.append(item)
	b=",".join(b)
	print(b)