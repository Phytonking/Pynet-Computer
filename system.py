from os import system

#clearapplication
def screenclear():
  _ = system('clear')



def Restart_Shutdown_Logoff():
  RSL = input()
  if RSL == "open.powermenu":
    print("1.Shut down")
    print("2.Log off")
    print("3.Restart")

