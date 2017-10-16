import cv2

events = [i for i in dir(cv2) if 'EVENT_' in i]
print( len(events) ,"events" )
print( events )
