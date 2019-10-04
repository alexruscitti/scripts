import semaphore_manager

def properUseCase():

    print('\nExample of proper semaphore use')
    lock1 = semaphore_manager.locksmith()
    lock1.lock()
    lock1.free()
    lock1.lock()
    lock1.lock(False) #non blocking
    lock1.free()
    lock1.printLog()

def improperUseCase():
    print('\nExample of improper semaphore use')
    lock2 = semaphore_manager.locksmith()
    lock2.lock()
    lock2.lock()
    lock2.free()
    lock2.lock(False) #non blocking
    lock2.lock()
    lock2.free()
    lock2.free()
    lock2.printLog()


def main():
    properUseCase()
    improperUseCase()

if __name__ == '__main__':
    main()