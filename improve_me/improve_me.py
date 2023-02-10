def validPath(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    # for i in edges:
    #     if source in edges
    pass


def longest_length(str_test):
    """
    3. 无重复字符的最长子串
    s = '131967498416321'

    output = longest_length(s)
    print(output)
    """
    if not str_test:
        return 0
    max_length = 0
    left = 0
    # now = 0
    store_str = []
    for i in range(len(str_test)):
        while str_test[i] in store_str:
            store_str.remove(str_test[left])
            left += 1
        store_str.append(str_test[i])
        max_length = len(store_str) if max_length < len(store_str) else max_length

    return max_length


def de_gui(begin, end, all_lian_jie):
    k = set()
    for i in begin:
        for j in all_lian_jie:
            if i in j:
                k += i.remove(source)
    if end in k:
        return True
    else:
        return de_gui(k, end, all_lian_jie)


if __name__ == '__main__':
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 2
    # # output = validPath(n, edges, source, destination)
    # # print(output)
    # 广度
    # 已经遍历过的数据
    # traversed = set()
    # traversed.add(source)
    # sources = [source]
    #
    # for source in sources:
    #     a = []
    #     for i in edges:
    #         if source in i:
    #             a += i.remove(source)
    #     for b in set(a):
    #         traversed.add(b)
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]


    p = list(range(n))
    for u, v in edges:
        p[find(u)] = find(v)
    print(find(source) == find(destination))
