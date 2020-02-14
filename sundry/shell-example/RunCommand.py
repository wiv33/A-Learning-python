import inspect
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
# print(os.path.dirname(os.path.realpath(__file__)))
if __name__ == '__main__':
    # print(__name__)
    import MakeDir

base_file_name = MakeDir.make_dir_func()
# print("base_file_name: %s" % base_file_name)

# split___ = os.path.basename(inspect.getfile(inspect.currentframe())).split(".")[0]
# print(split___)

scriptStr = ""
root = "C:\\dev\\gm_setting"

pf = open("{}\\delete_symbolic.txt".format(root), 'r')
for line in pf:
    scriptStr += line.replace("\n", " ^&^& ")
pf.close()

f = open("{1}\\{0}.txt".format("ilbo", root), 'r')
for line in f:
    scriptStr += line.replace("\n", " ^&^& ")

f.close()
""" 옵션 중 현재 사용할 옵션
    --noconsole # Dos console off
    -F, --onefile 실행파일 하나로 생성
    -n {name}, --name {name} 파일 이름 변경
"""
os.system("start cmd /c title RUN GM SCRIPT ^&^& {0} pause".format(scriptStr))
