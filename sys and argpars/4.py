import datetime
import os
import sys


def decorator_maker():
    def my_decorator(func):
        def wrapped(*function_arg):
            with open('logs.txt', 'w') as file:
                time = datetime.datetime.now()
                file.write(str(time) + '\n')
                file.write(str(function_arg) + '\n')
                x = func(function_arg)
                if x:
                    file.write(str(x) + '\n')
                else:
                    file.write('-\n')
                file.write(str(datetime.datetime.now()) + '\n')
                file.write(str(datetime.datetime.now() - time) + '\n')
                file.close()
        return wrapped
    return my_decorator

@decorator_maker()
def decorated_function_with_arguments(*function_arg):
    x = 1
    for i in range(1000):
        print(i)
    return 'return'



decorated_function_with_arguments(1, 2, 3, 4)
#path_ = input()
#os.chdir(os.path.abspath(path_))
