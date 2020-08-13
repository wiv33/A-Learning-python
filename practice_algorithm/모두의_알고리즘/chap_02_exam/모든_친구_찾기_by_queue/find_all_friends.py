# 입력: 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력: 모든 친구의 이름

def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        p, i = qu.pop(0)
        print(p, i)
        for x in g[p]:
            if x not in done:
                qu.append((x, i + 1))
                done.add(x)


friends = {
    'summer': ["john", "justin", "mike"],
    'john': ["summer", 'justin'],
    'justin': ['john', 'summer', 'mike', 'may'],
    'mike': ['summer', 'justin'],
    'may': ['kim'],
    'kim': ['may'],
    'tom': ['jerry'],
    'jerry': ['tom'],
}

print_all_friends(friends, 'summer')
print("==================================")
print_all_friends(friends, 'jerry')
