import socket

sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

print("Host::",host)

port=4555

sc.connect((host,port))

message=sc.recv(1000)

sc.send("Thank you")

sc.close()

print("Message",message)

