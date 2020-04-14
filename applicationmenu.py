#application opener
import clock

def applicationmenu():
  import system
  system.screenclear()
  print("Hello ")
  s = clock.timez()
  print("                                   "+s)
  print("what application will you open today ")
  print("type the number of the application you want to go into ")
  print("1.Game menu")
  print("2.calcualtor")
  print("3.Document printer")
  applict = input()
  if applict == "1":
    system.screenclear()
    import gamemenu
    gamemenu.game()
      
    
  if applict == "2":
    system.screenclear()
    import calculator
    calculator.calculator()  

  if applict == "3":
    system.screenclear()
    import documentprinter
    documentprinter.docpower()

    
       
        
  

  



