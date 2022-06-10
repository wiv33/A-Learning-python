def run():
    import re

    result = []
    s = []
    arr = [re.sub('[\n]', '', x) for x in
           open("/Users/nhn/PycharmProjects/A-Learning-python/sundry/ETC/txt_lines.txt").readlines()]
    for i, x in enumerate(arr, 1):
        if x.startswith("연차 생성"):
            x = f'<b><span style="color:#e11d21">{x}</span></b>'
        x = str(x + '<br>')
        s.append(x)

        if i % 3 == 0:
            ss = str(''.join(s)).ljust(100, ' ')

            result.append(f' {ss} |')
            s = []

    import numpy as np
    from datetime import datetime, timedelta
    from dateutil.relativedelta import relativedelta

    a = list(np.array(result).reshape(2, round(len(result) / 2)))
    baseDate = datetime.strptime('2022-11-01', '%Y-%M-%d').date()
    head = [f'{baseDate + relativedelta(month=x)}' for x in range(0, 13)]
    res = []
    for i in range(len(a[0])):
        res.append(f'| <ul><li class="task-list-item" data-te-task=""></li></ul> | +{i}월 | {a[0][i]} {a[1][i]}')

    # print(' | '.join(head))
    print("""| | n월 | 1일 | 2일 |\n| --- | --- | --- | --- |""")
    print('\n'.join(res))


if __name__ == '__main__':
    run()
