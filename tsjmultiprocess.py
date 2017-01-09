import multiprocessing
import requests
import datetime
import time

class url_request():
    times = []
    error = []
    def __init__(self,url):
        self.url=url
        #print "Get Url" % url
    def req(self):
        myreq=url_request
        r = requests.get(self.url)
        ResponseTime = float(r.elapsed.microseconds) / 1000
        myreq.times.append(ResponseTime)
        if r.status_code != 200:
            myreq.error.append("0")

if __name__ == "__main__":
    myreq = url_request('https://www.btcchina.com')
    nub = 10
    starttime = datetime.datetime.now()
    p = multiprocessing.Pool()
    for i in range(1,nub+1):
        p.apply_async(myreq.req())
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    endtime = datetime.datetime.now()
    print 'All subprocesses done.'
    AverageTime = "{:.3f}".format(float(sum(myreq.times)) / float(len(myreq.times)))
    print len(myreq.times)
    print "Average Response Time %s ms" % AverageTime