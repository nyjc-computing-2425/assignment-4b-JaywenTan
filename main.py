stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
# Type your code below
check = ["0","1","2","3","4","5","6","7","8","9","x","^",".","E","-"]
check2 = ["x","^",".","E","-"]
check3 = False
count = 0
num = len(stdform)
for a in stdform:
  if not a in check:
    break
  elif a in check2 and stdform.count(a) > 1:
    break
  else:
    count += 1
    if count == num:
      check3 = True
if check3 == True:
  a = stdform.find("x")
  b = stdform.find("^")
  c = stdform[b+1:]
  if "." in c:
    check3 = False
  else:
    text = stdform[:a] + "E" + stdform[b+1:]
if check3 == True:
  print("This number in E notation is {}.".format(text))
else:
  print("Error converting to scientific E notation.")
