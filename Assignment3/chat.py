from cryptography.fernet import Fernet
import hashlib 
import hmac

if __name__ == '__main__' :
   
    print("Enter")

    message = b'my deep dark dxdcdcdcsecret'

    # (a) Symmetric key encryption for confidentiality
    # Fernet class which is an implementation of AES

    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print(encrypted)
    decrypted = f.decrypt(encrypted)
    print(decrypted)

    # (b) SHA-512 for integrity
    # SHA 512

    print(hashlib.sha512(message).hexdigest())

    #(c) HMAC for message authentication
    # creating new hmac object using sha1 hash algorithm 
    digest_maker = hmac.new(key, message, hashlib.sha1) 
    
    print ("Hexdigest: " + digest_maker.hexdigest()) 

    # call update to update msg 
    # digest_maker.update(b'another msg')    
    