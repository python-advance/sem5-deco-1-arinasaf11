def time_decorator(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print("Время выполнения: ", time.time() - t)       
        return res
    return wrapper

@time_decorator
def plus(x, y):
    print("%d + %d = %d" % (x, y, x + y))
    return x + y

plus(2, 3)
