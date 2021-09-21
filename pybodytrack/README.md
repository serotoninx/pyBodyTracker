------------------------------------------------------------
from pyBodyTrack.handTrack import handtrack
tracker = handtrack()
tracker.start()
while True:
	try:
		print(tracker.landmarks[tracker.handlandmarks.WRIST])
	except:
		continue
------------------------------------------------------------