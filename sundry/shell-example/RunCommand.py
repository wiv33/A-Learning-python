import os

# 파이썬이 재미있는 이유

# pip install pyinstaller
# pyinstaller --onefile {fileName}

# pyinstaller --onefile --icon {iconFile} {pythonFile}

chk = input("중앙일보: a\n매체확장: e\n")
target = ""
if chk == "a":
    target = "ilbo"
elif chk == "e":
    target = "ext"
else:
    raise "입력 값은 해당사항 없음: [{}]".format(chk)

scriptStr = ""
f = open("C:\\dev\\gm_setting\\{0}.txt".format(target), 'r')
for line in f:
    scriptStr += line.replace("\n", " ^& ")

f.close()
""" 옵션 중 현재 사용할 옵션
    --noconsole # Dos console off
    -F, --onefile 실행파일 하나로 생성
"""
os.system("start cmd /c title RUN GM SCRIPT ^&^& {0} pause".format(scriptStr))
