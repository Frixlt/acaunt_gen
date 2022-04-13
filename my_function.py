import random
def pas(long=8,dict=False):
	if dict == False:
		dict ='1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'
	new_pas =''
	for i in range(long):
		new_pas+=random.choice(list(dict))
	return new_pas
def max(f):
    with open(f, 'r') as file:
        lines = 0
        for line in file.readlines():
            lines += 1
    return lines