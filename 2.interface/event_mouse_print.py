import cv2

event_dict = { eval('cv2.'+name) : name  
                 for name in dir(cv2) 
                      if 'EVENT_' in name 
                          and 
                         'EVENT_FLAG_' not in name}
flag_dict = { eval('cv2.'+name) : name
               for name in dir(cv2)
                     if 'EVENT_FLAG_' in name}

def onMouse(event, x, y, flags, param):
    evt_name = event_dict.get(event)
    flag_name = flag_dict.get(flags)
    print( evt_name, x, y , "%s(%d)"%(flag_name,flags))

img = cv2.imread('../img/blank_500.jpg')
cv2.imshow('mouse event', img)
cv2.setMouseCallback('mouse event', onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27: # esc로 종료
        break
cv2.destroyAllWindows()