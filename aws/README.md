# Python에서 AWS 다루기
<br>

## 설치  
Python에서는 기본적으로 `boto3` 라는 Python 라이브러리를 이용하여 개발합니다.  
그렇기에 이를 설치하도록 합니다.
```commandline
pip install boto3
```

<br>

## 설정 방법
AWS를 이용하려고 하면 기본적으로 두 가지의 Key가 필요합니다.  
바로 ACCESS_KEY와 SECRET_ACCESS_KEY가 있습니다. 파이썬에서 이용할 때 두 가지 방법이 있는데 하나는 코드에 직접 입력하는 방법이고 또 다른 방법은 PC에 미리 설정하는 방법입니다.
코드에 직접 입력하는 방법은 보안상 좋지 않기 때문에 PC에 설정하는 것을 진행합니다.

