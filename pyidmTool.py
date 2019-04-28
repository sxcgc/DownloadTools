"""
作者：陈光灿
联系方式：cgc@mail.ustc.edu.cn
github.ustccgc.io
"""
import pandas as pd
from subprocess import call
import os
import glob
import numpy as np
from modis_download import MODIS_download

'''
您可以从命令行中使用下列参数启动 IDM

idman /s
或 idman /d URL [/p 本地_路径] [/f 本地_文件_名] [/q] [/h] [/n] [/a]

参数：
/d URL - 下载一个文件，等等。
IDMan.exe /d "http://www.internetdownloadmanager.com/path/File Name.zip"
/s - 开始任务调度里的队列
/p 本地_路径 - 定义要保存的文件放在哪个本地路径
/f 本地local_文件_名 - 定义要保存的文件到本地的文件名
/q - IDM 将在成功下载之后退出。这个参数只为第一个副本工作
/h - IDM 将在成功下载之后挂起您的连接
/n - 当不要 IDM 询问任何问题时启用安静模式
/a - 添加一个指定的文件 用 /d 到下载队列，但是不要开始下载

参数 /a, /h, /n, /q, /f 本地_文件_名， /p 本地_路径 工作只在您指定文件下载 /d URL
--------------------- 
作者：muyangren907 
来源：CSDN 
原文：https://blog.csdn.net/MuoYangoRen/article/details/79954776 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

idmPath = r"D:\Program Files (x86)\Internet Download Manager"# idm的安装路径
modis_csv = r"I:\LAADS_query.2019-04-27T02_52.csv"#modis的csv下载
url_head = r"https://ladsweb.modaps.eosdis.nasa.gov"#modis路径
outputPath = r"I:\MYD"

a = MODIS_download(idmPath,modis_csv,url_head,outputPath)
bbb = a.check('idman')

#quene_url = pd.read_csv(modis_csv)
#batfileoutput = open(outputPath+"download.bat","w")
#batfileoutput.writelines("D:\n")
#batfileoutput.writelines("cd {:s}\n".format(idmPath))
	

	
'''	
for P in quene_url["fileUrls"]:
    index = index + 1
    print(index)
    print(P)
    #batfileoutput.writelines("IDMan /d {:s} /p {:s} /f {:s} /n \n".format(url_head+P,outputPath,P.split('/')[-1]))
#batfileoutput.close()
    call(['IDMan','/d',url_head+P,'/p',outputPath,'/f',P.split('/')[-1],'/n','/a'])
	
print(quene_url["size"].sum()/1024/1024/1024,end =" G\n")

'''