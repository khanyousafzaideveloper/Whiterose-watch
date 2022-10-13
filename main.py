import time
from playsound import playsound
import threading

def beep():
    file_name = 'wrist_watch_beep.mp3'
    return file_name

def curr_time():
    t = time.gmtime()
    print(f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}")

t1 = threading.Thread(target=beep)
t2 = threading.Thread(target=curr_time)

t2.start()
t1.start()

t2.join()
t1.join()

while True:
    t = time.gmtime()
    sec = str(t.tm_sec)
    if(sec=='0'):
        playsound(beep())
        curr_time()
     

