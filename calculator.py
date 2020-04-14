import system
system.screenclear()
def calculator():
  print("calculator")
  print("please enter the operation you wish to use")
  print("type 'mmm' to go into Mean Median and mode ")
  print("type exit to exit the application")

  print("+ is Addition")
  print("- is subtraction")
  print("* is multiplication")
  print("/ is divison")
  operate = input()
  if operate =="mmm":
    import numpy
    from scipy import stats
    speed =[12345,45647,324567,345367]

    x = numpy.mean(speed)
    y = numpy.median(speed)
    z = stats.mode(speed)

    print("the mode is "+z)
    print("the median is "+y)
    print("the mean is "+x)
  if operate == "+":
    print("please enter the first number")
    num1 = input(int)
    print("please enter the second number")
    num2 = input(int)
    system.screenclear()
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)
  if operate == "-":
    print("please enter the first number")
    num1 = input(int)
    print("please enter the second number")
    num2 = input(int)
    system.screenclear()
  print('{} - {} = '.format(num1, num2))
  print(num1 - num2)  
  if operate == "*":
    print("please enter the first number")
    num1 = input(int)
    print("please enter the second number")
    num2 = input(int)
    system.screenclear()
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)
  if operate == "/":
    print("please enter the first number")
    num1 = input(int)
    print("please enter the second number")
    num2 = input(int)
    system.screenclear()
    print('{} / {} = '.format(num1, num2))
    print(num1 + num2)
  if operate == "exit":
    system.screenclear()
    import applicationmenu
    applicationmenu.applicationmenu()
