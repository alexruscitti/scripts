import sys
import threading
import inspect

semaphore = threading.Semaphore()

class locksmith:
    def __init__(self):
        self.log = []
        self.semaphore = threading.Semaphore()
        self.success = 'FAIL'
        self.calframe = None

    def lock(self, blocking = True, timeout = 1):
        self.calframe = inspect.stack()[1][3]    
        self.success = 'FAIL'
        if blocking:        
            if semaphore.acquire(blocking, timeout):
                self.success = 'SUCCESS'
            self.log.append([self.calframe, 'Blocking LOCK' , self.success])
        elif not blocking:
            if semaphore.acquire(False):
                self.success = 'SUCCESS'
            else:
                self.success = 'PASS'
            self.log.append([self.calframe, 'Non-Blocking LOCK' , self.success])
        else:
            print('Invalid Semaphore blocking parameter. Closing.')
            sys.exit(1)
        return self.success == 'SUCCESS' or self.success == 'PASS'

    def free(self):
        self.success = 'SUCCESS'
        if semaphore.acquire(False): #Let's see if there's a semaphore currently acquired
            self.success =  'PASS'   #If this succeeds, there was no semaphore acquired, so the free 'passes'
        semaphore.release()
        self.log.append([self.calframe, 'FREE' , self.success])

        return self.success == 'SUCCESS' or self.success == 'PASS'

    def printLog(self):
        print('Semaphore log: ') # semaphore self.log format [calling function, acquire or release, result]
        print('Calling Function |Lock or Free     |Status           |')
        print('======================================================')
        for row in self.log:
            for item in row:
                print('{0: <17}|'.format(item), end='')
            print('')
        self.success = 'SUCCESS'
        return True

    def getLog(self):
        return self.log