#抵抗値をArduinoからもらって、その差が4いじょうだったら指定の位置をクリックするプログラム


from serial import Serial
import os

ser = Serial("/dev/cu.usbmodem1411", 9600)

tmp="0"
before_num=0
while 1:
    c=ser.read()
    if c=="a":
        before_num=int(tmp)
        tmp=""
    elif c=="b":
        print int(tmp)
        if before_num-int(tmp)>4:
            # print "push"
            os.system("cliclick c:612,606")
    else:
        tmp+=c
