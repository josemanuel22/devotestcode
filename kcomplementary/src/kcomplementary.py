
def kcomplementary(array, k):
	"""
    Calculate the k-complementary of a array.
    :param array: array for which to calculate the k-complement 
    :param k: k complemetary
    :type array: list of numbers (int, float, double)
    :type k: number (int, float, double)
    :return: array of k-complementary of each position
    """
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
