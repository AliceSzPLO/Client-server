import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 8081
##BUFFER_SIZE = 1024

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP,TCP_PORT)) #เชื่อมต่อ
    s.listen(1)
    print("Host Server are ready!")
    conn, addr = s.accept() #รอรับข้อมูลที่ส่งมาจาก client.py
    print('Connection address:', addr) #แสดงลายละเอียดของ client ที่เชื่อมต่อมา


    data = conn.recv(1024)
    if not data: break
    print("received data from ",addr," : ", data) #แสดงข้อมูลที่ส่งมา
    conn.send(data) # echo
    conn.close() #จบการเชื่อมต่อ