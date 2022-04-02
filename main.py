import itertools
from tqdm import tqdm
from scipy.special import comb
import random


def getSubSet(original_list):
    """https://blog.csdn.net/xjtuse123/article/details/99202846"""
    N = len(original_list)
    results = []
    for i in range(2 ** N):  # 子集个数，每循环一次一个子集
        result = []
        for j in range(N):  # 用来判断二进制下标为j的位置数是否为1
            if (i >> j) % 2:
                result.append(original_list[j])
        results.append(result)
    return results


def whetherCanFindTwoSubSetWhoseSumAreEqual(subsets: list):
    return len(set(list(map(lambda subset: sum(subset), subsets)))) != len(subsets)


def whetherThisNCanMeetTheRequirements(n):
    flag = True
    comb_num = comb(90, n)
    print(f"n取{n}时, 共有{comb_num}种组合方式")

    # n<7 的时候，数据量还不算太大，且经过验证，对于 n=7 时，在第 637108 个元素时就会出现不满足条件的情况
    if n < 7:
        for num_list in tqdm(itertools.permutations(list(range(10, 100)), n), total=comb_num):
            subsets_of_num_list = getSubSet(num_list)
            if not whetherCanFindTwoSubSetWhoseSumAreEqual(subsets_of_num_list):
                flag = False
                break
    # n > 7 时，随机1000000次，若均满足条件，算为满足条件
    else:
        for _ in tqdm(range(1000000)):
            original_numbers = []
            while len(original_numbers) < n:
                if (new_number := random.randint(10, 90)) not in original_numbers:
                    original_numbers.append(new_number)
            subsets_of_num_list = getSubSet(original_numbers)
            if not whetherCanFindTwoSubSetWhoseSumAreEqual(subsets_of_num_list):
                flag = False
                break

    print(f"n取{n}时", "全部都可以满足条件" if flag else "不全满足条件")
    return flag


if __name__ == '__main__':
    # whetherThisNCanMeetTheRequirements(10)
    # print(whetherCanFindTwoSubSetWhoseSumAreEqual(getSubSet([88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])))
    for n_to_be_verified in range(1, 11):
        print(f"-----------\n正在计算{n_to_be_verified}")
        whetherThisNCanMeetTheRequirements(n_to_be_verified)
