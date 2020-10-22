# 0
# 1
# 0
# 1
# 0
# 1
# using nested while loop

i = 0
while(i<3):
	j = 0
	while(j<2):
		print(j)
		j = j+1
	i = i+1

# 1st pass
# i =0

# 0<3 True
# 	j = 0
# 	0 < 2 True
# 		print(j) -> 0
# 		j = j+1 -> 1

# 	1 < 2 True
# 		print(j) -> 1
# 		j = j+1	-> 2

# 	2 < 2 False loop ended
# 	i = i + 1 -> 1
# 1<3 True
# 	j = 0
# 	0 < 2 True
# 		print(j) -> 0
# 		j = j+1 -> 1

# 	1 < 2 True
# 		print(j) -> 1
# 		j = j+1	-> 2

# 	2 < 2 False loop ended
# 	i = i + 1 -> 2

# 2<3 True
# 	j = 0
# 	0 < 2 True
# 		print(j) -> 0
# 		j = j+1 -> 1

# 	1 < 2 True
# 		print(j) -> 1
# 		j = j+1	-> 2

# 	2 < 2 False loop ended
# 	i = i + 1 -> 3

# 3<3 False Loop ended
