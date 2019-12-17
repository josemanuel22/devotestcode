
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
