import math, heapq
import os, argparse, logging, time
import sys, multiprocessing
import logging

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

class App:
    def __init__(self,dirpath,period, term, n, logfile=sys.stdout):
        self.documents=Documents(dirpath)
        self.period=period
        self.t=term
        self.n=n
        if logfile is not sys.stdout:
            logging.basicConfig(level=logging.INFO, format="%(message)s")
            f_handler = logging.FileHandler(logfile)
            self.logger=logging.getLogger()
            self.logger.addHandler(f_handler)
        else:
            logging.basicConfig(level=logging.INFO, format="%(message)s")
            self.logger=logging.getLogger()
        


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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='computed tf/idf for each document and the inferred ranking')
    parser.add_argument('-d', metavar='path', type=str, help='The directory D where the documents will be written', required=True)
    parser.add_argument('-t', metavar='N', type=str, nargs='*', help='The terms TT to be analyzed', required=True)
    parser.add_argument('-n', metavar='N', type=int, help='The count N of top results to show', required=True)
    parser.add_argument('-p', metavar='N', type=int, help='The period P to report the top N in segs', required=True)


    args = parser.parse_args()
    terms = args.t[0].split()

    newpid = os.fork()
    if newpid == 0:
        app=App(args.d, args.p, terms, args.n)
        app.run()

