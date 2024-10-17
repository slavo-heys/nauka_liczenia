import threading
import time
from nauka_liczenia import Program

class Program:
    def __init__(self):
       self.i = 0
       self.start()

    def start(self):
       for self.i in range(30):
          print(self.i)
          time.sleep(1)

class MyThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      print("Starting " + self.name)    
      print_time(self.name, self.counter, 1)
      
      
def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1
      start = Program()
      print("%s: %s" % ("Koniec", time.ctime(time.time())))
      
threads = []

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
# thread2 = MyThread(2, "Thread-2", 2)

# Start the new Threads
thread1.start()
# thread2.start()

# Join the threads
thread1.join()
# thread2.join()

print("Exiting Main Thread")