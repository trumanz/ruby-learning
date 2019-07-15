#!/usr/bin/env python
import unittest
import redis
import time
from rediswrapper import RedisWrapper
from redis.exceptions import ConnectionError
from redis.exceptions import ResponseError

class DateType(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      cls.redisSvc = RedisWrapper(200)
      cls.redisSvc.startServer()
      cls.rcli = redis.StrictRedis(host=cls.redisSvc.getServerIP(), port=6379, db=0)
   @classmethod
   def tearDownClass(cls):
      cls.redisSvc.stopServer() 

   def test_Strings(self):
      cli = DateType.rcli

      cli.set('test:foo', 'value')
      self.assertEqual(cli.get('test:foo'), 'value')

      cli.set('test:foo', 'newvalue')
      self.assertEqual(cli.get('test:foo'), 'newvalue')

      cli.delete("test:foo")
      self.assertEqual(cli.get('test:foo'), None)

   def test_Expire(self):
      cli = DateType.rcli
     
      cli.set('test:foo', 'value', ex=1)
      self.assertEqual(cli.get('test:foo'), 'value')
  
      time.sleep(1)
      self.assertEqual(cli.get('test:foo'), None)

   def test_Lists(self):
      cli = DateType.rcli
      cli.rpush("test:foolist", "val1")
      cli.rpush("test:foolist", "val2")
      cli.lpush("test:foolist", "val3")
      self.assertEqual(cli.lrange("test:foolist", 0, 2),  ['val3', 'val1', 'val2'] )

      self.assertEqual(cli.lpop("test:foolist"), 'val3')
      self.assertEqual(cli.lrange("test:foolist", 0, 2),  [ 'val1', 'val2'] )

      cli.delete("test:foolist")

   def test_Sets(self):
      cli = DateType.rcli
      cli.sadd("test:fooset", "val1")
      cli.sadd("test:fooset", "val1")
 
      self.assertEqual(cli.scard("test:fooset"), 1)
      self.assertEqual(cli.sismember("test:fooset", "val1"), True)
      self.assertEqual(cli.sismember("test:fooset", "val2"), False)

      cli.sadd("test:fooset", "2")

      cli.sadd("news:1000:tags", 1, 2, 3)
      self.assertEqual(cli.smembers("news:1000:tags"), set(['1', '2', '3']))

      self.assertEqual(cli.sinter("news:1000:tags", "test:fooset"), set(['2']))
      self.assertEqual(cli.sunion("news:1000:tags", "test:fooset"), set(['1', '2', '3', 'val1']))

      cli.delete("test:fooset") 
      cli.delete("test:1000:tags") 

   def test_SortedSets(self):
      cli = DateType.rcli
      cli.zadd('my-key', 5.5, 'a1', 6.6, 'b2', c3=3.3, d4=4.4)
      self.assertEqual(cli.zcard('my-key'), 4)
      self.assertEqual(cli.zcount('my-key', 3.3, 4.4), 2)
      self.assertEqual(cli.zcount('my-key', 3.3, 4.4), 2)
      self.assertEqual(cli.zrange('my-key', 0, 1), ['c3', 'd4'])
      self.assertEqual(cli.zrangebyscore('my-key', 3.3, 4.4), ['c3', 'd4'])


      cli.zadd('my-key', 1.0, 'a1', 1.0, 'b2', c3=1.0, d4=1.0)
      self.assertEqual(cli.zrangebylex('my-key', "[b", "[d"), ['b2', 'c3'])
      
   def test_Hashes(self):
       
       pass

   def test_BitArray(self):
       pass

   def test_HyperLogLogs(self):
       pass





if __name__ == '__main__':
    unittest.main(verbosity=2)

