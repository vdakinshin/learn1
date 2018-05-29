def get_summ(one, two, delimiter=' '):
	return str.upper(one) + str.upper(delimiter) + str.upper(two)

result = get_summ('HelLo','world!')
print(result)