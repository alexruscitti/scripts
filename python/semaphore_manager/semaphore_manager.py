import sys
import threading

semaphore = threading.Semaphore()

def semaphoreManager(self, condition, blocking = True, timeout = 1): # semaphore management function, all acquries and releases are logged
    calframe = inspect.stack()[1][3]                            # calframe is the name of the function that called the semaphore
    success = 'FAIL'
    if condition == LOCK:                                       
        if blocking:        
            if semaphore.acquire(blocking, timeout):
                success = 'SUCCESS'
            self.log.append([calframe, 'Blocking ' + condition, success])
        elif not blocking:
            if semaphore.acquire(False):
                success = 'SUCCESS'
            self.log.append([calframe, 'Non-Blocking ' + condition, success])
        else:
            print('Invalid Semaphore blocking parameter. Closing.')
            sys.exit(1)

    elif condition == FREE:
            semaphore.release()
            success =  'SUCCESS'
            self.log.append([calframe, condition, success])

    elif condition == LOG:
        print('\nSemaphore Log: ') # semaphore log format [calling function, acquire or release, result]
        for i in self.log:
            for j in i:
                print('{0: <16}|'.format(j), end='')
            print('')
        success = 'SUCCESS'
    else:
        print('Invalid semaphore condition parameter. Closing.')
        sys.exit(1)
    return True if success == 'SUCCESS' else False