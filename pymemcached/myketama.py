#!/usr/bin/env python
import sys
from binascii import crc32
import hashlib

def myhash(key):
    d =   hashlib.md5(key).hexdigest()
    return  [int(d[0:8], 16), int(d[8:16], 16), int(d[16:24], 16), int(d[24:32], 16)]
    return  ((crc32(key) & 0xffffffff  >> 16) & 0x7fff) or 1
    
class SRV:
    def __init__(self, addr):
         self.addr = addr
         self.keys = set()
         self.real_weight = 0
    def __str__(self):
         return  self.addr  +  ", has "  + str(len(self.keys))
    def __repr__(self):
         return str(self)

srvs = []
srvs_points = []


def getSrv(key):
   l = 0
   r = len(srvs_points) -1;
   v = myhash(key)[0]
   if r == 0: 
      return k[0]
   if v >= srvs_points[r][0] or v < srvs_points[0][0]:
      return srvs_points[r][1]
   while (r - l) > 1:
      m = (l + r)/2
      if v  < srvs_points[m][0]:
        r = m
      else:
        l = m
   return srvs_points[l][1]
       
def addSrv(addr):
  s = SRV(addr)
  srvs.append(s) 
  for i in range(0,40):
     haddr = addr + '-' + str(i) 
     hcode = myhash(haddr)
     for h  in hcode:
        srvs_points.append((h, s))
  srvs_points.sort(lambda p1, p2 : cmp(p1[0], p2[0]))

def delSrv(addr):
   global srvs_points
   tmp = [x for x in  srvs_points if x[1].addr != addr  ]
   srvs_points = tmp

if __name__ == '__main__':
   srvaddrs = ['SRV_A', 'SRV_B', 'SRV_C']
   for addr in srvaddrs:
      addSrv(addr)

   for key in range(0, 10*1000):
        s = getSrv(str(key))
        s.keys.add(key)
   print "After set 10K  in 3 server"
   print "len of  srvs_points=%d"%(len(srvs_points))
   print srvs
   print "Test Add one Server"
   addSrv('SRV_D')
   print "len of  srvs_points=%d"%(len(srvs_points))
   hit = 0
   for key in range(0, 10*1000):
       s  = getSrv(str(key))
       if key in s.keys:
          hit = hit+1
   print " hit=%d"%(hit)

   print "Test del one Server"
   delSrv('SRV_D')
   delSrv('SRV_C')
   print "len of  srvs_points=%d"%(len(srvs_points))
   hit = 0
   for key in range(0, 10*1000):
       s  = getSrv(str(key))
       if key in s.keys:
          hit = hit+1
   print " hit=%d"%(hit)
