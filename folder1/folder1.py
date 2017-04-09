import socket,os,datetime
import time
from threading import Thread
import threading
global lastACKNo, seqNo, windowSize, t_out
class Senderthread(Thread): #sender is my client
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        windowSize=5
        # f = open(filename,'rw+')
        def sendPacket(seq_num):
            offset = seq_num
            f.seek(offset,0)
            len_seq_no = len(str(seq_num))
            s = f.read(1024 - len_seq_no -1)
            pac = s + "~" + str(packet_number)
            s.send(pac)

        def sendWindow(win_off_pack):
            temp = seq_num
            for x in range(5):
                sendPacket(temp)
                temp2 = len(str(temp))
                temp = temp + (1024-temp2)




        host = ""
        port = 30000
        s = socket.socket() # for TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((host, port))
        windowSize=raw_input("Enter window size: ")
        t_out=raw_input("Enter timeout interval: ")
        numberOfPackets=raw_input("Enter number of pacekts to be sent: ")

        # iteratorOnPacketNumber=0
        sendWindow(0) # Sending initial window
        tempseqnum = 0
        while True:
            if seqNo > tempseqnum:
                sendPacket(seqNo)
                iteratorOnPacketNumber+=1


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
            data=conn.recv(1024)
            originalData=data
            data=data.split()
            ack_recv = 1
            seqNo = int(data)
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
