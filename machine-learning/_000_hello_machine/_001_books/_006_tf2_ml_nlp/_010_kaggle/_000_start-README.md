# Kaggle

    데이터 과학자의 놀이터
    자신이 만든 모델을 다른 사람의 모델과 비교하며 공부할 수 있는 공간
    캐글에는 많은 자연어 처리 문제가 있어,
    참고하여 공부하는 것을 권장

Install
-

```shell script
pip3 install kaggle
```

Authentication
-

    API 활용을 위해 kaggle.json을 
    /root/.kaggle/
    경로에 생성해야 한다.
    {"username":"username","key":"api-key"}

Download data
-

```shell script
kaggle competitions download -c <competition-name>
```

Retrieve data list
-

```shell script
kaggle competitions files -c <competition-name>
```

Submit data
-

```shell script
kaggle competitions submit <competition-name> -f <file-name> -m <message>
```

대회 목록 확인
-

```shell script
kaggle competitions list
```
