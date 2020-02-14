import os, shutil
import stat

"""TODO LIST
* 현재 실행 파일의 위치를 파악
* /dev/gm_setting/ 디렉토리가 있는지 확인
    - 없을 경우 Directory 생성
* 총 3개의 파일이 있는지 여부 확인
    - 각 파일의 길이가 0보다 큰 지 아닌지 확인
        - 없거나 0이면 현재 실행 파일에서 copy 해줌.

END


* 현재 실행 파일의 이름을 가져옴
    - cmd 실행할 때 ext, ilbo의 값을 실행 파일의 이름으로 전달해 줄 예정
    
"""


def make_dir_func():
    gm_setting = "C:\\devs\\gm_setting"
    if not os.path.exists(gm_setting) \
            or not os.path.exists(gm_setting + "\\delete_symbolic.txt.txt")\
            or not os.path.exists(gm_setting + "\\ilbo.txt")\
            or not os.path.exists(gm_setting + "\\ext.txt"):
        if os.path.exists(gm_setting):
            os.chmod(gm_setting, 0o775)

        os.makedirs(gm_setting,mode=0o775)
        for commandFile in os.listdir(os.getcwd()):
            print(commandFile)
            if os.path.basename(__file__) != commandFile\
                    and commandFile != "RunCommand.py"\
                    and commandFile != "__pycache__":
                # temp = open(commandFile, 'r')
                shutil.copy(commandFile, gm_setting)
                # temp.close()

    return os.path.basename(__file__)
    # print(os.getcwd())
    # print(os.listdir(os.getcwd()))


if __name__ == '__main__':
    make_dir_func()

