import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 8081
BUFFER_SIZE = 1024
##MESSAGE = "Hello, World!"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP,TCP_PORT)) #เชื่อมต่อ
    print("Conecting Success!")
    MESSAGE = input("Send to server : ")
    if MESSAGE == "DC" :
        print("\nDisconnecting....")
        s.close()
    s.send(MESSAGE.encode('utf-8')) #ส่งข้อมูลโดยก่อนส่งได้เข้ารหัสตัวอักษรเป็น utf-8
    data = s.recv(BUFFER_SIZE) #ดึงผลลัพธ์การส่งข้อมูล
    s.close() #จบการเชื่อมต่อ

    print("received data:", data,"\n") #แสดงผลลัพธ์การส่งข้อมูล