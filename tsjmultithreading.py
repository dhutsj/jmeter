import requests
import datetime
import time
import threading
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
if __name__ == '__main__':
    myreq = url_request('https://www.btcchina.com')
    threads = []
    starttime = datetime.datetime.now()
    print "request start time %s" % starttime
    nub = 10
    ThinkTime = 0.5
    for i in range(1, nub + 1):
        t = threading.Thread(target=myreq.req)
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print "request end time %s" % endtime
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times)) / float(len(myreq.times)))
    print "Average Response Time %s ms" % AverageTime
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour) * 60 * 60 + float(minute) * 60 + float(second)
    print "Concurrent processing %s" % nub
    print "use total time %s s" % (totaltime - float(nub * ThinkTime))
    print "fail request %s" % myreq.error.count("0")