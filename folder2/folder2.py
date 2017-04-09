import socket,os,datetime
import time
from threading import Thread
import threading
global ACKNo, seqNoOfReceivedPacket, noOfPacketsReceived,ackSentFlag
class Senderthread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        Thread.__init__(self)
        host = ""
        port = 60000 #the receiver send the acknowledgement on port 60000
        s = socket.socket() # for TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.connect((host, port))
        ackSentFlag=0
        while True:
            if ackSentFlag:
                print "The acknowledgement for the received packet number ", noOfPacketsReceived, "sent with acknowledgement number ",ACKNo
                s.send(ACKNo)
                ackSentFlag=0
            # command = raw_input("prompt:$ ")
            # arg=command.split()
            # # data = s.recv(1024)
            # if(command==""):
            #     continue

        print('Successfully get the file')
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        print('connection closed')

class Receiverthread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        port = 30000 #the receiver receives the packet on port 30000
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = ""

        s.bind((host, port))
        s.listen(5)
        conn, addr = s.accept()
        ackSentFlag
        while True:
            # print 'receiving.......'
            data=conn.recv(1024)
            if data:
                originalData=data
                data=data.split('~')
                seqNoOfReceivedPacket=int(data[1])
                ACKNo=seqNoOfReceivedPacket + len(data[0])
                noOfPacketsReceived+=1
                ackSentFlag=1
                print "Packet expecting with sequence number ",seqNoOfReceivedPacket
                print "Received packet number ",noOfPacketsReceived, "with sequence number ",seqNoOfReceivedPacket
                # conn.send(ACKNo)
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
