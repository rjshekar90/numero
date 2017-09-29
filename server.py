import socket

sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

print("Host::",host)

port=4555

sc.bind((host,port))

sc.listen(3)


while True:

    clientsoc,addr=sc.accept()

    print("Client Address:",addr)

    clientsoc.send("This is server")
    msg=clientsoc.recv(1000)
    print("Client Message:",msg)
    clientsoc.close()
