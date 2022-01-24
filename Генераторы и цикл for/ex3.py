def square(x):
    return x * x

def my_map(func, iterable):
    i = 0
    _current = func(iterable[i])
    while True:
        yield _current
        if i + 1 >= len(iterable):
            break
        _next = func(iterable[i + 1])
        i += 1
        _current = _next

iterable = [1, 3, 6, 8, 9]
for i in my_map(square, iterable):
    print(i)


def my_zip(iterable):
    i = 0
    j = min([len(x) for x in iterable])
    _current = [x[i] for x in iterable]
    while True:
        yield _current
        if i + 1 >= j:
            break
        _next = [x[i + 1] for x in iterable]
        i += 1
        _current = _next

iterable = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 5]
            ]
for i in my_zip(iterable):
    print(i)


def my_enumerate(iterable):
    i = 0
    _current = (i, iterable[i])
    while True:
        yield _current
        if i + 1 >= len(iterable):
            break
        _next = (i + 1, iterable[i + 1])
        i += 1
        _current = _next

iterable = [1, 3, 6, 8, 9]
for i in my_enumerate(iterable):
    print(i)
