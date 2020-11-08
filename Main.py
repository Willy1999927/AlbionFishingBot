import os
import psutil
import time             #time.sleep
import random           #random.uniform, random.randint
import numpy as np
import win32gui
import win32con
import winsound         #winsound.Beep
import keyboard         #keyboard.is_pressed
import pyautogui
import pyaudio
from PIL import ImageGrab
import cv2

def cast_rod():
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.12, 1.5))
    pyautogui.mouseUp()
def hold():
    pyautogui.mouseDown()
def release():
    pyautogui.mouseUp()
def use_fishing_bait():
    pyautogui.typewrite('1')

def get_position():  # Grab image, then find the Buoy
    capture = ImageGrab.grab(bbox=(839, 555, 1080, 556))  # Left, Upper, Right, Lower
    threshold = 150
    fn = lambda x: 255 if x > threshold else 0
    nums = np.array(capture.convert('L').point(fn, mode='1')).astype(int)

    for (x, y), value in np.ndenumerate(nums):
        if value == 1:
            return y + 7  
    return -1

hwnd = win32gui.GetForegroundWindow()
title = win32gui.GetWindowText(hwnd)
print(title)
if 'cmd.exe' in title or 'Main.exe' in title or 'Shell' in title:
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,0,640,700,400, 0) 

# Initialize Bot
maxValue = 2**14
bars = 35
p=pyaudio.PyAudio()

# Find the name of the speaker. Stereo problably
target = '立體聲混音'
# Find the name  
for i in range(p.get_device_count()):
    devInfo = p.get_device_info_by_index(i)   
    if devInfo['name'].find(target)>=0 and devInfo['hostApi'] == 0 :      
        print(devInfo)
        dev_idx = i
        break
p.terminate()
imgB = cv2.imread('bar_blue.png')
img_B, temp1, temp2 = cv2.split(imgB)
#wB, hB = img_B.shape[::-1]
imgR = cv2.imread('bar_red.png')
temp1, temp2, img_R = cv2.split(imgR)
#wR, hR = img_R.shape[::-1]
thresholdB = 0.88
thresholdR = 0.99

while True:
    print("Bot Starting Up, Good Luck")
    p=pyaudio.PyAudio()
    fishpoint = 0
    fishX = []
    fishY = []
    while True:
        if keyboard.is_pressed('F11'):
            fishpoint = fishpoint+1
            x, y = pyautogui.position()
            fishX.append(x)
            fishY.append(y)
            print("add point [%d], [%d]"%(x,y))
            winsound.Beep(523, 200)
            time.sleep(0.5)
        
        if keyboard.is_pressed('F10'):
            if fishpoint<1:
                fishpoint = fishpoint+1
                x, y = pyautogui.position()
                fishX.append(x)
                fishY.append(y)
            winsound.Beep(587, 200)
            break
        
    while True:
        print('CPU: ',psutil.cpu_percent())
        print('CPU Details: ',psutil.cpu_freq(percpu=True))
        print('Memory: ',psutil.virtual_memory().percent)
        print('New round, cast rod                             ', end = ' \r')
        playerexist = False
        while True:
            print('Player detecting                            ', end = ' \r')
            capture = np.array(ImageGrab.grab(bbox=(50, 70, 1870, 1030)))  # Left, Upper, Right, Lower
            capture_R, capture_G, capture_B = cv2.split(capture)
            res = cv2.matchTemplate(capture_B,img_B,cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= thresholdB)
            #print (np.count_nonzero(res >= thresholdB))
            if np.count_nonzero(res >= thresholdB)>0:
                for pt in zip(*loc[::-1]):
                    print(pt)
                time.sleep(random.uniform(10, 20))
                playerexist = True
                continue
            res = cv2.matchTemplate(capture_R,img_R,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= thresholdR)
            #print (np.count_nonzero(res >= thresholdR))
            if np.count_nonzero(res >= thresholdR)>0:
                for pt in zip(*loc[::-1]):
                    print(pt)
                time.sleep(random.uniform(10, 20))
                playerexist = True
                continue
            print('no player detected')
            if playerexist:
                time.sleep(random.uniform(20, 60))
            break
        fishpointselect = random.randint(0,fishpoint-1)
        pyautogui.moveTo(fishX[fishpointselect]+random.randint(-5,5), fishY[fishpointselect]+random.randint(-5,5))
        cast_rod()
        over = False
        time.sleep(1.8)
        print('start to detect sound')
        stream=p.open(input_device_index=dev_idx,format=pyaudio.paInt16,channels=2,rate=44100, input=True, frames_per_buffer=1024)
        previoussum = 0
        count = 0
        chunkcount = 0
        while True:
            print('Sound detecting                          ', end = ' \r')
            data = np.frombuffer(stream.read(4096),dtype=np.int16)
            volume = int(np.abs(np.max(data)-np.min(data))*bars/maxValue)
            if volume>0:
                chunkcount = chunkcount+1
            elif previoussum==0:
                chunkcount = 0
            starString = "#"*volume+"-"*int(bars-volume)
            print("Volume=[%s]"%(starString))
            if keyboard.is_pressed('F12'):
                break
            count = count + 1
            if count > 1000:
                break
            if volume>=6 or volume+previoussum>=9:
                if volume>=9 and chunkcount>3:
                    continue
                stream.stop_stream()
                stream.close()
                #print("L=[%s]\tR=[%s], Start to catch fish"%(np.max(dataL), np.max(dataR)))
                pyautogui.moveTo(fishX[fishpointselect]+random.randint(-5,5), fishY[fishpointselect]+random.randint(-5,5))
                hold()  # Move Right
                time.sleep(random.uniform(0.75, 0.8))
                release()
                #winsound.Beep(frequency, duration)
                while True:  # While Fishing Bar Is On Screen
                    position = get_position()
                    if position == -1:  # Fishing is Over
                        print('position is ', position, ', over')
                        release()
                        over = True
                        break

                    if position < 137:
                        hold()  
                        time.sleep(random.uniform(0.1, 0.15))
                    elif position > 145:
                        release()  
                        time.sleep(random.uniform(0.005, 0.02))
                        hold()
                        time.sleep(random.uniform(0.035, 0.6))
                        if random.randint(0,1) == 1:
                            release()
                            time.sleep(random.uniform(0.005, 0.013))
                    elif position < 145:
                        hold()
                        time.sleep(random.uniform(0.03, 0.08))
                        release()
            previoussum = volume
            if over==True:
                for i in range(30):
                    time.sleep(random.uniform(0.1, 0.2))
                    if keyboard.is_pressed('F12'):
                        break
                if keyboard.is_pressed('F12'):
                    break
                os.system('cls')
                print('start new round')
                break
            if keyboard.is_pressed('F12'):
                break
        if keyboard.is_pressed('F12'):
            break

    p.terminate()
    winsound.Beep(784, 200)
    os.system('cls')
