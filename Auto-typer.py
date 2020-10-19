import pyperclip
import time
import keyboard
import sys
import os
import keyboard
pse = True

cnt = 1
print("Get ready!")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

with open("script.txt", "r", encoding="utf-8") as fp:
   line = fp.readline()
   while line:
       print(" Remember! Ctrl + alt + p to pause")
       if keyboard.is_pressed('ctrl + alt + p'):
           pse = True
           while pse == True:
               if keyboard.is_pressed('ctrl + alt + s'):
                   pse = False
               else:
                   print("Paused! Ctrl + alt + s to resume")
                   os.system('cls')
       else:
           print("Line {}: {}".format(cnt, line.strip()))
           print(" ")
           line = fp.readline()
           pyperclip.copy(line)
           print("Line has been copyed!")
           keyboard.press_and_release('Ctrl+v')
           print("Line has been pasted!")
           time.sleep(0.25)
           keyboard.press_and_release('enter')
           print("Enter key has been pressed!")
           print("Waiting timeout...")
           time.sleep(1)
           print("3")
           time.sleep(1)
           print("2")
           time.sleep(1)
           print("1")
           time.sleep(0.8)
           print("NEXT LINE!")
           print(cnt)
           cnt += 1
           os.system('cls')
