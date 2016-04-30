# encoding: UTF-8
#

import httplib, mimetypes
import urllib
import urllib2
import os
import sys
import optparse
import hashlib
import time
import json

# The key for examples.
API_KEY = "填写自己的apikey"

class VirusBook(object):

    def __init__(self, api_key):

        super(VirusBook, self).__init__()

        self.api_key = api_key

    def __repr__(self):
        return "<VirusBook proxy>"

    def get(self, hash):
        print "Getting the report ...\r\n"
        #time.sleep(10)

        url = "https://www.virusbook.cn/api/v1/file/report"
        parameters = {"resource": hash,
                       "apikey": self.api_key}
        data = urllib.urlencode(parameters)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        ret_json = response.read()

        print "Report(in JSON):\r\n"
        #print(type(ret_json))
        strlength=len(ret_json)
        mylist = json.loads(ret_json)
        f=open('scans.csv', 'a')
        scan_list=['vbwebshell','Antiy','K7','IKARUS','Baidu','AVG','Avast','ClamAV','Kaspersky','Tencent','GDATA','Dr.Web','Sophos','kaiwei','Avira','Huorong','Kingsoft','Microsoft','ESET','Rising','Qihu360','Panda']
 
        for i in scan_list:
            #print(str(mylist[0]["scans"][i]["detected"]))
            f.write(str(mylist[0]["scans"][i]["detected"]))
            if i != "Panda":
                f.write(',')
            else :
                f.write('\n')
        f.close()

        return 1;

def main():
    parser = optparse.OptionParser(usage = """
    %prog <hash>
Samples:
    %prog b76280c2b71b369c8e013651d66d599c615cf83096388c1ad76be6c9725a26db
    """)

    (options, arguments) = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_usage()
        return -1

    hash = arguments.pop(0)
	
    try:
        v = VirusBook(API_KEY)
        v.get(hash)

    except Exception, e:
        print e
        print "VirusBook returned a non correct response. See the parameter -l"

if __name__ == "__main__":
    main()