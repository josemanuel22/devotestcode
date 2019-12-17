# Devotestcode

## Palindromes

In module palindrome we write an efficient algorithm to check if a string is a palindrome. The function that checks if a number is palindrome is in the src folder. In this function we simply verify that the initial half of the character string matches the final half read backwards. If a string of characters is palindrome then n / 2 comparisons will have to be made. Therefore the complexity is O (n), where n is the number of characters in the string.

## kcomplementary

In the module kcomplementay we write an efficient algorithm to find K-complementary pairs in a given array of integers.  Given Array A, pair (i, j) is K- complementary if K = A[i] + A[j]; 

The idea is that we want to avoid looping through the array again and again. 

* Go through the array once, and store in a Map the difference of the wanted sum and the current element mapped to how many times it occured. Effectively, this map remembers how much we're missing for an element at a given index so that the sum can be reached.

* Go through the array a second time, and check whether the map contains this element. If it does, then it means that our map contains an element e for which e = sum - arr[i], so it means that we've found a matching pair. And the number of matching pair we found, is the number of times this element appears in the array, which is the value of the map.

We return an array with the position in the complementary k-array for the element in that position. We begin to number the positions by zero. For example the 5-complementary of [1,2,3,4] is [3, 2, 1, 0]. In the event that an element does not have a complementary k we return None in that position.

```
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

```

Since the insertion and reading in a dictionary is linear, the complexity is linear with respect to the size of the array, i.e. O(n).
