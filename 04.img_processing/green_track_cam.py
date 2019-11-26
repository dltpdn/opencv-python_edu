'''
초록색 물체를 추적하는 카메라 
최소 단순 버전
SW PWM 사용
'''

import cv2
import numpy as np
import wiringpi as wpi
import RPi.GPIO as GPIO

PIN_SERVO_X = 18
WIDTH, HEIGHT = 480, 320
CENTER_MARGIN = 50
STEP_X = 5

ANGLE_X_MAX = 150
ANGLE_X_MIN = 30
MIN_RADIUS = 10

colorLower = np.array([60, 100,100])
colorUpper = np.array([70, 255,255])

angle_x = 90

(prev_x, x) = -1,-1 
dir_x= 0

class ServoDriver():

    def __init__(self, PIN_SERVO, hw=False, min_angle=0, max_angle=180):
        self.PIN_SERVO = PIN_SERVO
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.hw = hw
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_SERVO, GPIO.OUT)
        if hw :
            wpi.wiringPiSetupGpio()
            wpi.pinMode(self.PIN_SERVO, wpi.PWM_OUTPUT)
            wpi.pwmSetMode(wpi.PWM_MODE_MS)
            wpi.pwmSetClock(192) #19.2MHz / 384 = 50000Hz = 50KHz(0.02ms)
            wpi.pwmSetRange(2000) # 0.02ms * 1000 = 20ms, 50KHz / 1000 = 50Hz
        else:
            self.pwm = GPIO.PWM(PIN_SERVO,50)
            self.pwm.start(0)
        
    def setAngle(self, angle):
        if angle < self.min_angle :
            angle = self.min_angle 
        if angle > self.max_angle :
            angle = self.max_angle 

        if self.hw:
            value = (240-60)/180 * angle + 60 # 0.6ms~2.4ms => 0.6ms :60, # 2.4ms: 240
            #print("value:", value)
            wpi.pwmWrite(self.PIN_SERVO, int(value))
        else:
            value = (10)/180 * angle + 2.5 # 2.5~12.5, 
            #print("value:", value)
            self.pwm.ChangeDutyCycle(value) 
        
    def stop(self):
        if self.hw:
            wpi.pwmSetMode(wpi.PWM_MODE_BAL)
            wpi.pwmSetClock(0)
            wpi.pwmSetRange(1024)
            wpi.pinMode(self.PIN_SERVO, wpi.INPUT)
        else:
            self.pwm.stop()

#servo_x = ServoDriver(PIN_SERVO_X, hw=False)

# hw=True : h/w pwm, must with sudo
servo_x = ServoDriver(PIN_SERVO_X, hw=True)

# 타겟을 화면 중심에 두기 위해 서보를 조금씩 이동 시키는 함수
def tracePosition(x):
    global angle_x, dir_x
    if (x < (WIDTH/2-CENTER_MARGIN)): #center = 240 = 480/2
        angle_x += STEP_X
        if angle_x > ANGLE_X_MAX:
            angle_x = ANGLE_X_MAX
            return False
        servo_x.setAngle(angle_x)
        dir_x = 1
        print("<---", x, prev_x)
    elif (x > (WIDTH/2+CENTER_MARGIN)):
        angle_x -= STEP_X
        if angle_x < ANGLE_X_MIN:
            angle_x = ANGLE_X_MIN
            return False
        servo_x.setAngle(angle_x)
        dir_x = -1
        print("--->", x, prev_x)
    else:
        print("--|--", x)
        dir_x = 0
    return True
   
    
def main():
    global prev_x, x, WIDTH, HEIGHT
    servo_x.setAngle(angle_x)

    cap = cv2.VideoCapture(0)    # 0번 카메라 연결
    WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    try:
        while cap.isOpened:
            ret, frame = cap.read()
            if ret:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, colorLower, colorUpper)
                mask = cv2.erode(mask, None, iterations=2)
                mask = cv2.dilate(mask, None, iterations=2)
            
                _, cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)
                center = None
                
                if len(cnts) > 0:
                    c = max(cnts, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(c)
                    
                    # 둘레가 10 이상인것만
                    if radius >= MIN_RADIUS:
                        M = cv2.moments(c)
                        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                        # 초록 동그라미            
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                            (0, 255, 255), 2)
                        # 중심 빨간점
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        
                        #이전 좌표에서 5이상 움직이면
                        if abs(prev_x - x) > 5:
                            prev_x = x
                            tracePosition(int(x))
                            
                if not center:
                    # do noting
                    print("lost") 

            
                cv2.imshow("Frame", np.hstack( (frame, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)) ))
                if cv2.waitKey(1) & 0xFF  == 27: #ESC
                        break
            else:
                break
    finally:
        print("\n [INFO] Exiting Program and cleanup stuff \n")
        cap.release()
        cv2.destroyAllWindows()
        servo_x.stop()
    
if __name__ == '__main__':
    main()