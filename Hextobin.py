def hextobin(chaine):
	rang = 0
	res = 0
	liste = "0123456789ABCDEF"
	for i in reversed(chaine):
		for j in range(16):
			if i == liste[j]:
				res += j*16**rang
				rang += 1
	v = ""
	if res < 2:
		return str(res)
	while res > 0:
		v += str(res%2)
		res //= 2
	return v[::-1]
print(hextobin("CAF"))