import time

# function that opens hot and cold water taps
def tapsOn():
  print("Hot and cold taps are on.")

# function that closes hot and cold water taps
def tapsOff():
  print("Hot and cold taps are off.")  

# function that asks the user if the water temperature is okay and also validates user input
def tempCheck():
  temp = input("Is it too hot or cold? (yes/no)\n")
  if temp == "yes":
    print("Keep hot and cold taps on.")
    tempCheck()
  elif temp == "no":
    return
  else:
    print("Please enter 'yes' or 'no'.")
    tempCheck()

# function that asks the user if the bath water level is full and also validates user input
def levelCheck():
  level = input("Is the bath full? (yes/no)\n")
  if level == "no":
    print("Keep hot and cold taps on.")
    waitCheck()
    levelCheck()
  elif level == "yes":
    return
  else:
    print("Please enter 'yes' or 'no'.")
    levelCheck()

# function that waits for 120 seconds
def waitCheck():
  print("Waiting for 2 minutes.")
  time.sleep(120)
  print("Waiting time is reached.")
  return

# main program
tapsOn()
tempCheck()
waitCheck()
levelCheck()
tapsOff()
