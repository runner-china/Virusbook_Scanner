import postfile
import time
import json 

host = "www.virusbook.cn"
selector = "https://www.virusbook.cn/api/v1/file/scan" 
fields = [("apikey", "填写自己的apikey")] 

with open('samples-malware.txt', 'r') as f:
    list1=[i.strip() for i in f.readlines()]

with open('samples-normal.txt','r') as f:
    list2=[i.strip() for i in f.readlines()]

myfile=open('out.txt', 'w')

for i in list1:
    filename='samples-malware\\'+i    
    file_content = open(filename, "rb").read()
    files = [("file", filename, file_content)]
    json_string = postfile.post_multipart(host, selector, fields, files)
    mydict = json.loads(json_string)
    myfile.write(mydict["permalink"])
    myfile.write('    '+i)
    myfile.write('\n')
    time.sleep(13)
    
for i in list2:
    filename='samples-normal\\'+i     
    file_content = open(filename, "rb").read()
    files = [("file", filename, file_content)]
    json_string = postfile.post_multipart(host, selector, fields, files)    
    mydict = json.loads(json_string)
    myfile.write(mydict["permalink"])
    myfile.write('    '+i)
    myfile.write('\n')
    time.sleep(13)
    
myfile.close()
print("over!")
