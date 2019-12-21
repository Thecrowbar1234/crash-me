import os 
import time
import random

filelist = os.listdir()
def shoot():
  crap = random.choice(filelist)
  os.system("rm "+str(crap))
  shoot()
shoot()