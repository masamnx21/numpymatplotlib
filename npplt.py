if __name__=='__main__':
	#ask users for row and col numbers
	rows = int(input('how many rows? (between 1 and 5) '))
	cols = int(input('how many columns? (between 1 and 5) '))
	
	#total student name list
	
	all_names = ['Sasha', 'Jon', 'Martin', 'Elias', 'Basira', 'Bertie', 'Michael', 'Cel', 'Azu', 'Emily', 'Lizzie', 'Lillian', 'Carolyn', 
'Elizabeth', 'Rose', 'James', 'Albert', 'Hypatia', 'Copernicus', 'Kepler', 'Compton', 'Rosalind', 'Marie', 'Newton', 'Euler']

	#ensuring the proper number of names is used
	names = all_names[:rows*cols]
	
	#importing packages
	import numpy as np
	from numpy import random

	#generating randomly ordered names
	random_names = np.array([])

	i = len(names)
	while i > 0:
		x = random.randint(i)
		random_names = np.append(random_names, names[x])
		del names[x]
		i = i - 1
	
	#reshaping into requested seating chart shape
	chart = random_names.reshape(rows, cols)

	#printing seating chart
	for i in range(rows):
		listi = []
		for j in range(cols):
			listi.append(chart[i][j]+'('+str(i)+','+str(j)+')          ')

		print(listi)
