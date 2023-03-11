
# Test data [1,2, 4], [-1,-3], [1,2,3]
def solution(A):
    a_list = sorted(A)

    if 1 not in a_list or a_list[-1] < 0:
        return 1

    for index in range(len(A)):
        if index + 1 == len(A):
            return a_list[index] + 1
        elif a_list[index + 1] - a_list[index] > 1 and a_list[index] + 1 > 0:
            return a_list[index] + 1