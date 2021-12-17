import string

cipher = "wbusckgocywo"
solution = []

for i in range(26):
	solution = ''
	for char in cipher:
		if char in string.ascii_lowercase:
			index = string.ascii_lowercase.index(char) - i
			solution = solution + string.ascii_lowercase[index]
	print(solution)


				

