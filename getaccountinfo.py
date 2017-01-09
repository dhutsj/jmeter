import multiprocessing
import requests
import datetime
import time
import json
import login
import global_config

token_req=login.url_request('https://api.btcchina.com/api.php/account/authenticate/')


r = requests.post(token_req.url, headers=global_config.Login_headers)
print r.headers.get('Last-Modified')

Getaccount_headers= {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Json-Web-Token": r.headers.get('Last-Modified')

        }
print Getaccount_headers
