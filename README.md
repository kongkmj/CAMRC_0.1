# 전자공학실험4 오후 13조(CAMRC카)

Web으로 조종하는 CAM RC카


### 시작하기에 앞서

필요한 것들

1) 라즈베리파이3
2) 아두이노 키트
3) 보조배터리

![연결구도](./readme_img/1)
![회로도](./readme_img/2)

```
예시도 제공하세요
```

### 설치하기

1. motion
2. python-pip
3. flask

라즈베리파이 업데이트 & 업그레이드
```
$ sudo apt-get update & upgrade
```
카메라 라이브러리 설치
```
$ sudo apt-get install motion
```

파이썬 패키지매니저 설치
```
$ sudo apt-get install python-pip
```

플라스크 설치
```
$ sudo pip install flask
```
### motion 설정 변경
```
$ sudo vi /etc/default/motion
```

1) start_motion_daemon = yes 로설정

```
$ sudo vi /etc/motion/motion.conf
```

#### 필수설정
1) daemon = off 에서 on으로 설정 => 백그라운드에서 돌리기
2) webcam_localhost = on 에서 off 로 설정 => 외부에서 접속할수 있도록 설정

#### 카메라옵션
1) width 640 (추천)  => 자신이 원하는 크기로 너무크면 영상의 속도가 느려진다.
2) height 480 (추천)  => 자신이 원하는 크기로 너무크면 영상의 속도가 느려진다.
3) framerate 1000 (높은수치 설정) => frame설정을 30이상 올려도 비슷하다 그냥 1000으로 하였다.
4) webcam_port 8081 (기본)  =>webcam의 화면을 띄워줄 포트 번호

### html 수정

```
$ sudo vi /templates/index.html
```
자신의 라즈베리파이 ip로 수정을 하야한다.

<img src="http://192.168.43.141:8081" class="img-responsive" id="test" />

## 테스트 실행하기

```
$ sudo python app.py
```

### End-to-End 테스트

```
라즈베리파이와 공유된 인터넷으로 http://라즈베리파이의ip:5010 으로 접속
```


```
예시도 재공하세요
```

### 코딩 스타일 테스트

이 단위 테스트가 테스트하는 항목을 설명하고 테스트를 하는 이유를 적어주세요.

```
예시도 재공하세요
```


## 배포

추가로 실제 시스템에 배포하는 방법을 노트해 두세요.

## 사용된 도구

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - 웹 프레임워크
* [Maven](https://maven.apache.org/) - 의존성 관리 프로그램
* [ROME](https://rometools.github.io/rome/) - RSS 피드 생성기

## 기여하기

[CONTRIBUTING.md](https://gist.github.com/iamtaeuk/aafc154da8ad3ffb3f3eeeac61a04901) 를 읽으신 후 기여를 해주십시오. 자세한 Pull Request 절차와 행동 규칙을 확인하실 수 있습니다.

## 버전 관리

[SemVer](http://semver.org/) (을)를 사용하여 버전을 관리합니다. 자세한 방법은 레포지토리의 [테그(tags)](https://github.com/your/project/tags)를 확인해 주십시오.

## 저자

* **Billie Thompson** - *초기작* - [PurpleBooth](https://github.com/PurpleBooth)
* **Taeuk Kang** - *한국어 번역* - [GitHub](https://github.com/iamtaeuk) / [Keybase](https://keybase.io/taeuk)


[기여자 목록](https://github.com/your/project/contributors)을 확인하여 이 프로젝트에 참가하신 분들을 보실 수 있습니다.

## 라이센스

이 프로젝트는 MIT 허가서를 사용합니다 - [LICENSE.md](LICENSE.md) 파일에서 자세히 알아보세요.

## 감사 인사

* 본인의 코드가 사용된 분께 경의를 표합니다
* 영감
* etc (등)

---
