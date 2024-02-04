def prime(number):
		for i in number:
			if i >= 2:
				size = (i // 2) + 1
				for j in range(2,size,1):
					if i % j == 0:
						return False
			return True
def result(number):
	newnum = []
	for i in number:
		solution = prime(i)
		if solution:
			newnum.append(i)
	print(newnum)
def num():
		newlist = []
		n = int(input("size:"))
		for i in range(n):
			num = int(input("num:"))
			newlist.append(num)
		result(newlist)

num()
		
