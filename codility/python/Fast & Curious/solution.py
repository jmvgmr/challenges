def solution(A):
    # write your code in Python 3.6
    mod = 10 ** 9 + 7
    total = 0
    distances = [0] * len(A)
    for i, a in enumerate(A):
        distances[i] = A[-1] - a
        total += distances[i]

    result = total - distances[0]
    temp = result
    for i, a in enumerate(A[:-1], 1):
        temp = temp - distances[i] + i * (A[i] - A[i - 1])
        if result > temp:
            result = temp

    return result % mod


try:
    assert solution([1, 5, 9, 12]) == 7
    assert solution([5, 15]) == 0
    assert solution([2, 6, 7, 8, 12]) == 9
    assert solution([k * (5 * 10 ** 7) for k in range(20)]) == 499999972
    print('Success!')
except AssertionError:
    print('Error!')
