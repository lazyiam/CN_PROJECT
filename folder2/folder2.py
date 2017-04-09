import socket,os,datetime
import time
from threading import Thread
import threading
global modified_files
class Senderthread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):

class Receiverthread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):

if __name__ == '__main__':
   # Declare objects of Serverthread class
   myThreadOb1 = Serverthread()

   myThreadOb2 = Clientthread()

   # Start running the threads!
   myThreadOb1.start()
   time.sleep(10)
   myThreadOb2.start()

   # Wait for the threads to finish...
   myThreadOb1.join()
   myThreadOb2.join()

   print('Main Terminating...')
