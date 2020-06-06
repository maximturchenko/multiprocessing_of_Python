
from multiprocessing import Process
import time


def count_down(name, delay):
    print('Process %s starting...' % name)

    counter = 5

    while counter:
        time.sleep(delay)
        print('Process %s counting down: %i...' % (name, counter))
        counter -= 1

    print('Process %s exiting...' % name)


if __name__ == '__main__':
    process1 = Process(target=count_down, args=('A', 25))
    process2 = Process(target=count_down, args=('B', 25))

    process1.start()
    process2.start()

    print('1 ' + str(process1.pid))
    print('2 ' + str(process2.pid))

    process1.join()
    process2.join()

    print('Done.')