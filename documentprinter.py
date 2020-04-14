import system
system.screenclear()

def docpower():
  print("1.New document")
  print("2.Read an old document")
  print("3.Edit a document")
  print("delete files")
  opt = input()
  if opt == "1":
    print("what is the new name of the document")
    name = input()
    C = open(name+".txt","x")
    print(C)
    if opt == "2":
      print("which document") 
      nom = input()
      R = open(nom+".txt","r") 
      print(R)
    if opt == "3":
      print("what document")  
      n = input()
      E = open(n+".txt","w")
      print(E)

      if opt == "4":
        nam = input()
        import os
        os.remove(nam+".txt")