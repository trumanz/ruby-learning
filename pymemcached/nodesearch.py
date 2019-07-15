#!/usr/bin/env python 




def get(k,v):
   l = 0
   r = len(k) -1;

   if r == 0: 
      return k[0]
   if v >= k[r] or v < k[0]:
      return k[r]  
 
   #print l,r
   while (r - l) > 1:
      m = (l + r)/2
      if v  < k[m]:
        r = m
      else:
        l = m
   #   print l,r 

   #print "result %d"%(l)
   return k[l]


if __name__ == '__main__':
  k=[2, 10, 20, 50]
  print k
  assert  get(k, 3)  == 2
  assert   get(k, 11) == 10
  assert  get(k, 20) == 20
  assert  get(k, 50) == 50
  assert  get(k, 100) == 50
  assert  get(k, 1)  == 50

  k=[2]
  print k
  assert  get(k, 3)  == 2
  assert  get(k, 2)  == 2
  assert  get(k, 1)  == 2

  k=[2,5]
  print k
  assert  get(k, 1)  == 5
  assert  get(k, 2)  == 2
  assert  get(k, 3)  == 2
  assert  get(k, 5)  == 5
  assert  get(k, 6)  == 5
