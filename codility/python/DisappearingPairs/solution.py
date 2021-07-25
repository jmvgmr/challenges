def solution(S):
    # write your code in Python 3.6
    result = []
    for c in S:
        if result and c == result[-1]:
            result.pop()
            continue
        else:
            result.append(c)
    return ''.join(result)


try:
    assert solution('ACCAABBC') == 'AC'
    assert solution('ABCBBCBA') == ''
    assert solution('BABABA') == 'BABABA'
    print('Success!')
except AssertionError:
    print('Error!')
