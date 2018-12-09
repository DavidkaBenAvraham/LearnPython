# https://habr.com/post/149420/
# Эта программа создает 2 потока. В каждом потоке она пишет в отдельный файлик по пол миллиона строк “1”.

from threading import Thread

def writer(filename, n):
    with open(filename, 'w') as fout:
        for i in xrange(n):
            print >> fout, 1

t1 = Thread(target=writer, args=('test2.txt', 500000,))
t2 = Thread(target=writer, args=('test3.txt', 500000,))

t1.start()
t2.start()
t1.join()
t2.join()
