#include<Servo.h>
Servo Right;
Servo Left;
Servo Cam;

// RC 카 Pin 설정
const int leftPin = A0; // 전진 Pin
const int rightPin = A1; // 후진 Pin
const int fowardPin = A2; // 좌회전 Pin
const int backwardPin = A3; // 우회전 Pin

// 카메라 Pin 설정
const int upPin = 5;
const int downPin = 6;

int camAngle;

void setup() {
 Serial.available();
 Right.attach(10);
 Left.attach(11);
 Cam.attach(9);

 pinMode(fowardPin,INPUT);
 pinMode(backwardPin,INPUT);
 pinMode(leftPin,INPUT);
 pinMode(rightPin,INPUT);
 pinMode(upPin,INPUT);
 pinMode(downPin,INPUT);
 
// RC 카 정지
 Right.writeMicroseconds(1500);
 Left.writeMicroseconds(1500);
 
// Cam 정지
 camAngle=80;
 Cam.write(camAngle);

}


void RC_stop(){
 Right.writeMicroseconds(1500);
 Left.writeMicroseconds(1500);
}

void foward(){
 Right.writeMicroseconds(1300);
 Left.writeMicroseconds(1700);
}

void backward(){
 Right.writeMicroseconds(1700);
 Left.writeMicroseconds(1300);
}

void right_side(){
  Right.writeMicroseconds(1500);
  Left.writeMicroseconds(1700);
}

void left_side(){
  Right.writeMicroseconds(1300);
  Left.writeMicroseconds(1500);
}

void loop() {
  
  if(digitalRead(fowardPin)==HIGH){
    Serial.println("전진");
    foward();
  }
  
  else if(digitalRead(backwardPin)==HIGH){
    Serial.println("후진");
    backward();
  }
  else if(digitalRead(leftPin)==HIGH){
    Serial.println("왼쪽");
    left_side();
  }
  else if(digitalRead(rightPin)==HIGH){
    Serial.println("오른쪽");
    right_side();
  }
  else {
    Serial.println("정지");
    RC_stop();
  }

  if(digitalRead(upPin)==HIGH){
    Serial.println("up");
    if(camAngle>=180){
      camAngle=180;
    }else{
      camAngle++;
      delay(10);
    }
   Cam.write(camAngle); 
  }
  else if(digitalRead(downPin)==HIGH){
    if(camAngle<=0){
      camAngle=0;
    }else{
      camAngle--;   
      delay(10);      
    }
    Cam.write(camAngle);
  }
}
