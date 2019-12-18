# Devotestcode

##Setups

I have tested the code both on my personal computer and on a ubuntu 18.04.3 VM. The code provided only uses packages from the standard python3 library. However, we include a requirements.txt if necessary. If a ModuleNotFoundError error appears, remember to add the path to the PYTHONPATH variable so that the compiler can find the modules. That is, add the devotestcode folder to the path.

```
export PYTHONPATH=route_to_devotestcode/devotestcode
```

## Palindromes

In module palindrome we write an efficient algorithm to check if a string is a palindrome. The function that checks if a number is palindrome is in the src folder. In this function we simply verify that the initial half of the character string matches the final half read backwards. If a string of characters is palindrome then n / 2 comparisons will have to be made. Therefore the complexity is O(n), where n is the number of characters in the string.

```
def is_palindrome(string):
    i=0
    n=int(len(string)/2)
    for letter in string[0:n-1]:
        i+=1
        if letter != string[-i]:
            return False
    return True
```

### Run tests

To run the tests be sure to be located in the directory /devotestcode/kcomplementary . Run it the following way:
```
python3 tests/palindrome_tests.py
``` 

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

### Run tests

To run the tests be sure to be located in the directory /devotestcode/kcomplementary . Run it the following way:
```
python3 tests/kcomplementary_tests.py
``` 


## Term frequency / Inverse document frequency (Tf/idf)

We assume that we have a directory D containing a document set S, with one file per document. Documents will be added to that directory by external agents, but they will never be removed or overwritten. We are given a set of terms TT, and we compute the tf/idf of TT for each document in D, and report the N top documents sorted by relevance. 
The program must run as a daemon/service that is watching for new documents, and dynamically updates the computed tf/idf for each document and the inferred ranking. 

The program will run with the parameters: 

* The directory D where the documents will be written. 
* The terms TT to be analyzed. 
* The count N of top results to show. 
* The period P to report the top N.

We have divided the problem into three classes, the Tfidf class that calculates the tfidf of a document, the Documents class, which contains the documents to be analyzed and the top functionality and the App class responsible for dynamic updating. To calculate the top, what we have done is to insert in a priority queue based on the Tf / idf, the documents and then remove the n least priority elements. If the heap is complete the complexity of both extraction and insertion will be O(1) (regarding the number of documents). The Tf Idf calculation operations are done in linear time with respect to the number of characters that the documents have. In fact, we compare the terms of the document term to term with the term to be searched. That is, the tfidf operation will have complexity O(N*n) (where n is the maximum number of characters that appears in a document and N the number of documents) If we assume that N is bounded by a constant and (n>>N) then O(N*n)=O(n). Then at first to calculate the top we will have to calculate Tf / idf for each document. Then, the operation will be done in O(N2*n), With the assumption before, O(N^{2}*n)=O(n). The operation of calculation of the top in the successive updates will have a cost that will depend directly on the number of documents added. If documents are not added, the cost will therefore be O(1).

### Class Tfidf

```
class Tfidf:
    """
    Calculate Tfidf of a document
    """

    def is_term(self, t, document):
        """
        Check if a term t appears in a document
        :param t: term to search
        :param document: documento where to search the term
        :type t: String
        :type document: String
        :return: True if the term is in the document, if not False
        """
        matches=0
        with open(document) as f:
            for line in f:
                for word in line.split():
                    if word in t:
                        return True
        return False 

    def tf(self, t, document):
        """
        Calculate the tf of a term in a document
        :param t: term to search
        :param document: documento where to search the term
        :type t: String
        :type document: String
        :return: The tf of the term
        """
        matches=0
        with open(document) as f:
            for line in f:
                for word in line.split():
                    if word in t: 
                        matches+=1
        return matches

    def idf(self, t, documents):
        """
        Calculate the itf of a term of a list of documents
        :param t: term to search
        :param documents: list of documents where to search the term
        :type t: String
        :type documents: list of Strings
        :return: The tf of the term
        """
        i=0
        for d in documents:
            if self.is_term(t, d):
                i+=1
        return math.log((len(documents)+1)/(i+1)+1) #(i+1) so no /0, len(documents)+1) so no negative numbers, and +1 so no all 0 when the term is in all docs

    def tfidf(self, t, d, documents):
        return self.tf(t, d)*self.idf(t,documents)

```

