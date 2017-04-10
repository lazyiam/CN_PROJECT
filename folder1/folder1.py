import socket,os,datetime
import time
from threading import Thread
import threading
from random import randint
seqNo=0
windowSize=5
t_out =5
ack_dict = {}
# ack_recv
senttill = 0
packetNum=1
arrTimeOut=[0 for i in range(1000000)]
arr=[0 for i in range(1000000)]
breakflag =0
numberOfPackets = 0
class Senderthread(Thread): #sender is my client
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        # f = open('testfile','rb')
        # global senttill = 0
        # ack_dict = {}
        # windowSize=5
        # f = open(filename,'rw+')
        # ack_recv = 0
        # sent = []
        # unacked = []
        global packetNum
        def sendPacket(pacNo):
            global senttill
            global ack_dict,numberOfPackets
            p=randint(1,10)
            if p !=3 and pacNo<=numberOfPackets:
                conn.send(str(pacNo))
            else:
                if pacNo<=numberOfPackets:
                    print "missed for ",pacNo
            senttill=pacNo

            # offset = seq_num
            # f.seek(offset,0)
            # len_seq_no = len(str(seq_num))
            # s = f.read(1024 - len_seq_no -1)
            # # print "s=",s
            # if not s:
            #     # print "here"
            #     # f.close()
            #     return
            # else:
            #     ack_dict[str(1024 - len_seq_no -1)] = 0
            #     if (offset + 1024 - len_seq_no -1) > senttill:
            #         senttill = (offset + 1024 - len_seq_no -1)
            #     pac = s + "~" + str(seq_num)
            #     print "pac=",pac
            #     conn.send(pac)
            #     return 1

        def sendWindow(l,r):

            for x in range(l,r):
                sendPacket(x)
                arrTimeOut[x]=time.time()
                time.sleep(0.1)
                # if packetSentOrNot==1:
                # temp2 = len(str(temp))
                # temp = temp + (1024-temp2)
                # else:


        host = ""
        port = 30000
        s = socket.socket() # for TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(15)
        windowSize=int(raw_input("Enter window size: "))
        t_out=int(raw_input("Enter timeout interval: "))
        atemp=int(raw_input("Enter number of pacekts to be sent: "))
        global numberOfPackets
        numberOfPackets = atemp

        # iteratorOnPacketNumber=0
        conn, addr = s.accept()
        tempseqnum = 0
        sendWindow(1,1+windowSize) # Sending initial window
        t0=time.time()
        ackIterator=1
        global breakflag
        counter = 0
        while True:
            counter+=1
            if arr[numberOfPackets] == 1:
                conn.send("close")
                breakflag=1
                break
            global senttill
            global ack_dict
            global seqNo
            if time.time()-arrTimeOut[ackIterator]<t_out :
                if arr[ackIterator]==1:
                    sendWindow(ackIterator+windowSize,ackIterator+windowSize+1)
                    ackIterator+=1
            else:
                sendWindow(ackIterator,ackIterator+windowSize)
            # global packetNum

            # if ack_dict[str(seqNo-1)] == 1: #ack_dict[index]=0 means that the acknowledgement is not received for that packet
            #     sendPacket(senttill + 1, 1, 2)   #ack_dict[index]=1 means that the acknowledgement is received for the packet one time only.
            #     iteratorOnPacketNumber+=1        #ack_dict[index]=2 is assigned to make sure multiple occurences of the same packet doesn't occur.
            #     # ack_recv = 0
            #     ack_dict[str(seqNo-1)]=2


        print('Successfully get the file')
        conn.close()
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
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = ""
        global ack_recv, seqNo, packetNum, arr
        s.connect((host, port))
        # s.listen(5)
        # conn, addr = s.accept()
        global breakflag
        while True:
            if breakflag==1:
                break
            data=s.recv(1024)
            if data:

                # print "data =", str(data)
                originalData=data
                ack_recv = 1
                seqNo = int(data)-1
                for i in range(1,seqNo+1):
                    if arr[i]==0:
                        arr[i]=1
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
