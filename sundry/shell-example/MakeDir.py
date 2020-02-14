import inspect
import os, shutil

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
    gm_setting = "C:\\dev\\gm_setting"
    command_files = ["delete_symbolic.txt", "ilbo.txt", "ext.txt"]
    setting_dir = os.path.exists(gm_setting)
    if not setting_dir \
            or not os.path.exists(gm_setting + "\\" + command_files[0])\
            or not os.path.exists(gm_setting + "\\" + command_files[1])\
            or not os.path.exists(gm_setting + "\\" + command_files[2]):
        if setting_dir:
            os.chmod(gm_setting, 0o775)

        os.makedirs(gm_setting, mode=0o775, exist_ok=setting_dir)
        for commandFile in os.listdir(os.getcwd()):
            print(commandFile + ":{}".format(commandFile in command_files))

            if commandFile in command_files:
                # temp = open(commandFile, 'r')
                shutil.copy(commandFile, gm_setting)
                # temp.close()


    return os.path.basename(__file__).split(".")[0]
    # print(os.getcwd())
    # print(os.listdir(os.getcwd()))

class MakeDir:
    pass