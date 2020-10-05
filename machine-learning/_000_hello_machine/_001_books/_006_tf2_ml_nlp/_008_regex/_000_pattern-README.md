# 표현식

---

| expression | description |
| :---: | :--- |
| `.` | 줄바꿈을 제외한 모든 문자 |
| `^` | 문자열의 시작 |
| `$` | 문자열의 끝 |
| `*` | 앞에 있는 문자가 0회 이상 반복된 문자열 |
| `+` | 앞에 있는 문자가 1회 이상 반복된 문자열 |
| `{m}` | 앞 문자를 m회 반복하는 문자열 |
| `{m,n}` | 앞 문자를 m부터 n회 반복하는 문자열 |
| `?` | 앞 문자가 나오거나 나오지 않는 문자열 (`{0, 1}`과 동일) |
| `\d` | 숫자 |
| `\D` | 숫자가 아닌 문자 |
| `\w` | 문자 혹은 숫자 |
| `\W` | 문자 혹은 숫자가 아닌 것 |
| `(...)` | 괄호 안의 모든 정규 표현식을 만족하는 문자 |
| `[abc]` | a, b, c 중 한 개의 문자와 일치|


```python
import re
re_pattern = re.compile('\w+')
res = re.search('(\w+)', 'wow, it is awesome')
```

re
=

compile(pattern)
-
    특정 기호를 정규 표현식 객체로 만들어준다.
    해당 패턴의 객체로 만들어 재사용 용이
    
search(pattern, words)
-
    패턴에 해당되는 문자열을 반환
    위 예제에서
    res = search(문자 혹은 숫자 1회 이상, words)
    
    span=(0,3)
    match='wow'
    출력
    

spilt(pattern, words)
-
    `pattern`을 만족하는 문자열을 리스트화

sub(pattern, repl, words)
-
    `pattern`을 만족하는 문자를
    `repl`로 치환한다. 
    re.sub("\d", "number", "7 day")
    >>> number day
    