### Class Documents

```
class Documents:
    """
    Class that stores documents and calculates the top.
    """
    def __init__(self, dirpath):
        self.dirpath=dirpath
        self.documents=list()
        self.tfidf=Tfidf()
        self.h=[]

    def refresh(self, t):
        """
        Refresh to check if there is a new document and calculates his tfidf.
        :param t: term to search
        :type t: String
        """
        temp=[]
        for r, d, f in os.walk(self.dirpath):
            for file in f:
                if '.txt' in file and self.dirpath+"/"+file not in self.documents:
                    self.documents.append(self.dirpath+"/"+file)
                    temp.append(file)
        for file in temp:
            heapq.heappush(self.h,(self.tfidf.tfidf(t,self.dirpath+"/"+file,self.documents),self.dirpath+"/"+file))

    def top(self, t, n):
        """
        Calculates the top n documents that matches the search t
        :param t: term to search
        :param n: top n
        :type t: String
        :type n: int
        :return: Top n documents tha matches the search t
        """
        self.refresh(t)
        return heapq.nlargest(n,self.h)

```

### Class App

```
class App:
    def __init__(self,dirpath,period, term, n, logfile=sys.stdout):
        self.documents=Documents(dirpath)
        self.period=period
        self.t=term
        self.n=n
        logging.basicConfig(level=logging.INFO, format="%(message)s")
        if logfile==sys.stdout:
            f_handler = logging.FileHandler(logging.StreamHandler(sys.stdout))
        else:
            f_handler = logging.FileHandler(logfile)
        self.logger=logging.getLogger()
        self.logger.addHandler(f_handler)

    def run(self):
         """
        Run a continous top n (specified in the constructor) search of the terms t in the documents specified in the constructor with period specified also in the constructor. 
        Print the result in sdout (can be modified).
        """
        while True:
            top = self.documents.top(self.t, self.n)
            for tfidf, doc in top:
                self.logger.info(str(tfidf)+" "+doc.split("/")[-1])
            time.sleep(self.period)

    def run_test(self):
        top = self.documents.top(self.t, self.n)
        for tfidf, doc in top:
            self.logger.info(str(tfidf)+" "+doc.split("/")[-1])   

````

### Read params

For reading params we use the python package argparse in the main section of the program.

```
    parser = argparse.ArgumentParser(description='computed tf/idf for each document and the inferred ranking')
    parser.add_argument('-d', metavar='path', type=str, help='The directory D where the documents will be written', required=True)
    parser.add_argument('-t', metavar='N', type=str, nargs='*', help='The terms TT to be analyzed', required=True)
    parser.add_argument('-n', metavar='N', type=int, help='The count N of top results to show', required=True)
    parser.add_argument('-p', metavar='N', type=int, help='The period P to report the top N in segs', required=True)


    args = parser.parse_args()
    terms = args.t[0].split()
```

### Creating the deamon

For creating the deamon we use a simple fork() (python threads do not work as we think they should work) so the the child process will be responsible for running the program while the main process will normally end. 
```
  newpid = os.fork()
    if newpid == 0:
        app=App(args.d, args.p, terms, args.n)
        app.run()

```

To end the child process, just run:
```
ps -e
```
Select the pid of the child process (easy to identify, if not use grep with a pipe) and then use the kill comand.


### Run the program

To run the program with our test documents be sure to be in the folder that the -d flag point to the following direction:
```
your_path_to/devotestcode/compute_tf_idf/tests/documents
```
For instance:
```
python3 ./src/compute_tf_idf.py -d "./compute_tf_idf/tests/documents" -t "freedom" -n 3 -p 10
```

### Run tests

To run the tests be sure to be located in the directory /devotestcode/compute_tf_idf . Run it the following way:
```
python3 tests/compute_tf_idf_tests.py
``` 

### Possible improvements

We could have improved the efficiency of the tfidf calculation by studying the implementation of the [Knuth Algorithm algorithm - Morris - Pratt](https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm).










