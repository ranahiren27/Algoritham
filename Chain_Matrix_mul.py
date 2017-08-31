import math
import sys
import time
arr = []
b = 0
def MCM(i,j):
	if i == j:
		return 0
	m = sys.maxint
	for k in xrange(i,j):
		d = MCM(i,k) + MCM(k+1,j) +arr[i-1]*arr[k]*arr[j]
		m = min(m,d)
	return m 

def main():
	b = time.time()
	a = int(input("Enter number of Matrix:"))
	print("Enter Values of P\n")
	for c in range(a):
		v = int(input())
		arr.append(v)
	cost = MCM(1,a-1)
	print(cost)
	print ('total run time is:', time.time()-b)

if __name__ == '__main__':
    main()