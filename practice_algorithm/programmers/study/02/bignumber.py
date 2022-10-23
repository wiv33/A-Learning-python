def solution(numbers):
    num_list = list(map(str, numbers))
    num_list.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(num_list)))


def solution2(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    if numbers[0] == '0':
        return '0'
    answer = ''.join(numbers)
    return answer


if __name__ == '__main__':
    assert "6210" == solution([6, 10, 2])
    assert "9534330" == solution([3, 30, 34, 5, 9])
