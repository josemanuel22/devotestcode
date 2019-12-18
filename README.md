# Devotestcode

## Palindromes

In module palindrome we write an efficient algorithm to check if a string is a palindrome. The function that checks if a number is palindrome is in the src folder. In this function we simply verify that the initial half of the character string matches the final half read backwards. If a string of characters is palindrome then n / 2 comparisons will have to be made. Therefore the complexity is O(n), where n is the number of characters in the string.

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

## Term frequency / Inverse document frequency (Tf/idf)

We assume that we have a directory D containing a document set S, with one file per document. Documents will be added to that directory by external agents, but they will never be removed or overwritten. We are given a set of terms TT, and we compute the tf/idf of TT for each document in D, and report the N top documents sorted by relevance. 
The program must run as a daemon/service that is watching for new documents, and dynamically updates the computed tf/idf for each document and the inferred ranking. 

The program will run with the parameters: 

* The directory D where the documents will be written. 
* The terms TT to be analyzed. 
* The count N of top results to show. 
* The period P to report the top N.

We have divided the problem into three classes, the Tfidf class that calculates the tfidf of a document, the Documents class, which contains the documents to be analyzed and the top functionality and the App class responsible for dynamic updating. To calculate the top, what we have done is to insert in a priority queue based on the Tf / idf, the documents and then remove the n least priority elements. If the heap is complete the complexity of both extraction and insertion will be O(1) (regarding the number of documents). The Tf Idf calculation operations are done in linear time with respect to the number of characters that the documents have. In fact, we compare the terms of the document term to term with the term to be searched. That is, the tfidf operation will have complexity O(N*n) (where n is the maximum number of characters that appears in a document and N the number of documents) If we assume that N is bounded by a constant and (n>>N) then O(N*n)=O(n). Then at first to calculate the top we will have to calculate Tf / idf for each document. Then, the operation will be done in O(N2*n), With the assumption before, $O(N^{2}*n)=O(n)$.









