"""
this is an example usage of the handTracking module provided
install mediapipe and opencv2 before proceeding

Serotonin
"""
from pyBodyTrack.poseTrack import posedetect
tracker = posedetect()

def callback(): #used to run code while tracker is running
    print(tracker.landmarks[tracker.landmark.NOSE].x)   #print x value of the NOSE landmark
    
tracker.detect(callback=callback)#specify callback function when running model
#press ESC to exit from opencv window
