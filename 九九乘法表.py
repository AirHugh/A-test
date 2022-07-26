# a = 1
# b = 1
# while a <= 9:
# 	if a >= b:
# 		print("%d * %d = %d"%(b,a,a*b),end = "\t")
# 		b += 1
# 	else:
# 		print()
# 		a += 1
# 		b = 1

#2.0版
a = 1 
while a <= 9:
	b = 1
	while b <= a:
		print("%d * %d = %d"%(b,a,a*b),end="\t")
		b += 1
	print()
	a += 1
#第二版直接少了两行，真不戳