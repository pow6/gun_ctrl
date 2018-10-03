#coding:utf-8

import pyautogui
import re
import os
import subprocess
import sys
import time
import array
import win32api
import win32gui
import win32con
import serial

def serial_main():
    with serial.Serial('COM3',9600,timeout=1)as ser:
        while True:
            data =ser.readline(1)
            while data!=(b's'): #開始文字が来るまで待機
                data =ser.readline(1)                
            x = int(ser.readline(3))
            y = int(ser.readline(3))
            z = int(ser.readline(3))
            if(ser.readline(1)==(b'e')):
                print('X='+str(x)+'Y='+str(y)+'Z='+str(z))
                mouse_main(x,y,z)
            else:
                print("Error")

def mouse_main(x,y,z):
#    screen_x,screen_y = pyautogui.size()
#    pyautogui.moveTo
    pyautogui.moveTo(x,y)

if __name__=="__main__":
    serial_main()


#GUIを追加し，初期設定などをできるようにしよう。
#初期設定では，画面の取得や，加速度センサのデフォルトの値を計算するようにできるようにする。ボタンを押して設定とか。
#画面の取得は，GUIで直設定でもいいかも