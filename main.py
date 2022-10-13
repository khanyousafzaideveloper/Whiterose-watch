import time
from playsound import playsound

while True:
    t = time.gmtime()
    sec = str(t.tm_sec)
    if(sec=='0'):
        playsound('wrist_watch_beep.mp3')
        print(f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}")
        time.sleep(57)
     
