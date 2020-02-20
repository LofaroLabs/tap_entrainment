# -*- encoding: UTF-8 -*- 

''' PoseZero: Set all the motors of the body to zero. '''

import sys
from naoqi import ALProxy
import time
import math
#import forwardKinematics 
import qi

bpm = 90.0# 60 bpm by default

### max is 90 bpm or 1.5 Hz reliably.

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def main(robotIP):
    global bpm
    # Init proxies.
    #charGetter = _GetchUnix()
    #charGetter.__init__()
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
	session = qi.Session()
	session.connect("tcp://" + robotIP + ":" + str(9559))
        memory_service = session.service("ALMemory")
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    pRArm = "RArm"


    # [115.59515097  20.11797839  20.11797839 -76.84603986   0.        ]
    offset = -10
    #pTargetAngles0R = [ (75),12.21749182,-90, -63.51705609+offset, 90 ] 
    #pTargetAngles1R = [ (75),12.21749182,-90, -80.51705609+offset, 90 ] 
    pTargetAngles1R = [ 70,-12.2,90,88.5, -90,1 ]
    pTargetAngles0R = [ 70,-12.2,90,88.5-10, -90,1]
    #pTargetAngles0Lfk = [ (96.99678999),10.55418621,10.55418621,-40.52489326, 0 ]
    
    pTargetAnglesR = pTargetAngles0R
    pTargetAnglesRadR = [0.0] * 6
    for a in range(len(pTargetAnglesR)):
	pTargetAnglesRadR[a] = math.radians(pTargetAnglesR[a])
    motionProxy.setAngles(pRArm, pTargetAnglesRadR, 0.5)
    startingTime = time.time()
    count = 0
    pMaxSpeedFraction = 0.99
    motion1T = 0
    motion2T = 0
    tap =0
    while(startingTime + 150 > time.time()):
	    if(count==1):
		if(pTargetAngles0R==pTargetAnglesR):
			pTargetAnglesR = pTargetAngles1R
		else:
			pTargetAnglesR = pTargetAngles0R	
		count = 0

		for a in range(len(pTargetAnglesR)):
			pTargetAnglesRadR[a] = math.radians(pTargetAnglesR[a])

                tic = time.time()
		motionProxy.angleInterpolationWithSpeed(pRArm, pTargetAnglesRadR , pMaxSpeedFraction)# takes ~.35 sec
		motion2T = motion1T
		motion1T = (time.time()-tic)
		#print(motion1T,motion2T)
	    else:
		motionProxy.setAngles(pRArm, pTargetAnglesRadR, pMaxSpeedFraction)
	    count += 1
	    tap += 1
	    if(tap == 2):
	      tDelay = (1/(bpm/60.0)) - (motion1T + motion2T)
              #print(tDelay)
	      if(tDelay>0):
		time.sleep(tDelay)
	      tap = 0
    for a in range(len(pTargetAnglesR)):
        pTargetAnglesR[a] = math.radians(pTargetAngles1R[a])

    motinoProxy.setAngles(pRArm, pTargetAnglesRadR , pMaxSpeedFraction)

if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python motion_poseZero.py robotIP (optional default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIp = sys.argv[1]
    else:
	robotIp = sys.argv[1]
	bpm = float(sys.argv[2])*60.0
        print(bpm)
    print(bpm)
    main(robotIp)
