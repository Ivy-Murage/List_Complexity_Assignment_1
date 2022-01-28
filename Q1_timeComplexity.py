from timeit import Timer

def check_time():
    numbers = []
    for i in range(20):
        numbers.append(i)


if __name__=='__main__':
    t = Timer("check_time()", "from __main__ import check_time")
    print (f"The time complexity is : {t.timeit()}")
