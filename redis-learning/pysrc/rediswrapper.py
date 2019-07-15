#!/usr/bin/env python

import commands

class RedisWrapper():
    def __init__(self, maxMemory):
        self.maxMemory = maxMemory
        self.dockerContainer = None
    def startServer(self):
        if self.dockerContainer == None:
           cmdstr = "docker run -d -i -t  -m %dmb  --memory-swap=%dmb  -e REDIS_MAX_MEMORY=%dmb  trumanz/redis /run-redis.sh"%(self.maxMemory*1.2, self.maxMemory*1.2, self.maxMemory)
           print cmdstr
           (status, output) = commands.getstatusoutput(cmdstr)
           if status != 0:
               raise NameError(output)
           self.dockerContainer = output  
        else:
           raise NameError("docker container already started");
    def stopServer(self):
        if self.dockerContainer != None:
             cmdstr = "docker rm -f  " + self.dockerContainer  
             print cmdstr
             (status, output) = commands.getstatusoutput(cmdstr)
             if status != 0:
               raise NameError(output)
             self.dockerContainer = None
           
    def getServerIP(self):
        if self.dockerContainer == None:
           raise NameError("docker container already started");
        else:
           cmdstr =  "docker inspect --format='{{ .NetworkSettings.IPAddress }}' "  +  self.dockerContainer
           (status, output) = commands.getstatusoutput(cmdstr)
           if status != 0:
               raise NameError(output)
           return output

         

