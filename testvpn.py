# -*- coding: utf-8 -*-
"""
Created on 2017-04-29 23:57 

@author: home 
"""
import dns.resolver
from python_ping.ping import *
import os
inputstr = open('vpn.txt')
str1 = inputstr.readlines()
ip_dict = dict()

for line in str1:
    try:
        host = line.strip('\r\n')
        a = dns.resolver.query(host)
        for i in a.response.answer:
            for j in i.items:
                ip = j.address
                p = Ping(ip)
                p.run(1)
                if p.receive_count > 0:
                    delay = p.total_time / p.receive_count
                    print delay
                    ip_dict[ip] = delay
    except:
        continue
sdict = sorted(ip_dict.iteritems(), key=lambda d:d[1], reverse = False)
for item in sdict:
    print("%s,%0.1f" % (item[0], item[1]))

os.system("pause")