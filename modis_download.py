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
import platform

class MODIS_download():
      
    def __init__(self,idmPath,modis_csv,url_head,outputPath):
        self.idmPath = idmPath
        self.modis_csv = modis_csv
        self.url_head = url_head
        self.outputPath = outputPath
        self.quene_url = pd.read_csv(modis_csv)
        self.quene_temp = self.quene_url
        
    def idman(self,quene = ""):
        now = os.getcwd()
        os.chdir(self.idmPath)
        index = 0
        
        for P in self.quene_url["fileUrls"]:
            index = index + 1
            print(index)
            print(P)
            call(['IDMan','/d',self.url_head+P,'/p',self.outputPath,'/f',P.split('/')[-1],'/n','/a'])
        os.chdir(now)
		
    def cgc(self):
        print("hello world")
		
    def wget(self,filename = "wget.sh"):
        f = open(filename,"w")
        f.writelines("#!/bin/bash\n")
        index = 0
        
        for P in self.quene_url["fileUrls"]:
            index = index + 1
            f.writelines("echo {:d}\n".format(index))
            #wget -nc  --user=$user --password=$pass -P $outputPath ftp://arthurhou.pps.eosdis.nasa.gov/pub/gpmdata/$year/$(printf '%02d' $month)/$(printf '%02d' $day)/radar/$gpmtype".*.HDF5"    
            f.writelines("wget -nc -P {:s} {:s}\n".format(self.outputPath,self.url_head+P))
        f.close()
    def calcTotal(self):
          print(self.quene_url["size"].sum()/1024/1024/1024,end =" G\n")
          
    def check(self,mode = "wget",addfilename = "wget_add.sh"):
        print("outputPath is {:s}".format(self.outputPath))
        print("modis_csv is {:s}".format(self.modis_csv))
        if platform.system() == 'Windows':
            download_file = glob.glob(self.outputPath+"\*.hdf")
            a = [i.split("\\")[-1] for i in download_file]
        elif platform.system()  == 'Linux':
            download_file = glob.glob(self.outputPath+"/*.hdf")
            a = [i.split("/")[-1] for i in download_file]
        #print(a)
        print("all download file is :{:d}".format(len(download_file)))
        b = np.ones(len(a))
        all = pd.Series(data = b, index = a)
        output={}
        index = 0
        keys = self.quene_url.keys()
        for k in keys:
              output[k] =[]
        
        for P in self.quene_url["fileUrls"]:
            if P.split('/')[-1] in all.index:
                continue
            else:
                index += 1
                index1 = self.quene_url[self.quene_url["fileUrls"] == P].index.tolist()[0]
                for k in  keys:
                    output[k].append(self.quene_url.iloc[index1][k])        
        output = pd.DataFrame(data = output)     
  				
        print("loss :{:d}".format(index))
        if mode == "idman" :
            addfilename = "idman_add.csv"
            self.quene_temp = self.quene_url
            self.quene_url = output
            self.idman()
            self.quene_url = self.quene_temp
        elif mode == "wget":
            print(addfilename)
            self.quene_temp = self.quene_url
            self.quene_url = output
            self.wget(addfilename)
            self.quene_url = self.quene_temp
        return output
            
            
            
            