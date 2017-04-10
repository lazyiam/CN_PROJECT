import socket,os,datetime
import time
from threading import Thread
import threading
from random import randint
ACKNo = 0
seqNoOfReceivedPacket = 0
noOfPacketsReceived =0
ackSentFlag = 0
lastACKNo=1
# senttill
class Senderthread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global lastACKNo
        Thread.__init__(self)
        host = ""
        port = 60000 #the receiver send the acknowledgement on port 60000
        s = socket.socket() # for TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((host, port))
        # global ackSentFlag
        # ackSentFlag=0
        s.listen(5)
        conn ,addr = s.accept()
        while True:
            global ACKNo,noOfPacketsReceived
            global ackSentFlag
            # if str(ACKNo)=='5':
            #     continue
            if ackSentFlag:
                if seqNoOfReceivedPacket==lastACKNo:
                    print "The acknowledgement for the received packet number ", noOfPacketsReceived, " sent with acknowledgement number ",ACKNo, '\n', '\n','\n'
                    p = randint(0,15)
                    # if p !=3:
                    conn.send(str(ACKNo))
                    # else:
                    #     print "missed for ",ACKNo
                    #     time.sleep(1.5)
                    lastACKNo=ACKNo
                    ackSentFlag=0
                    print "downloaded -->",lastACKNo
                else:
                    print "Didn't get what receiver expected. Sending the last received acknowledgement number ", lastACKNo, '\n', '\n','\n'
                    conn.send(str(lastACKNo))
                    ackSentFlag=0
            # command = raw_input("prompt:$ ")
            # arg=command.split()
            # # data = s.recv(1024)
            # if(command==""):
            #     continue

        print('Successfully get the file')
        # s.shutdown(socket.SHUT_RDWR)
        conn.close()
        print('connection closed')

class Receiverthread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global ackSentFlag
        port = 30000 #the receiver receives the packet on port 30000
        s = socket.socket()
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = ""

        s.connect((host, port))
        # s.listen(5)
        # conn, addr = s.accept()
        ackSentFlag = 0
        while True:
            # print 'receiving.......'
            data=s.recv(1024)
            print "data= ",data
            # print "next data"
            # print "Data received on the end of folder2.py",data
            global ACKNo,seqNoOfReceivedPacket,noOfPacketsReceived
            if data:
                originalData=data
                # data=data.split('~')
                seqNoOfReceivedPacket=int(data)
                ACKNo=seqNoOfReceivedPacket + 1
                noOfPacketsReceived+=1
                print "Packet expecting with sequence number ",seqNoOfReceivedPacket, '\n'
                print "Received packet number ",noOfPacketsReceived, " with sequence number ",seqNoOfReceivedPacket, '\n'
                ackSentFlag=1
                # conn.send(ACKNo)
            # print "data:",data
        # s.shutdown(socket.SHUT_RDWR)
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
   # myThreadOb1.join()
   # myThreadOb2.join()

   # print('Main Terminating...')
