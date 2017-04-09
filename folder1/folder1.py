import socket,os,datetime
import time
from threading import Thread
import threading
seqNo=0
windowSize=5
t_out =5
ack_dict = {}
# ack_recv
senttill = 0
class Senderthread(Thread): #sender is my client
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        f = open('testfile','rb')
        # global senttill = 0
        # ack_dict = {}
        # windowSize=5
        # f = open(filename,'rw+')
        ack_recv = 0
        # sent = []
        # unacked = []
        def sendPacket(seq_num):
            global senttill
            global ack_dict
            offset = seq_num
            f.seek(offset,0)
            len_seq_no = len(str(seq_num))
            s = f.read(1024 - len_seq_no -1)
            # print "s=",s
            if not s:
                # print "here"
                # f.close()
                return
            else:
                ack_dict[str(1024 - len_seq_no -1)] = 0
                if (offset + 1024 - len_seq_no -1) > senttill:
                    senttill = (offset + 1024 - len_seq_no -1)
                pac = s + "~" + str(seq_num)
                print "pac=",pac
                conn.send(pac)

        def sendWindow(seq_num):
            temp = seq_num
            for x in range(5):
                sendPacket(temp)
                temp2 = len(str(temp))
                temp = temp + (1024-temp2)

        host = ""
        port = 30000
        s = socket.socket() # for TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(15)
        windowSize=raw_input("Enter window size: ")
        t_out=raw_input("Enter timeout interval: ")
        numberOfPackets=raw_input("Enter number of pacekts to be sent: ")

        # iteratorOnPacketNumber=0
        conn, addr = s.accept()
        sendWindow(0) # Sending initial window
        tempseqnum = 0
        while True:
            global senttill
            global ack_dict
            if ack_recv == 1:
                sendPacket(senttill + 1)
                iteratorOnPacketNumber+=1
                ack_recv = 0


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

        s.connect((host, port))
        # s.listen(5)
        # conn, addr = s.accept()
        while True:
            data=s.recv(1024)
            if data:

                # print "data =", str(data)
                originalData=data
                # data=data.split()
                ack_recv = 1
                seqNo = int(data)
                ack_dict[str(seqNo-1)] =1
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
