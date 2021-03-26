import time 
import datetime
import os
from playsound import playsound


print('----------------------')
print("Enter the H :M: S")
print("----------------------")
alarm_h=int(input("enter hour:"))
alarm_m=int(input("enter min :"))
alarm_s=int(input('enter sec:'))
am_pm =str(input("Am / Pm"))


print("waiting to ring the alarm ",alarm_h,':',alarm_m,':',alarm_s,':',am_pm)


if am_pm=="pm":
    alarm_h+=12
    while (1==1):
        if (alarm_h==datetime.datetime.now().hour and alarm_m==datetime.datetime.now().minute and alarm_s==datetime.datetime.now().second ):
            print("wakeup")
            playsound("C:/Users/LOKESH/OneDrive/Desktop/munny/python projects/alarm clock gui/master_blaster.mp3")
            break