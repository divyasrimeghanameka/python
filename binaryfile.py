f=open("binaryfile.bin","wb")
f.write(b'\x01\x02\x03\x04')
f=open("binaryfile.bin","rb")
print(f.read())
