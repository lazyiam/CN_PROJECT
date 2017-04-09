import socket,os,datetime
import time
from threading import Thread
import threading
global lastACKNo, seqNo, windowSize, t_out
class Senderthread(Thread): #sender is my client
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        f = open(filename,'rw+')
        def sendPacket(packet_number):
            offset = packet_number*1024
            f.seek(offset,1);
        def sendWindow(win_off_pack):
            for i in range(win_off_pack,win_off_pack+windowSize):
                sendPacket(i)




        host = ""
        port = 30000
        s = soc ket.socket() # for TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.connect((host, port))
        windowSize=raw_input("Enter window size: ")
        t_out=raw_input("Enter timeout interval: ")
        numberOfPackets=raw_input("Enter number of pacekts to be sent: ")

        iteratorOnPacketNumber=0
        while iteratorOnPacketNumber<=numberOfPackets:
            print "Sending", iteratorOnPacketNumber "......."
            sendPackets(iteratorOnPacketNumber)
            iteratorOnPacketNumber+=1
            # command = raw_input("prompt:$ ")
            # arg=command.split()
            # # data = s.recv(1024)
            # if(command==""):
            #     continue

        print('Successfully get the file')
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        print('connection closed')

class Receiverthread(Thread): #receiver is my server sort of......
    def __init__(self):
        # print "Hello"
        Thread.__init__(self)

    def run(self):
        port = 60000
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = ""

        s.bind((host, port))
        s.listen(5)
        conn, addr = s.accept()
        while True:
            # print 'receiving.......'
            data=conn.recv(1024)
            originalData=data
            data=data.split()
            # print "data:",data
        s.shutdown(socket.SHUT_RDWR)
        s.close()

if __name__ == '__main__':
   # Declare objects of Serverthread class
   myThreadOb1 = Senderthread()

   myThreadOb2 = Receiverthread()

   # Start running the threads!
   myThreadOb1.start()
   time.sleep(10)
   myThreadOb2.start()

   # Wait for the threads to finish...
   myThreadOb1.join()
   myThreadOb2.join()

   # print('Main Terminating...')
