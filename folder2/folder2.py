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
someflag=0
breakflag=0
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
        global someflag,breakflag
        while True:
            if breakflag==1:
                break
            global ACKNo,noOfPacketsReceived
            global ackSentFlag
            # if str(ACKNo)=='5':
            #     continue
            if ackSentFlag:
                if seqNoOfReceivedPacket==lastACKNo:
                    print "ACK for correctly recieved packet sent with ACK no.= ",ACKNo
                    p = randint(0,15)
                    lastACKNo=ACKNo
                    ackSentFlag=0
                    if p !=3:
                        conn.send(str(ACKNo))
                    else:
                        print "ACK sent but lost during propogation with ACK no.= ",ACKNo
                        someflag = 1
                        time.sleep(1.5)
                        someflag=0
                    print "downloaded -->",lastACKNo-1, '\n','\n'
                else:
                    print "Didn't get what receiver expected. Sending the last received acknowledgement number ", lastACKNo, '\n', '\n'
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
        global someflag,breakflag
        while True:
            # print 'receiving.......'
            data=s.recv(1024)
            if data == "close":
                breakflag=1
                break
            # if someflag==0:
            print "data= ",data
            global ACKNo,seqNoOfReceivedPacket,noOfPacketsReceived
            # print "next data"
            # print "Data received on the end of folder2.py",data
            if data:
                originalData=data
                # data=data.split('~')
                seqNoOfReceivedPacket=int(data)
                ACKNo=seqNoOfReceivedPacket + 1
                noOfPacketsReceived+=1
                if someflag==0:
                    print "Packet expecting with sequence number ",lastACKNo
                    print "Received with sequence number ",seqNoOfReceivedPacket
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
