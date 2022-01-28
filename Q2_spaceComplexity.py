from memory_profiler import profile
@profile

def my_func():
    a = [1, 2, 2, 4, 5]
    b = [2, 0, 3]
    del b
    return a

if __name__ == '__main__':
    my_func()

