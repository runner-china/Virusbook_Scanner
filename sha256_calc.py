#!/usr/bin/env python3
#encoding=utf-8
import hashlib

with open('samples-normal.txt','r') as f:
    mylist=[ i.strip() for i in f.readlines()]   
print(mylist)

for i in mylist:
    with open('samples-normal\\'+i,'rb') as f:
        mybytes=f.read()   
    sha256 = hashlib.sha256()
    sha256.update(mybytes)
    print(sha256.hexdigest())
