import os
# 파이썬이 재미있는 이유

# pip install pyinstaller
# pyinstaller --onefile {fileName}

# pyinstaller --onefile --icon {iconFile} {pythonFile}

print("중앙일보: a\n매체확장: e\n")
chk = input()
if chk == "a":
    target = "ilbo"
else:
    target = "ext"
scriptStr = ""
for line in open("C:\\dev\\gm_setting\\{0}.txt".format(target), 'r').readlines():
    scriptStr.join(line)
    if line is not None:
        scriptStr.join("&")

""" 옵션 중 현재 사용할 옵션
    --noconsole # Dos console off
    -F, --onefile 실행파일 하나로 생성
"""
os.system("start cmd /c title RUN GM SCRIPT && {}".format(scriptStr))

