def my_fib_range(a):
    pipe = [1, 1]
    i = 0
    _current = pipe[0]
    while True:
        yield _current
        if i < 2:
            _next = pipe[1]
        else:
            _next = pipe[0] + pipe[1]
            pipe[0], pipe[1] = pipe[1], _next
        if i > a:
            break
        i += 1
        _current = _next


for i in my_fib_range(1500090):
    print(len(str(i)))
