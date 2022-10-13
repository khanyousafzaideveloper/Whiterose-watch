import time
from playsound import playsound

while True:
    local_time = time.gmtime()
    curr_sec = str(local_time.tm_sec)
    print(curr_sec)
    if(curr_sec=='0'):
        playsound('wrist_watch_beep.mp3')
        time.sleep(54)
     
