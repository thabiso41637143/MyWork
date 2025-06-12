
n = int(input("Size: "))
dash_line = (n * 2) - 2
temp = (n - 1)
alp = chr(97 + temp)
c_list = alp
list_ch = []
list_lines = []
for i in range(1, n):
	print(f"{'-'*dash_line}{c_list}{'-'*dash_line}")
	list_lines.append(f"{'-'*dash_line}{c_list}{'-'*dash_line}")
	dash_line -= 2
	temp -= 1
	c_list = alp
	list_ch = [alp]
	for c in range((n - 2), (temp - 1), -1):
		c_list += '-' + chr(97 + c)
		list_ch.append(chr(97 + c))
	list_ch.reverse()
	c_list += '-'+ '-'.join(list_ch[1:])

print(c_list)
list_lines.reverse()
print('\n'.join(list_lines))

