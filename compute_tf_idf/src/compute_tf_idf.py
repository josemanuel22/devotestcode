import math, heapq
import os, argparse, logging, time
import sys, multiprocessing
import logging

class Tfidf:

    def is_term(self, t, document):
        matches=0
        with open(document) as f:
            for line in f:
                for word in line.split():
                    if word in t:
                        return True
        return False 

    def tf(self, t, document):
        matches=0
        with open(document) as f:
            for line in f:
                for word in line.split():
                    if word in t: 
                        matches+=1
        return matches

    def idf(self, t, documents):
        i=0
        for d in documents:
            if self.is_term(t, d):
                i+=1
        return math.log((len(documents)+1)/(i+1)+1) #(i+1) so no /0, len(documents)+1) so no negative numbers, and +1 so no all 0 when the term is in all docs

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
            heapq.heappush(self.h,(self.tfidf.tfidf(t,self.dirpath+"/"+file,self.documents),self.dirpath+"/"+file))

    def top(self, t, n):
        self.refresh(t)
        return heapq.nlargest(n,self.h)

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
    app=App(args.d, args.p, terms, args.n)
    app.run()

    newpid = os.fork()
    if newpid == 0:
        app=App(args.d, args.p, terms, args.n)
        app.run()

