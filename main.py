import itertools
from tqdm import tqdm


def ten2bin(num) -> str:
    """ 十进制转二进制，方便对真值表进行迭代 """
    la = []
    if num < 0:
        return '-' + ten2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        la.append(str(remainder))
        if num == 0:
            return ''.join(la[::-1])


def truthTableGenerator(n) -> str:
    max_iterate_time = 2 ** n
    iterate_time = 0

    while iterate_time < max_iterate_time:
        s = ten2bin(iterate_time)
        s = (n - len(s)) * '0' + s  # 补0
        yield s
        iterate_time += 1
    return


def getSubSet(original_list):
    _subsets = []
    for truthTableStr in truthTableGenerator(len(original_list)):
        subset = []
        for index, value in enumerate(truthTableStr):
            if value == "1":
                subset.append(original_list[index])
        _subsets.append(set(subset))
    return _subsets


def whetherCanFindTwoSubSetWhoseSumAreEqual(subsets: list):
    return len(set(list(map(lambda subset: sum(subset), subsets)))) != len(subsets)


def whetherThisNCanMeetTheRequirements(_n):
    flag = True
    for num_list in tqdm(itertools.permutations(list(range(10, 100)), _n)):
        subsets_of_num_list = getSubSet(num_list)
        if not whetherCanFindTwoSubSetWhoseSumAreEqual(subsets_of_num_list):
            flag = False
            break
    print(f"n取{_n}时", "全部都可以满足条件" if flag else "不全满足条件")
    return flag


if __name__ == '__main__':
    # whetherThisNCanMeetTheRequirements(10)
    # print(whetherCanFindTwoSubSetWhoseSumAreEqual(getSubSet([88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])))
    for n in range(1, 11):
        print(f"正在计算{n}")
        whetherThisNCanMeetTheRequirements(n)
