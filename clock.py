import time
import datetime




def timez():
  t = datetime.datetime.now()
  Year = t.strftime("%Y")
  month = t.strftime("%b")
  day = t.strftime("%a")
  hour = t.strftime("1")
  minute = t.strftime("%M")
  AMPM = t.strftime("%p")
  print("                                                                                         "+day+"/"+month+"/"+Year)
  print("                                                                                         "+hour+":"+minute+AMPM)
  import system
  system.screenclear()
  time.sleep(60)
  timez()

  
timez()