def binary_search(s_things, lst):
    l = 0
    r = len(s_things)
    found = False
    while l + 1 < r:
        m = int((l + r) / 2)
        if lst[m] == s_things:
            l = r = m
            found = True
        elif s_things[m] > val:
            r = m
        else:
            l = m + 1
    if found:
        print(f'Элемент найден под индексом: {l}')
    else:
        print('Элемент не найден')


def bubble_sort(sear):
    for k in range(1, len(sear)):
        for i in range(1, len(sear) - k + 1):
            if sear[i] < sear[i - 1]:
                sear[i - 1], sear[i] = sear[i], lst[i - 1]
    return sear