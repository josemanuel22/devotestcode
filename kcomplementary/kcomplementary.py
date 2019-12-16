
def kcomplementary(array, k):
	d=dict(); complements=list()
	for i in range(0,len(array)):
		complement=k-array[i]
		d[complement]=i
	for i in range(0,len(array)):
		if array[i] in d:
			complements.append(d[array[i]])
		else:
			complements.append(None)
	return complements

if __name__ == "__main__":
	print(kcomplementary([1,2,3,4],5))
	print(kcomplementary([2,0,3,5],5))
	print(kcomplementary([-1,6,3,7,0],6))
	print(kcomplementary([0,6,3,7,1],6))