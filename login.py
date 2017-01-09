import multiprocessing
import requests
import datetime
import time
import json
import global_config


class url_request():
    times = []
    error = []

    def __init__(self, url):
        self.url = url

    def req(self):
        myreq = url_request

        headers = global_config.Login_headers

        r = requests.post(self.url, headers=headers)
        print r.headers.get('Last-Modified')
        print r.headers
        print r.text
        print r.content
        ResponseTime = float(r.elapsed.microseconds) / 1000
        myreq.times.append(ResponseTime)
        if r.status_code != 200:
            print "Request Fail! Error code %d" % r.status_code
            myreq.error.append("0")


if __name__ == "__main__":
    myreq = url_request('https://api.btcchina.com/api.php/account/authenticate/')
    nub = 1
    starttime = datetime.datetime.now()
    p = multiprocessing.Pool()
    for i in range(1, nub + 1):
        p.apply_async(myreq.req())
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    endtime = datetime.datetime.now()
    print 'All subprocesses done.'
    AverageTime = "{:.3f}".format(float(sum(myreq.times)) / float(len(myreq.times)))
    print len(myreq.times)
    print "Average Response Time %s ms" % AverageTime
