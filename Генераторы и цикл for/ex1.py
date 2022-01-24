def square(x):
    return x * x

def print_map(func, iterable):
    i = min(iterable)
    while i <= max(iterable):
        if i in iterable:
            print(func(i))
        i += 1
