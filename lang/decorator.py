
import functools


def repeat(_func=None, *, num_times=1):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            val = None
            for _ in range(num_times):
                val = func(*args, **kwargs)
            return val
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat(num_times=10)
def print_hello():
    print('hello, decorator')


if __name__ == '__main__':
    print_hello()