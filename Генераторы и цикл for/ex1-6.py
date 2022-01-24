import itertools

############
####  1
############
def get_cartesian_product(a, b):
    a = list(map(str, a))
    b = list(map(str, b))
    ab = a + b
    ab_set = set(ab)
    ab = list(itertools.product(ab_set, repeat=2))
    ab_final = []
    for i in ab:
        if ab_final.count(i[::-1]) == 0:
            if a.count(i[0]) >= 1 and b.count(i[1]) >= 1 and i[0] != i[1]:
                ab_final.append(i)
    return ab_final

print(get_cartesian_product([1, 2], [4, 5]))


############
####  2
############
def get_permutations(s, n):
    x = [str(x[0] + x[1]) for x in list(itertools.permutations(s, n))]
    x.sort()
    return x

print(get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"])


############
####  3
############
def get_combinations(s, n):
    x = []
    for i in s:
        x.append(i)
    for i in range(2, n + 1):
        y = [str(x[0] + x[1]) for x in list(itertools.combinations(s, i))]
        y.sort()
        x += y
    return x

print(get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"])


############
####  4
############
def get_combinations_with_r(s, n):
    y = [str(x[0] + x[1]) for x in list(itertools.combinations_with_replacement(s, n))]
    y.sort()
    return y

print(get_combinations_with_r("cat", 2))


############
####  5
############
def compress_string(s):
    result = []
    for key, group in itertools.groupby(s, lambda x: x[0]):
        i = 0
        for item in group:
            i += 1
        result.append((i, key))
    return result

print(compress_string("1222311"))


############
####  6
############
def maximize(lists, m):
    arr = []
    for i in lists:
        arr += i
    arr = list(itertools.combinations(arr, len(lists)))
    arr_new = []
    for i in arr:
        flg = True
        for j in range(len(lists)):
            if lists[j].count(i[j]) == 0:
                flg = False
        if flg:
            arr_new.append(i)
    max = 0
    for a, b, c in arr_new:
        if (a**2 + b**2 + c**2) % m > max:
            max = (a**2 + b**2 + c**2) % m
    return max

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000) == 206)
