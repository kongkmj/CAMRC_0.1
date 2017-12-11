from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

# move
leftPin = 5
rightPin = 6
fowardPin = 13
backwardPin =19

# camera
upPin= 9
downPin=11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftPin, GPIO.OUT)
GPIO.setup(rightPin, GPIO.OUT)
GPIO.setup(fowardPin, GPIO.OUT)
GPIO.setup(backwardPin, GPIO.OUT)
GPIO.output(leftPin,0)
GPIO.output(rightPin,0)
GPIO.output(fowardPin,0)
GPIO.output(backwardPin,0)

print " setup done"
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    GPIO.output(leftPin,1)
    GPIO.output(rightPin,0)
    GPIO.output(fowardPin,0)
    GPIO.output(backwardPin,0)
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,1)
   GPIO.output(fowardPin,0)
   GPIO.output(backwardPin,0)
   return 'true'

@app.route('/foward_side')
def up_side():
   data1="FORWARD"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,0)
   GPIO.output(fowardPin,1)
   GPIO.output(backwardPin,0)
   return 'true'

@app.route('/back_side')
def down_side():
   data1="BACK"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,0)
   GPIO.output(fowardPin,0)
   GPIO.output(backwardPin,1)
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(leftPin,0)
   GPIO.output(rightPin,0)
   GPIO.output(fowardPin,0)
   GPIO.output(backwardPin,0)
   return  'true'

@app.route('/up')
def up():
   data1="UP"
   GPIO.output(downPin,0)
   GPIO.output(upPin,1)
   return 'true'

@app.route('/down')
def down():
   data1="DOWN"
   GPIO.output(upPin,0)
   GPIO.output(downPin,1)
   return 'true'

@app.route('/camStop')
def cam_stop():
   data1="CAMSTOP"
   GPIO.output(upPin,0)
   GPIO.output(downPin,0)
   return 'true'

if __name__ == "__main__":
 print "Start"
 app.run(host='0.0.0.0',port=5010)
