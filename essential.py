import time
import snownlp
import random
import streamlink
import cv2
import wordcloud
import matplotlib.pyplot as plt
import requests
bilibili_dict={"Referer":"https://live.bilibili.com/",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
def GetTs():
    tsurl="https://api.vtbs.moe/meta/timestamp"
    tsr=requests.get(tsurl)
    return (tsr.ok,tsr.content.decode() if tsr.ok else "Failed")
def GetLastupd():
    tsurl="https://api.vtbs.moe/v1/guard/time"
    tsr=requests.get(tsurl)
    return (tsr.ok,tsr.content.decode() if tsr.ok else "Failed")
def ConvertTime_Ts(Ts):
    return (True,{"raw_time":time.localtime(Ts),"fmt_time":time.strftime("%Y/%m/%d#%H:%M:%S",time.localtime(Ts))})