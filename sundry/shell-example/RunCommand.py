import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# 파이썬이 재미있는 이유

# pip install pyinstaller
# pyinstaller --onefile {fileName}

# pyinstaller --onefile --icon {iconFile} {pythonFile}

# 1::삭제할 부분
# chk = input("중앙일보: a\n매체확장: e\n")
# target = ""
# if chk == "a":
#     target = "ilbo"
# elif chk == "e":
#     target = "ext"
# else:
#     raise "입력 값은 해당사항 없음: [{}]".format(chk)
# 1::삭제할 부분
print(os.path.dirname(os.path.realpath(__file__)))
if __name__ == '__main__':
    print(__name__)
    import MakeDir

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))

getExeName = MakeDir.make_dir_func()
print(getExeName)
scriptStr = ""
f = open("C:\\dev\\gm_setting\\{0}.txt".format(getExeName), 'r')
for line in f:
    scriptStr += line.replace("\n", " ^& ")

f.close()
""" 옵션 중 현재 사용할 옵션
    --noconsole # Dos console off
    -F, --onefile 실행파일 하나로 생성
"""
os.system("start cmd /c title RUN GM SCRIPT ^&^& {0} pause".format(scriptStr))
