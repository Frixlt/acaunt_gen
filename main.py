from my_function import pas
with open('a_gen.txt', 'r') as file:
	lost=int(file.readlines()[0])
acaunts={}
need_pas=int(input("сколько нужно акаунтов:"))
for i in range(need_pas):
	lost+=1
	acaunts[lost]=pas()+pas(1,'1234567890')
with open('a_gen.txt', 'w+') as file:
	file.write(str(lost)+"\n")
	for key, value in acaunts.items():
		file.write(f"{key}:{value}\n")
print("end!")