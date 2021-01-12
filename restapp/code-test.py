from threading import Thread
import time


class myThread(Thread):
    def __init__(self, email):
        Thread.__init__(self)
        self.email = email

    def run(self):
        print('before sleep')
        time.sleep(6)
        print(f'email: {self.email}')


thread1 = myThread("aaaa")
thread1.start()

print('test')
