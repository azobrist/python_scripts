from serialcom import *
from prg_bar import progress
import time

ser=sercom()

total = 100
i = 0
while i < total:
    progress(i, total, status='Doing very long job')
    time.sleep(0.5)  # emulating long-playing job
    i += 1

closecom(ser)
