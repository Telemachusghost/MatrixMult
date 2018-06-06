"""
A game that helps with matrix multiplication
Derick Falk
6/5/2018

"""

import numpy as np
import random as rd

def genmatrix(value, a = "", b = ""):
	if a:
		a = a
	else:
		a = rd.randint(1,5)
	if b:
		b = b
	else:
		b = rd.randint(1,5)
	matrix = []
	mx = np.random.rand(a,b)
	for i in mx:
		matrix.append((i*value).astype(int))
	return matrix




def main():
	wrong = True
	while wrong:
		rng = int(input("Please input a range for the elements in the matrices: "))
		a = genmatrix(rng)
		x = np.shape(a)[1]

		b = genmatrix(rng,a=x)
		# print(np.shape(b))
		print("*** Matrix A ***")
		print(f"{np.asmatrix(a)}")
		print(f"*** {np.shape(a)} ***\n")

		print("*** Matrix B ***")
		print(f"{np.asmatrix(b)}")
		print(f"*** {np.shape(b)} ***\n")

		ans = np.matmul(a,b)
		# print("*** A*B ***")
		# print(f"{np.matmul(a,b)}")
		# print(f"{np.shape(np.matmul(a,b))}\n")

		randrow = np.shape(a)[0] 
		randcol = np.shape(b)[1] 
		guess = input(f"What is the value in product A*B_{rd.randint(1,randrow)}{rd.randint(1,randcol)}? ")

		if int(guess) == ans[randrow-1][randcol-1]: 
			print(f"Correct answer {ans[randrow-1][randcol-1]}")
			wrong = False
			print("\n***A*B***")
			print(ans, "\n")
			playagain = input("Your Right!\nDo you want to play again y/n ").lower()
			if playagain == 'y' or playagain == 'yes':wrong = True
			else: 
				continue
		else:
			print(f"Correct answer {ans[randrow-1][randcol-1]}")
			print("***\n***")
			print(ans, "\n")
			playagain = input("Your Wrong!\nDo you want to play again y/n ").lower()
			if playagain == 'y' or playagain == 'yes':wrong = True
			else: 
				continue
if __name__=="__main__":
	main()
