#!/usr/bin/env python
import memcache
import os
import sys
import time
import commands
import subprocess
import signal
from multiprocessing import Process
import pylibmc


use_pylibmc =  True
def getClient(ports):
    srvs = []
    for i in ports:
       #srvs.append(('127.0.0.1:%d'%(i+20000), 100))
       srvs.append('127.0.0.1:%d'%(i+20000))
    mc = None
    if use_pylibmc:
         mc = pylibmc.Client(srvs, 
                        binary=True, 
                        behaviors={"tcp_nodelay": True,   "ketama": True})
    else:
        mc =   memcache.Client(srvs, debug =1)
    return mc

def startSrvs(ports):
    for i in  ports:
        cmd = "/usr/bin/memcached  -m 64 -p %d -u memcache -l 127.0.0.1"%(20000 + i)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn = os.setsid)
        #all_srv.append(p)

def createData(ports, nData):
    mc = getClient(ports)
    for i in range(0, nData):
      mc.set(str(i), str(i))
    mc.disconnect_all()

def hitData(ports, nData):
    hit  = 0
    mc = getClient(ports)
    for i in range(0, nData):
       if mc.get(str(i))  != None:
           hit =  hit + 1
    mc.disconnect_all()
    return hit

def dumpSrvInfo(ports):
    mc = getClient(ports)
    for stat in mc.get_stats():
       print stat[0]  + '  curr_items=' +  stat[1]['curr_items']
    mc.disconnect_all()

def testScale(numOfSrv = 5, numOfData = 10*1000):
    global all_srv
    assert numOfSrv >= 3
    startSrvs(range(0,numOfSrv))
    time.sleep(1)
    createData(range(0,numOfSrv-1), numOfData)
    dumpSrvInfo(range(0,numOfSrv))
    hit = hitData(range(0,numOfSrv-2), numOfData)
    hit =  float(hit)/float(numOfData)*100
    print "scale in hit %f"%(hit)
    hit = hitData(range(0,numOfSrv), numOfData)
    hit =  float(hit)/float(numOfData)*100
    print " scale out  %f"%(hit)
    commands.getstatusoutput('pkill -9  memcached')

if __name__ == '__main__':
   commands.getstatusoutput('pkill -9  memcached')
   use_pylibmc = True
   testScale(4, 10*1000)
   use_pylibmc =  False
   testScale(4, 10*1000)

