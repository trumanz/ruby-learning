#!/usr/bin/env python
import unittest
import redis
import time
from rediswrapper import RedisWrapper
from redis.exceptions import ConnectionError
from redis.exceptions import ResponseError

class TestMem(unittest.TestCase):
   def test_mem(self):
      redisSvc = RedisWrapper(40)
      redisSvc.startServer();
 
      r = redis.StrictRedis(host=redisSvc.getServerIP(), port=6379, db=0)
      str1K = '0123456789'*100;
      str1M = str1K*1000;

      respErr = False
      try:
         for i in range(0, 50):
            print i
            r.set(i, str1M)
            #print r.get(i)
      except  ResponseError as e:
           respErr = True
      self.assertEqual(respErr, True)
      print r.client_list();
  
      redisSvc.stopServer()    
      

if __name__ == '__main__':
    unittest.main()

