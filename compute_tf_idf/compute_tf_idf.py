import math, heapq
import os, argparse, logging, time
import daemon
import logging
import sys

class Tfidf:

    def is_term(self, t, document):
        matches=0
        with open(document) as f:
            for line in f:
                for word in line.split():
                    if t==word:
                        return True
        return False 

    def tf(self, t, document):
        matches=0
        with open(document) as f:
            for line in f:
                for word in line.split():
                    if t==word:
                        matches+=1
        return matches

    def idf(self, t, documents):
        i=0
        for d in documents:
            if self.is_term(t, d):
                i+=1
        return math.log(len(documents)/(i+1))

    def tfidf(self, t, d, documents):
        return self.tf(t, d)*self.idf(t,documents)


class Documents:

    def __init__(self, dirpath):
        self.dirpath=dirpath
        self.documents=list()
        self.tfidf=Tfidf()
        self.h=[]

    def refresh(self, t):
        temp=[]
        for r, d, f in os.walk(self.dirpath):
            for file in f:
                if '.txt' in file and self.dirpath+"/"+file not in self.documents:
                    self.documents.append(self.dirpath+"/"+file)
                    temp.append(file)
        for file in temp:
            heapq.heappush(self.h,(self.tfidf.tfidf(t[0],self.dirpath+"/"+file,self.documents),self.dirpath+"/"+file))

    def top(self, t, n):
        self.refresh(t)
        return heapq.nlargest(n,self.h)

class App:
    def __init__(self,dirpath,period, term, n):
        self.documents=Documents(dirpath)
        self.period=period
        self.t=term
        self.n=n

    def run(self):
        while True:
            top = self.documents.top(self.t, self.n)
            for tfidf, doc in top:
                print(str(tfidf)+" "+doc.split("/")[-1])
            time.sleep(self.period)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='computed tf/idf for each document and the inferred ranking')
    parser.add_argument('-d', metavar='path', type=str, help='The directory D where the documents will be written', required=True)
    parser.add_argument('-t', metavar='N', type=str, nargs='*', help='The terms TT to be analyzed', required=True)
    parser.add_argument('-n', metavar='N', type=int, help='The count N of top results to show', required=True)
    parser.add_argument('-p', metavar='N', type=int, help='The period P to report the top N in segs', required=True)

    args = parser.parse_args()
    app=App(args.d, args.p, args.t, args.n)
    app.run()
    #with daemon.DaemonContext():
    #    app.run()

    












