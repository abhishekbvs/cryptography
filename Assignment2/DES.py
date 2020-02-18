from Crypto.Cipher import DES
import string
count = 0
ct = "4B518774A408E3E5"
a = string.letters + string.digits
for i in range(255):
    for j in range(255):
        for k in range(255):
            for l in range(255):
                for m in range(255):
                    for n in range(255):
                        for o in range(255):
                            for p in range(255):
                                key = chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+chr(n)+chr(o)+chr(p)
                                des = DES.new(key,DES.MODE_ECB)
                                pt = des.decrypt(ct.decode("hex"))
                                if(all(c in a for c in pt)):
                                    print count
                                    print(pt)
                                    f  = open('plaintext',"a")
                                    f.write("[ " + key.encode("hex") + " : ")
                                    f.write(pt + " ]\n")
                                    f.close()
                                count += 1