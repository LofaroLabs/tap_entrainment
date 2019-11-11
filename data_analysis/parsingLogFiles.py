import numpy as np
import matplotlib.pyplot as plt



f= open("/home/alex/Desktop/Data_for_analyzing/2019-10-23T143522.478872.log","r")# change this to the path to the log file in your computer
count,diffCount = 0,0
timer = f.readline()
diffVal = np.array([])
Add = True
EyeState = np.array([])
while True:
  temp = f.readline()
  if(temp == ""):
    break # break condition
  first = temp.split(" ")[0]
  if(first == "B"):
    [first,second] = temp.split(" ")
    if(int(second) == 3):
        # swtich here
        Add = not(Add)
    EyeState = np.append(EyeState,diffCount)
  elif(first == "D"):
    [first,second,third,fourth] = temp.split(" ")
      # this is what we care about
      # first is "D", second is time diff, third is "diff" and fourth is a space(nice job alex)
    if(Add):
      diffVal = np.append(diffVal,float(second))
      diffCount +=1

  count +=1
plt.plot(diffVal)
for a in EyeState:
  plt.axvline(x=a,color='r')
plt.show()
