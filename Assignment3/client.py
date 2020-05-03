import socket
import hashlib 
import hmac
from cryptography.fernet import Fernet

port = 11111
client_socket = socket.socket()
client_socket.connect(('127.0.0.1',port))
opp = '@' + client_socket.recv(1024).decode()+':'
print("Your are connected and user detail saved")

# Some Random Symmetric Key for Both Alice and Bob
key = b'w4ZNAAaJF_DzVRuP_H8_T1RN-QqcOy6x_6AjNLAsaLY='

# Fernet class which is an implementation of AES
f = Fernet(key)

while True:
    try:
        recv_msg = client_socket.recv(1024).decode()
        # Extract encrypted message
        enc_msg = recv_msg[0:recv_msg.index('#')]
        # Decrypt the message
        decrypted = f.decrypt(enc_msg.encode())
        # Extracting SHA512 Hash Message
        print("Recieved message :"+decrypted.decode())
        h_msg = recv_msg[recv_msg.index('#')+1:recv_msg.index('$')]
        # Extract HMAC SHA256 Digest
        hmac_digest = recv_msg[recv_msg.index('$')+1:]
        # Verify SHA512 Hash
        if h_msg == hashlib.sha512(decrypted).hexdigest() :
            print("SHA512 Hash matched",end=", ")
        if hmac_digest == hmac.new(key,decrypted, hashlib.sha256).hexdigest():
            print("HMAC SHA256 Digest matched")
    except:
        print("Initiate the Chat")
        pass
    send_msg = input("Send message: ")
    if send_msg == 'exit':
        break
    else:
        # Encrypting the message
        encrypted_msg =f.encrypt(send_msg.encode()).decode()
        # SHA 512 Hash Message
        hash_msg='#'+hashlib.sha512(send_msg.encode()).hexdigest()
        # creating new hmac object using sha1 hash algorithm 
        hmac_digest ='$'+hmac.new(key, send_msg.encode(), hashlib.sha256).hexdigest()
        # Send to other client via server
        client_socket.send((opp+encrypted_msg+hash_msg+hmac_digest).encode())

client_socket.close()