import sys
import socket,select

port = 11111
socket_list = []
users = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1',port))
server_socket.listen(2)
socket_list.append(server_socket)

while True:
    ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)
    for sock in ready_to_read:
        if sock == server_socket:
            connect, addr = server_socket.accept()
            socket_list.append(connect)
            if users:
                users['bob'] = connect
                connect.send("alice".encode())
                print ("User Bob added and connection is established")
                users['alice'].send("Hello".encode())
            else:
                users['alice'] = connect
                connect.send("bob".encode())
                print ("User Alice added and connection is established")
        else:         
            data = sock.recv(2048).decode()
            if data.startswith("@"):
                print("Message Transfered to "+data[1:data.index(':')])
                print("AES Encrypted Message : " +data[data.index(':')+1:data.index('#')])
                print("SHA512 Hash : "+data[data.index('#')+1:data.index('$')])
                print("HMAC SHA256 Digest : "+data[data.index('$')+1:])

                users[data[1:data.index(':')].lower()].send(data[data.index(':')+1:].encode())

server_socket.close()