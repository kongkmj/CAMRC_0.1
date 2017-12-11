from flask import Flask # 서버프레임워크
from flask import render_template, request # 템플릿, 리퀘스트
import RPi.GPIO as GPIO #GPIO 라이브러리
import time #time 라이브러리
app = Flask(__name__)

# move 핀 설정
leftPin = 5
rightPin = 6
fowardPin = 13
backwardPin =19

# camera 핀 설정
upPin= 9
downPin=11

GPIO.setwarnings(False) # 경고제거
GPIO.setmode(GPIO.BCM) # 라즈베리파이 BCM 방식
# 핀 OUT 설정
GPIO.setup(leftPin, GPIO.OUT)
GPIO.setup(rightPin, GPIO.OUT)
GPIO.setup(fowardPin, GPIO.OUT)
GPIO.setup(backwardPin, GPIO.OUT)

# 초기값 제로
GPIO.output(leftPin,0)
GPIO.output(rightPin,0)
GPIO.output(fowardPin,0)
GPIO.output(backwardPin,0)

print " setup done"

# 라우팅

# 메인
@app.route("/") 
def index():
    return render_template('index.html')

# 좌회전
@app.route('/left_side')
def left_side():
    data1="LEFT"
    GPIO.output(leftPin,1)
    GPIO.output(rightPin,0)
    GPIO.output(fowardPin,0)
    GPIO.output(backwardPin,0)
    return 'true'

# 우회전
@app.route('/right_side')
def right_side():
   data1="RIGHT"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,1)
   GPIO.output(fowardPin,0)
   GPIO.output(backwardPin,0)
   return 'true'

# 전진
@app.route('/foward_side')
def up_side():
   data1="FORWARD"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,0)
   GPIO.output(fowardPin,1)
   GPIO.output(backwardPin,0)
   return 'true'

# 후진
@app.route('/back_side')
def down_side():
   data1="BACK"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,0)
   GPIO.output(fowardPin,0)
   GPIO.output(backwardPin,1)
   return 'true'

# 정지
@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,0)
   GPIO.output(fowardPin,0)
   GPIO.output(backwardPin,0)
   return  'true'

# 카메라 상
@app.route('/up')
def up():
   data1="UP"
   GPIO.output(downPin,0)
   GPIO.output(upPin,1)
   return 'true'

# 카메라 하
@app.route('/down')
def down():
   data1="DOWN"
   GPIO.output(upPin,0)
   GPIO.output(downPin,1)
   return 'true'

# 카메라 정지
@app.route('/camStop')
def cam_stop():
   data1="CAMSTOP"
   GPIO.output(upPin,0)
   GPIO.output(downPin,0)
   return 'true'

# 서버리스닝
if __name__ == "__main__":
 print "Start"
 app.run(host='0.0.0.0',port=5010)
