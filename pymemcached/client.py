#!/usr/bin/env python
import memcache
import os
import sys
import time

mc = memcache.Client(['127.0.0.1:11211'], debug = 1)


def getStatsInfo(mc):
    info = ""
    stats = mc.get_stats();
    for stat in stats:
       if len(info) > 0:
           info += '\n'
       info = info + "server: " + stat[0] 
       info = info + ', curr_items: '  + stat[1]['curr_items']
       info = info + ', bytes: '  + stat[1]['bytes']
       info = info + ', limit_maxbytes: '  + stat[1]['limit_maxbytes']
       percent = float(stat[1]['bytes'])/float(stat[1]['limit_maxbytes'])
       info = info + " " + str(percent)
    return info

def getValue(index):
   c =  chr(ord('a') + index%(ord('z') - ord('a') ))
   return c*1024
def getKey(index):
   return 'key_' + str(index)


#1 delete all 
mc.flush_all()
print "After flush all buf not try access: "   + getStatsInfo(mc)
#for i in range(0, 100*1024*1024):
#   mc.get(getKey(i));
#print "After flush all and try acccess all: "   + getStatsInfo(mc)


#2.create
num = 100*1024
for i in range(0,num):
    mc.set(getKey(i), getValue(i), 0);
for i in range(0, num):
   mc.get(getKey(i));
print "After set %s items : "%(num) + getStatsInfo(mc)

