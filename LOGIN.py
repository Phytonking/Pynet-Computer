#compile
import system
import applicationmenu
Avi = {
 "name":"Avi Agola",
 "Password":"Avimongo",
 "email":"avi.agola@gmail.com"
}




def password():
  x = Avi["Password"]
  passw = input()
  if passw == x:
    print("Login successful")
    system.screenclear()
    applicationmenu.applicationmenu()
  else:
    print("ERROR 409: INCORRECT PASSWORD")
    password()





def security():
  y = Avi["email"]
  print("Enter your email connected with pynet")
  Email = input()
  if Email == y:
    print(y)
    print("Hello Avi, Type in your Pynet password")
    passw = input()
    password()
     

    
    

  
  