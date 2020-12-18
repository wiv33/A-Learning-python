secure = 0

secure_yn = input("1. 암호화 2. 암호 해석 중 선택 : ")
in_file_name = input("입력 파일명을 입력하세요 : ")
out_file_name = input("출력 파일명을 입력하세요 : ")

if secure_yn == "1":
    secure = 100
elif secure_yn == '2':
    secure = -100

in_file = open(in_file_name, 'r', encoding='UTF-8')
out_file = open(out_file_name, 'w', encoding='UTF-8')

while True:
    in_str = in_file.readline()
    if not in_str:
        break

    out_str = ''
    for i in range(0, len(in_str)):
        ch = in_str[i]
        ch_num = ord(ch)
        ch_num = ch_num + secure
        ch2 = chr(ch_num)
        out_str = out_str + ch2

    out_file.write(out_str)

out_file.close()
in_file.close()
print(f'변환 완료: {in_file_name} -> {out_file_name}')
# 1: raw_data.txt / secure_data.txt
