item = []


def set_mean(lst): # 평균을 구하는 함수입니다
    mean = sum(lst) / len(lst)
    mean = float("{:.1f}".format(mean))
    return mean
def sort_and_divide(lst): # 평균을 기준으로 대소를 비교하여 두 개의 리스트로 나눈 후 병합하는 함수를 호출합니다
    if len(lst) <= 1:
        return lst
    else:
        mean = set_mean(lst)
        left_lst = [x for x in lst if x <= mean]
        right_lst = [x for x in lst if x > mean]
        left_lst = sort_and_divide(left_lst)
        right_lst = sort_and_divide(right_lst)
        return merge_lists(left_lst, right_lst)
def merge_lists(lst1, lst2): # 두 리스트를 하나의 리스트로 병합합니다
    result = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result += lst1[i:]
    result += lst2[j:]
    return result

def find_mid_num(lst): # 중앙값을 찾아냅니다.
    if len(lst) % 2 == 1:
        return lst[int(len(lst)/2)]
    else:
        lst = lst[int(len(lst)/2)- 1:int(len(lst)/2) + 1]
        return set_mean(lst)

while True:
    s = input("input value: ")
    if s == ".":
        sorted_lst = sort_and_divide(item)
        print("Sorted list:", sorted_lst)
        print("The middle number is", find_mid_num(sorted_lst))
        break
    elif s == "":
        continue
    item.append(int(s))

    