import os
from datetime import datetime

# keep running
while True:
    # get the time at this precise moment
    now = datetime.now()
    # get the current seconds
    currentSeconds = now.strftime("%S")
    # if the current second is at an interval of 30 sec run program
    if (int(currentSeconds) % 30) == 0:
        # simply runs program in quotations in a cmd format
        os.system('new.py')
