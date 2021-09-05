import time
import threading


class 儿童锁:
    def __init__(self, 时间限制=3):
        self.时间限制 = 时间限制
        self._锁 = threading.Lock()
        self.初次接触时间 = 0
        self.上次接触时间 = 0
    def 上锁(self):
        self._锁.acquire()
    def 解锁(self):
        now = time.time()
        if now - self.上次接触时间 > 0.1:
            self.初次接触时间 = now
            self.上次接触时间 = now
            return True
        if now - self.初次接触时间 > self.时间限制:
            self._锁.release()
            return False
        self.上次接触时间 = now
        return True


l = 儿童锁()

l.上锁()

print(l._锁.locked())

l.解锁()

while l.解锁(): 
    time.sleep(0.01)

print(l._锁.locked())
