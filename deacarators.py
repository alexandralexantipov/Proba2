import time


def decor(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

def time_run(func):
    def wrapper(*arg, **kwargs):
        start = time.perf_counter()
        func(*arg, **kwargs)
        stop = time.perf_counter()
        duration = stop - start
        print(f'Функция {func.__name__} работает {duration:.2f} сек.')
    return wrapper


@decor
def proba():
    print('PROBA')

@time_run
def etalon(n, m):
    print('START')
    time.sleep(n + m)

# proba()
# fn = decor(proba)
# fn()
etalon(3)
