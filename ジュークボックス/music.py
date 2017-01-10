#!/usr/local/bin python
#-*- coding: utf-8 -*-
from serial import Serial
import glob
from random import shuffle
import os

#Serialの取得先をserに収納
ser = Serial("/dev/cu.usbmodem1411", 9600)

#Serialを連続でread
tmp="0"
before_num=0
while 1:
    c=ser.read()#圧力の値を読み取る。
    if c=="a":
        before_num=int(tmp)
        tmp=""
    elif c=="b":
        print int(tmp)
        #圧力の値の差が大きい時、ターミナルに書き込み
        if before_num-int(tmp)>20:
            x=glob.glob("box/*.flac") #testの中のflac音源をリスト化
            shuffle(x) #リストをシャッフル
            print x[1]#再生する音源を表示
            music="open "+x[1]#「open hoge」という文字列を作成
            os.system(music)
    else:
        tmp+=c




#pygame.mixer.init()
#pygame.mixer.music.load(x[1])
#pygame.mixer.music.play(1)

#print "ctrl+c stop"
#while 1:
#    x = 1

#pygame.mixer.music.stop() # 再生の終了
