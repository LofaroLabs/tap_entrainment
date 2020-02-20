import time
import numpy
f = open("2019-11-21T10:44:40.732952.log","r")
lastDat = 0
diffArr = numpy.array([])
while(True):
  line = f.readline()
  if(line == ""):
    break
  if(line.split(" ")[0] == "H"):
    typeTap = line.split(" ")[2]
    if(typeTap == "left\r\n"):
      dat = line.split(" ")[1]
      diff = float(dat)-float(lastDat)
      if(diff > 0.21):
        diffArr = numpy.append(diffArr,diff)
        lastDat = dat
print(diffArr)
print(numpy.average(diffArr))


